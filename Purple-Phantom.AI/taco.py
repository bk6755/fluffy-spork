import pandas as pd
import torch
import torch.nn as nn
from torch.nn import functional as F

batch_size = 4
block_size = 2

url = "https://storage.googleapis.com/kagglesdsdata/datasets/2958426/5094410/Conversation.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240129%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240129T135619Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=8ca9f4edb3be267e9f240ef05066d0b153c5c323d689734b876440e4f8c100bf444ed4d9d433d7e2a837076c1786cda908dbef6b5fd12f90c0d14fb9e8d399696f9601039c6219fc85c731c9f858a0ae569b400523b9479c57e77c75b62414341fbf66c062266067fe14350a38a54a0974721180e9c180f0101d2b07bd3d9ee3d8b612aa4018709adb6e4cad09a6ddf4788906fe223e2af6f2278591faf7c76bfd18b48128052ed1d96335bf7bb593b0cf139f72567179b6e0bbc0ba563b4743cc3da318ba3ef96973c0ab7b7d5d314337c44525e8bd92d3ab13d2779be7cf0602591094ad394ab42292b847379c2db9cb730cf8e12171f3489e5678b5f4016c"

QnAconVo1 = pd.read_csv(url)
QnAconVo1.fillna('*', inplace=True)

# Make a sorted set of characters of QnAconVo1
characters = sorted(list(set([char for line in QnAconVo1 for char in line])))

# Create dictionaries for encoding and decoding
encode = {char: number for number, char in enumerate(characters)}
encode['*'] = len(encode)
decode = {number: char for char, number in encode.items()}

# Create an encoding function that handles unknown characters
def encode_text(text, encode_dict):
    return [encode_dict.get(char, encode_dict["*"]) for char in text]

# Apply the encoding function to each line in QnAconVo1
data = [encode_text(str(line), encode) for line in QnAconVo1.values.flatten()]

# Set vocab_size to be larger than the maximum index
vocab_size = len(encode)

# Verify that all indices are within the valid range
assert (vocab_size > 0), "Invalid vocab size"

# Remove any lines that are longer than the block size
data = [x for x in data if len(x) <= block_size]

# Remove any lines that are not a multiple of the block size
data = [x for x in data if len(x) % block_size == 0]

# Print 100 rows of the encoded data
# print(data[:100])

n = int(0.8 * len(data))
train_data = data[:n]
val_data = data[n:]

def get_batch(split):
    data_split = train_data if split == 'train' else val_data
    ix = torch.randint(max(0, len(data_split) - block_size + 1 - batch_size), (batch_size,))
    x = torch.stack([torch.unsqueeze(torch.tensor(data_split[i:i + block_size], dtype=torch.long), dim=0) for i in ix])
    y = torch.stack([torch.unsqueeze(torch.tensor(data_split[i + 1:i + block_size + 1], dtype=torch.long), dim=0) for i in ix])

    x = x.squeeze(0)
    y = y.squeeze(-1)

    y = y.to(torch.long)

    if x.shape != (batch_size, block_size):
        raise ValueError(f"Unexpected shape of x tensor: {x.shape}")

    x, y = x, y

    return x, y

x, y = get_batch('train')

class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

    def forward(self, index, targets=None):
        index = index.transpose(0, 1)
        logits = self.token_embedding_table(index)
        B, T, C = index.shape[0], index.shape[1], self.token_embedding_table.embedding_dim

        if logits.shape != (B, T, C):
            raise ValueError(f"Unexpected shape of logits tensor: {logits.shape}")

        if targets is None:
            loss = torch.tensor(0.0, device=logits.device).unsqueeze(0)
        else:
            logits = logits.view(B*T, C)  # Flatten logits for loss computation
            targets = targets.view(B*T)
            loss = F.cross_entropy(logits, targets)

        return logits.view(B, T, C), loss / T

    def generate(self, index, max_new_tokens):
        index = index.transpose(0, 1)
        for _ in range(max_new_tokens):
            logits, loss = self.forward(index)
            logits = logits[:, -1, :]
            probs = F.softmax(logits, dim=-1)
            index_next = torch.multinomial(probs, num_samples=1)
            index = torch.cat((index[:, 1:], index_next), dim=1)
        return index.transpose(0, 1)

model = BigramLanguageModel(vocab_size)
optimizer = torch.optim.AdamW(model.parameters(), lr=3e-4)
max_iters = 1000

for iter in range(max_iters):
    xb, yb = get_batch('train')
    logits, loss = model.forward(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
    print(loss.item())

context = torch.zeros((1, 1), dtype=torch.long)
generated_chars = list(map(decode.get, model.generate(context, max_new_tokens=500)[0].tolist()))
# print(generated_chars)
# generated_text = ''.join(generated_chars)
# generated_text = generated_text.replace(':', ' ')
# print(generated_text)






