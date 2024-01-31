import pandas as pd 
import torch
import torch.nn as nn
from torch.nn import  functional as F

block_size = 8
batch_size = 4

url = "https://storage.googleapis.com/kagglesdsdata/datasets/2958426/5094410/Conversation.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240129%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240129T135619Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=8ca9f4edb3be267e9f240ef05066d0b153c5c323d689734b876440e4f8c100bf444ed4d9d433d7e2a837076c1786cda908dbef6b5fd12f90c0d14fb9e8d399696f9601039c6219fc85c731c9f858a0ae569b400523b9479c57e77c75b62414341fbf66c062266067fe14350a38a54a0974721180e9c180f0101d2b07bd3d9ee3d8b612aa4018709adb6e4cad09a6ddf4788906fe223e2af6f2278591faf7c76bfd18b48128052ed1d96335bf7bb593b0cf139f72567179b6e0bbc0ba563b4743cc3da318ba3ef96973c0ab7b7d5d314337c44525e8bd92d3ab13d2779be7cf0602591094ad394ab42292b847379c2db9cb730cf8e12171f3489e5678b5f4016c"

QnAconVo1 = pd.read_csv(url)

QnAconVo1.fillna('*' , inplace=True)

characters = sorted(list(set([char for line in QnAconVo1 for char in line])))

encode = {char: number for number, char in enumerate(characters)}
encode['*'] = len(encode) 
decode = {number: char for char, number in encode.items()}

data = torch.tensor([encode.get(char, encode["*"]) for char in QnAconVo1.values.reshape(-1)], dtype=torch.long)

vocab_size = len(characters)

n = int(0.8*len(data))
train_data = data[:n]
val_data = data[n:]

class BigramLanguageModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table  = nn.Embedding(vocab_size, vocab_size)
        self.register_buffer('transition_matrix', torch.randn(vocab_size, vocab_size))

    def forward(self, index, targets=None):
        index = index.transpose(0, 1).contiguous()
        logits = self.token_embedding_table(index)

        if targets is None:
            loss = torch.tensor(0.0, device=logits.device)
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
            loss = F.cross_entropy(logits, targets)

        return logits, loss

    def generate(self, index, max_new_tokens):
        # index is (0, 1) array of indicies in the current context
        for _ in range(max_new_tokens):
            # get the predictions
            logits, loss = self.forward(index)
            # focus only on the last time step
            logits = logits[:, -1, :] # becomes (B, C)
            # apply  softmax to get probabilities
            probs = F.softmax(logits, dim=-1) # (B, C)
            # sample from distribution
            index_next = torch.multinomial(probs, num_samples=1)# (B, 1)
            # append sample index to the running sequence
            index =  torch.cat((index, index_next), dim=1) # (B, T+1)
        return index

model = BigramLanguageModel(vocab_size)
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-2)
learning_rate = 5e-2
max_iters = 1000  

for iter in range(max_iters):
        
    # sample a batch of data
    xb, yb = get_batch('train')
            
    # evaluate the loss
    logits, loss = model.forward(xb, yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
    print(loss.item())

context = torch.zeros((1,1), dtype=torch.long)
generated_chars = list(map(decode.get, model.generate(context, max_new_tokens=500)[0].tolist()))
#print(generated_chars)
#generated_text = ''.join(generated_chars)
#generated_text = generated_text.replace(':', ' ')
#print(generated_text)