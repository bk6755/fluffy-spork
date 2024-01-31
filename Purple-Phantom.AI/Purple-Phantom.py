# import the necessary libraries
import random
from datetime import datetime, timedelta
import csv
import pytz
import requests
import requests as rq
import json
import pandas as pd

















assistant_name = 'Purple-Phantom'

# set the name for the AI Assisstant's Master
assistant_master = 'Kaream Phillips'







# place data for different greetings and resposes to the master greeting if given and let make it a large amount of data
greetings = ['Hello, my name is Purple Phantom. I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hi Kaream, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hey kaream, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hi kaream Phillips, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hey, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hi, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hello, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hi, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Wassup, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hi, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hey, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hi, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hey, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hi, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hey, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hi, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hey, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hi, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hey, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
             'Hello there! Im Purple Phantom, your friendly AI assistant. Whats on your agenda today, kaream?',
             'Hey, its Purple Phantom, your AI assistant! How can I assist you today?',
             'Hi! Purple Phantom here, a AI assistant at your service, What can I do for you?',
             'Hey! Im Purple Phantom, the AI assistant here to help with anything you need. Whats up?',
             'Greetings, Kaream! Purple Phantom at your service. Im your AI assistant, ready for action. What can I do for you today?',
             'Hi there, kaream! Purple Phantom checking in, your trusty AI assistant. What do you need assistance with?',
             'Hey Kaream, Purple Phantom here, your AI assistant! Ready to tackle your tasks. What can I help you with?',
             'Hello, Kaream! Im Purple Phantom, a AI assistant here to make your day smoother. What can I assist you with today?',
             'Hey Master Phillips, its Purple Phantom, your AI assistant! How can I make your day better?',
             'Hi! Purple Phantom here, your AI assistant. Ready and eager to assist you, kaream. Whats on your mind?'
]


# lets set data for a lot of responses to the master greeting if given and lets make it as normal as possible
response_greeting = [ 'Hello, my name is Purple Phantom. I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hi Kaream, I am a AI assistant my name is Purple phantom. I am here to help you with your daily tasks. What can I do for you?',
                 'Hey Kaream, I am a  AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hi Kaream, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hey Kaream, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hi Kaream, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hey Kaream, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Wassup, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hey, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hi, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hey, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hi, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hey, I am a AI assistant. I am here to help you with your daily tasks. What can I do for you?',
                 'Hello there! I\'m AI assistant. What\'s on your agenda today, Kaream?',
                 'Hey, it\'s AI assistant. How can I assist you today?',
                 'Hi! Purple AI assistant here, a freindly AI assistant. What can I do for you?',
                 'Hey Kaream! I\'m AI assistant. Ready to tackle your tasks. What can I help you with?',
                 'Hello, kaream! I am a AI every day assistant here. I\'m your daily assistant, ready to help you with anything you need.',
                 'Hola!, I am a AI assistant here. I\'m ready to help you with your tasks. What can I do for you today?',
                 'Hi! Kaream AI assistant here, your helpful AI assistant. What\'s on your mind?',
                 'Hey, it\'s AI assistant. How can I make your day better?',
                 'Hi! Purple Phantom assistant here, your helpful AI assistant. Ready and eager to assist you, What\'s on your mind?',
                 'Hello, Hola Como Estas! helpful AI assistant here. I\'m Purple Phantom your daily assistant, ready to help you with anything you need.',
                 'Hey how are you, I am Purple phantom a AI assistant here. I\'m ready to help you with your tasks. What can I do for you today?',
                 'Hi! My name is Purple Phantom AI assistant here, your AI assistant. What\'s on your mind?'
]


# lets set a algorithm to make randomized desicion to choose the type of greeting 
# that is said to the master, the type of Purple-Phantom can give is one based on the time of day or the data set

# lets set the main algorithm to make a decision to choose the type of greeting that is said to the master so this will be the desicion that is made

def Greeting_Decision():
    greeting_functions = [Time_greeting, Dataset_greeting]
    Greeting_Choices = random.choice(greeting_functions)
    Greeting_Choices()

# lets define function that will give time based greetings
# for Mississippi time
def Time_greeting():
    Mississippi_tz = pytz.timezone('America/Chicago')
    current_time = datetime.now(Mississippi_tz)
    
    
    if 7 <= current_time.hour < 12:
        print("Purple Phantom: Good morning Kaream!")
    elif 12 <= current_time.hour < 17:
        print("Purple Phantom: Good afternoon Kaream!")
    elif 17 <= current_time.hour < 19:
        print("Purple Phantom: Good evening Kaream!")
    elif 19 <= current_time.hour < 21:
        print("Purple Phantom: It's a bit late Kaream! Have you eaten yet?")
    else:
        print("Purple Phantom: It's getting quite late Kaream! Be sure to eat something before bed.")
        
def Dataset_greeting():
    print(random.choice(greetings))


def Master_greeting():
    master_greetings = ['hey purple', 'wasssup purple', 'how are you purple']
    master_response = input('Kaream: ')
    for greeting in master_greetings:
        if master_response.lower() == greeting:
            print(random.choice(response_greeting))
        break
    else:
        print("Sorry, I didn't understand your input.")
    

# ok the problem here is that Purple phantom is lacking the knowledge to make a decision based on conversation
# and even though I could give hime regulare command I want Purple phantom to make logical desiciones, predictiones, and associationes
# so lets set some data to make Purple-Phantom make a decision based on the conversation and functiones that can do those exact thing


        




# okay the current objective here is logical reasonong in prediction
# and what I mean by this is I want Purple Phantom to predict or do what I request
# and the type of logical understanding that can help him predict what I might want next
# for example: say I was the master and I asked for the time he could make a prediction and ask hey 
# would you like to know what the date is after or would you like to know the weather is
# and here is another example say I said I need to remmember to do somthing and he would ask do you
# want to set a reminder for a secific time  yes or no

# to do this we ware going to use probabilistic logical reasoning with a data set keywords
# to put together with a label upon making a prediction on what function to use for what 
# the master wants purple phantom to do next.


data = {
    'time': ['wonder', 'time', 'how long till', 'what time is it?', 'show me the current time', 'can you get the time'],
    'date': ['when', 'todays date', 'what is todays', 'can you get me the date'],
    'weather': ['what is the', 'weather', 'what does the weather look like', 'show me tomorrows weather'],
    'month': ['what is the month currently', 'can you tell me the month', 'what month is the month right now', 'what month is it', 'what month', 'Month', 'month'],
    'year': ['what year', 'year', 'what is the current year', 'Year'],
    'temperature': ['what is the temp', 'what is the temperature outside', 'what temperature is it', 'how is the temperature', 'what is the current temperature', 'temperature'],
    'location': ['where am I', 'where is', 'what is', 'location', 'Location', 'where is the', 'where is the location of', 'Is the'],
    'news': ['what is the', 'get the latest news', 'show the latest news', 'what is the current news', 'what is the latest news', 'news', 'News'],
    'reminder': ['set a', 'remind me to', 'set', 'set a time', 'set a day', 'set remind for', 'I need to', 'set a', 'remember', 'remind me'],
    'calendar': ['set a time on my calendar', 'add this', 'show me', 'put on', 'calendar', 'Calendar', 'what is', 'when is', 'can you', 'set my'],
    'joke': ['tell me a', 'make a joke', 'say something funny', 'say something', 'joke', 'Joke', 'tell me a joke', 'say a joke'],
    'music': ['play my music', 'play something', 'play the', 'can you', 'play ', 'show me', 'play my', 'what is ', 'Play', 'play some of my tunes'],
    'sports': ['what is the next time Georgia plays', 'what is the', 'Georgia', 'what is the next', 'georgia bulldogs', 'georgia', 'what are th points for georgia bulldogs'],
    'social media': ['check my', 'send a message to', 'show me', 'how many', 'check my messages', 'can you', 'instagram', 'get my'],
    'email': ['send an email', 'can you', 'what is', 'check my', 'send an email to', 'send a', 'send my', 'show my']
}


# okay lets make the Probability algorithm this will get the keywords said in a specifice category in the data set
# and Purple phantom will make a random prediction on a function
# from a list of functions that have been predefined
# such as tell time, show date, tell weather, etc...
def Probability_prediction(data, Master_query):
    time_functions = [Mississippi_time, weather, date, Month, year, get_location, set_reminder, get_calendar]
    date_function = [Mississippi_time, date, Month, year]
    weather_function = [weather, get_location]
    month_function = [Month, set_reminder, get_calendar]
    year_function = [Month, date, year]
    location_function = [get_location, set_reminder, get_calendar]
    news_function = [get_news, set_reminder]
    reminder_function = [set_reminder, get_calendar, date]
    calendar_function = [get_calendar, set_reminder]
    joke_function = [get_joke, get_calendar]
    music_function = [get_music, set_reminder]
    sports_function = [get_sports, set_reminder, get_calendar]
    social_media_function = [get_social_media, set_reminder, get_calendar]
    email_function = [get_email, set_reminder, get_calendar]
    # okay lets make a condition for if the keywords in a category are said then make choose a random function for that category 
    # that can be able to do that request in that certain category
    # once the random function is chosen then Purple phantom will make a prediction asking yes or no would you like me to do that certain request
    Master_query = input('Kaream: ')
    selected_function = None
    for category, keywords in data.items():
        if category == 'time':
            for keyword in keywords:
                if keyword in Master_query:
                    selected_function = random.choice(time_functions)
    if selected_function is not None:
            if selected_function == Mississippi_time:
                print("Purple Phantom: would you like me to show you the current? (y/n)")

                # Corrected this line to take user input
                answer = input()

                if answer.lower() == "yes":
                    selected_function()

                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)

                    if csvfile.tell() == 0:
                        csv_writer.writerow(["Selected Function", "Master Query"])
                        csv_writer.writerow([selected_function.__name__, Master_query])

                if answer.lower() == "no":
                    return AI_Sense()
            if selected_function == weather:
                print("Purple Phantom: would you like me to show you the weather? (y/n)")
                answer = input()
                if answer.lower() == "yes":
                    selected_function()

                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)

                    if csvfile.tell() == 0:
                        csv_writer.writerow(["Selected Function", "Master Query"])
                        csv_writer.writerow([selected_function.__name__, Master_query])

                if answer.lower() == "no":
                    return AI_Sense()
            if selected_function == date:
                print("Purple Phantom: would you like me to show you the date? (y/n)")
                answer = input()
                if answer.lower() == "yes":
                    selected_function()

                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)

                    if csvfile.tell() == 0:
                        csv_writer.writerow(["Selected Function", "Master Query"])
                        csv_writer.writerow([selected_function.__name__, Master_query])

                if answer.lower() == "no":
                    return AI_Sense()
            if selected_function == Month:
                print("Purple Phantom: would you like me to show you the month? (y/n)")
                answer = input()
                if answer.lower() == "yes":
                    selected_function()

                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)

                    if csvfile.tell() == 0:
                        csv_writer.writerow(["Selected Function", "Master Query"])
                        csv_writer.writerow([selected_function.__name__, Master_query])

                if answer.lower() == "no":
                    return AI_Sense()
            if selected_function == year:
                print("Purple Phantom: would you like me to show you the year? (y/n)")
                answer = input()
                if answer.lower() == "yes":
                    selected_function()

                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)

                    if csvfile.tell() == 0:
                        csv_writer.writerow(["Selected Function", "Master Query"])
                        csv_writer.writerow([selected_function.__name__, Master_query])

                if answer.lower() == "no":
                    return AI_Sense()
            if selected_function == get_location:
                print("Purple Phantom: would you like me to show you the location? (y/n)")
                answer = input()
                if answer.lower() == "yes":
                    selected_function()

                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)

                    if csvfile.tell() == 0:
                        csv_writer.writerow(["Selected Function", "Master Query"])
                        csv_writer.writerow([selected_function.__name__, Master_query])

                if answer.lower() == "no":
                    return AI_Sense()
            if selected_function == set_reminder:
                print("Purple Phantom: would you like me to set a reminder? (y/n)")
                answer = input()
                if answer.lower() == "yes":
                    selected_function()

                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)

                    if csvfile.tell() == 0:
                        csv_writer.writerow(["Selected Function", "Master Query"])
                        csv_writer.writerow([selected_function.__name__, Master_query])

                if answer.lower() == "no":
                    return AI_Sense()
            if selected_function == get_calendar:
                print("Purple Phantom: would you like me to show you the calendar? (y/n)")
                answer = input()
                if answer.lower() == "yes":
                    selected_function()

                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)

                    if csvfile.tell() == 0:
                        csv_writer.writerow(["Selected Function", "Master Query"])
                        csv_writer.writerow([selected_function.__name__, Master_query])
                if answer.lower() == "no":
                    return AI_Sense()
    elif 'date' in data['date']:
        for category, keywords in data.items():
            if category == 'date':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(date_function)
                if selected_function is not None:
                    if selected_function == date:
                        print("Purple Phantom: would you like me to show you the date? (y/n)")
                        answer = input()
                        if answer.lower() == "yes":
                            selected_function()

                        with open('Prediction_table.csv', 'a', newline='') as csvfile:
                            csv_writer = csv.writer(csvfile)

                            if csvfile.tell() == 0:
                                csv_writer.writerow(["Selected Function", "Master Query"])
                                csv_writer.writerow([selected_function.__name__, Master_query])

                            if answer.lower() == 'no':
                                return AI_Sense()
    elif 'weather' in data.items():
        for category, keywords in data.items():
            if category == 'weather':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(weather_function)
                    if selected_function is not None:
                        if selected_function == weather:
                            print("Purple Phantom: would you like me to show you the weather? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == 'no':
                                            return AI_Sense()
                        if selected_function == get_location:
                            print("Purple Phantom: would you like me to show you the location? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == 'no':
                                            return AI_Sense()
    elif 'month' in data.items():
        for category, keywords in data.items():
            if category == 'month':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(month_function)
                    if selected_function is not None:
                        if selected_function == Month:
                            print("Purple Phantom: would you like me to show you the month? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == 'no':
                                            return AI_Sense()
                        if selected_function == set_reminder:
                            print("Purple Phantom: would you like me to set a reminder? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == 'no':
                                            return AI_Sense()
                        if selected_function == get_calendar:
                            print("Purple Phantom: would you like me to show you the calendar? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == 'no':
                                            return AI_Sense()
    elif 'year' in data.items():
        for category, keywords in data.items():
            if category == 'year':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(year_function)
                    if selected_function is not None:
                        if selected_function == Month:
                            print("Purple Phantom: would you like me to show you the current Month? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == 'no':
                                            return AI_Sense()
                        if selected_function == date:
                            print("Purple Phantom: would you like me to show you the today's date? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == 'no':
                                            return AI_Sense()
                        if selected_function == year:
                            print("Purple Phantom: would you like me to show you the year? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == 'no':
                                            return AI_Sense()
    elif 'location' in data.items():
        for category, keywords in data.items():
            if category == 'location':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(location_function)
                    if selected_function is not None:
                        if selected_function == get_location:
                            print("Purple Phantom: would you like me to show you the location? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == 'no':
                                            return AI_Sense()
                        if selected_function == set_reminder:
                            print("Purple Phantom: would you like me to set a reminder? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == get_calendar:
                            print("Purple Phantom: would you like me to show you the calendar? (y/n)")
                            answer = input()  
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
    elif 'news' in data.items():
        for category, keywords in data.items():
            if category == 'news':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(news_function)
                    if selected_function is not None:
                        if selected_function == get_news:
                            print("Purple Phantom: would you like me to show you the news? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == set_reminder:
                            print("Purple Phantom: would you like me to set a reminder? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
    elif 'reminder' in data.items():
        for category, keywords in data.items():
            if category =='reminder':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(reminder_function)
                    if selected_function is not None:
                        if selected_function == get_reminder:
                            print("Purple Phantom: would you like me to show you the reminder? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == get_calendar:
                            print("Purple Phantom: would you like me to show you the calendar? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
    elif 'calendar' in data.items():
        for category, keywords in data.items():
            if category == 'calendar':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(calendar_function)
                    if selected_function is not None:
                        if selected_function == get_calendar:
                            print("Purple Phantom: would you like me to show you the calendar? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == set_reminder:
                            print("Purple Phantom: would you like me to set a reminder? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
    elif 'joke' in data.items:
        for category, keywords in data.items():
            if category == 'joke':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(joke_function)
                    if selected_function is not None:
                        if selected_function == get_joke:
                            print("Purple Phantom: would you like me to show you a joke? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == get_calendar:
                            print("Purple Phantom: would you like me to show you the calendar? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
    elif 'music' in data.items():
        for category, keywords in data.items():
            if category == 'music':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(music_function)
                    if selected_function is not None:
                        if selected_function == get_music:
                            print("Purple Phantom: would you like me to manage you'r music? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return False
                        if selected_function == set_reminder:
                            print("Purple Phantom: would you like me to set a reminder? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
    elif 'sports' in data.items():
        for category, keywords in data.items():
            if category == 'sports':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(sports_function)
                    if selected_function is not None:
                        if selected_function == get_sports:
                            print("Purple Phantom: would you like me to show you some info for sports? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == set_reminder:
                            print("Purple Phantom: would you like me to set a reminder? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == get_calendar:
                            print("Purple Phantom: would you like me to manage calendar? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
    elif 'social media' in data.items():
        for category, keywords in data.items():
            if category == 'social media':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(social_media_function)
                    if selected_function is not None:
                        if selected_function == get_social_media:
                            print("Purple Phantom: would you like me to do something with you'r social media? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == set_reminder:
                            print("Purple Phantom: would you like me to set a reminder? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == get_calendar:
                            print("Purple Phantom: would you like me to manage calendar? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
    elif 'email' in data.items():
        for category, keywords in data.items():
            if category == 'email':
                for keyword in keywords:
                    if keyword in Master_query:
                        selected_function = random.choice(email_function)
                    if selected_function is not None:
                        if selected_function == get_email:
                            print("Purple Phantom: would you like me to do something with you'r email? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == set_reminder:
                            print("Purple Phantom: would you like me to set a reminder? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        if selected_function == get_calendar:
                            print("Purple Phantom: would you like me to manage calendar? (y/n)")
                            answer = input()
                            if answer.lower() == "yes":
                                selected_function()
                                with open('Prediction_table.csv', 'a', newline='') as csvfile:
                                    csv_writer = csv.writer(csvfile)
                                    if csvfile.tell() == 0:
                                        csv_writer.writerow(["Selected Function", "Master Query"])
                                        csv_writer.writerow([selected_function.__name__, Master_query])
                                        if answer.lower() == "no":
                                            return AI_Sense()
                        

# lets make a Machine learning algorithm while making Purple Phantoms features

# lets start with the algorithm Mississippi time and I will explain the goal of the funtion

def Mississippi_time():
    # I will make a algorithm that can not only tell Mississippi time
    # but when its day light savings time so the time is always correct
    # when Purple phantom tells the time Purple phantom will also states only on the days when
    # daylight savings has started and has ended when telling the time in Mississippi
    # he not only does that but logs the date that daylight savings had started and ended into a file
    # so lets first put the code to show Mississippi's time in mississippi
    # and the code to show the daylight savings time in mississippi when actually daylight savings starts or ends
    Mississippi_TZ = pytz.timezone('America/Mississippi')
    Mississippi_CurrTM = datetime.now(Mississippi_TZ)
    dst_offset = Mississippi_TZ.utcoffset(Mississippi_CurrTM)
    is_dst = dst_offset != timedelta(0)
    Mississippi_time_str_dst = Mississippi_CurrTM.strftime('%I:%M %p')
    Mississippi_time_str_non_dst = Mississippi_CurrTM.strftime('%I:%M %p')
    start_time = end_time = datetime(Mississippi_CurrTM.year, 1, 1, tzinfo=Mississippi_TZ)
    # let add the start rules for saving the date for daylight saving and then end rules as well and use different a different module
    transitions = []
    for year in range(Mississippi_CurrTM.year - 1, Mississippi_CurrTM.year + 1):
        start = datetime(year, 1, 1, tzinfo=Mississippi_TZ)
        end = datetime(year + 1, 1, 1, tzinfo=Mississippi_TZ)
        transitions.append((start, end))

    for start, end in transitions:
        if start < Mississippi_CurrTM < end:
            start_time = start
            end_time = end
            break

    # lets add a condition for if it is daylight savings time then show the time as daylight saving time and also if 
    # it is the the day that day light savings began or ended the Putple phantom will say that day light savings time has began or ended
    if is_dst:
            print(f"Purple Phantom: It is currently day light savings time and the current time is {Mississippi_time_str_dst}")
    else:
            print(f"Purple Phantom: It is not currently day light savings and the current time is {Mississippi_time_str_non_dst}")
    # lets add in something to store into a file the date when daylight savings started and what date daylight savings ended
    with open('Dst_Date', 'a') as file:
        file.write(f"Daylight savings started on: {start_time.strftime('%m/%d/%Y')} and ended on: {end_time.strftime('%m/%d/%Y')}")


# lets create the next feature which is date now I will explain the main goal of this Machine learning Algorithm inside the function

def date():
    # in this Machine learning algorithm Purple phantom will not only be telling me todays date
    # but know what holiday it is and what my age is currently by the date I was born and can calculate if it is my birthday and what age im turning
    # also what I said about the holiday thing sense I know I wont be interacting with him all the time
    # I will add in something for him to say for if it is a holiday and if its a good couple of weeks past any holiday
    
    # lets add a list of dates for every holiday using the month number and the day
    # and then we can use those numbers to find out which holiday it is
    # or maybe even better just have a list of holidays and their corresponding months
    # and then check if today falls within any of them
    holiday = {
        'New Years' : ['01/1'],
        'Valentines Day':['02/14'],
        'Presidents Day':['02/15'],
        'St Patricks Day':['03/17'],
        'Easter Sunday':['04/18'],
        'Good Friday':['04/19'],
        'Memorial Day':['05/30'],
        'Independence Day':['07/04'],
        'Labor Day':['09/06'],
        'Columbus Day':['10/02'],
        'Veterans Day':['11/11'],
        'Thanksgiving Day':['11/22'],
        'Christmas Day':['12/25']
    }
    formatted_date = datetime.now()
    Todays_date = formatted_date.strftime("%m/%d/%Y")
    Masters_birth_date = '04/12/2006'
    current_year = int(formatted_date.strftime("%Y"))
    current_month = int(formatted_date.strftime("%m"))
    current_day = int(formatted_date.strftime("%d"))
    birth_year = 2006
    birth_month = 4
    birth_day = 12
    age = (current_year - birth_year) * 365 + ((current_month-birth_month)*30 + (current_day-birth_day))
    # lets add a condition for it is a holiday then Purple Phantom will say Happy and that holiday
    # and if the holiday has just past then Purple Phantom says Happy late and that holiday
    # and if it is not a holiday then Purple will just print the date
    for holidays, dates in holiday.items():
        if str(Todays_date) == dates[0]:
            print(f"Purple Phantom: Happy {holidays} Kaream!, todays date is {Todays_date}")
        if str(Todays_date) >= dates[0]:
            print(f"Purple Phantom: Happy late {holidays} Kaream!, todays date is {Todays_date}")
        else:
            print(f"Purple Phantom: Today's date is {Todays_date}")
    # now lets add a conditione for if the current date is the masters birthday or not
    if str(Masters_birth_date) == Todays_date:
        print(f"Purple Phantom: Happy Birthday Kaream!, you are now {age} years old congrates!! :)")
        with open('Kareams_birthday.txt', 'a') as file:
            file.write(f"Purple Phantom: Today was Kareams {age} birthday YAY!!")
    if str(Masters_birth_date) >= Todays_date:
        print(f"Purple Phantom: Happy late Birthday Kaream!, you are now {age} years old congrates!! :)")
    else:
        return None
    

# lets add in the next feature and I will explain how this ML algorithm works 
def weather():
    """
    This function does use api unfortunately
    It doesnt actualy use machine learning because I dont know much about getting the weather
    but I can make it request it from a site and print weather for the current day of the week
    and get the temparture, the type of weather for example rainy, fogy, or cloudy, and thats it
    """
    import datetime
   # Your API key
    api_key = '9893a18f5e152d21b63e35c756ab429a'
    
    # Your desired location
    location = 'Jackson, US'
    
    # Fetch the weather data
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}')
    data = response.json()
    
    # Extract the necessary information
    main_weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15 # Convert from Kelvin to Celsius
    temperature = (temperature * 9/5) + 32 # Convert from Celsius to Fahrenheit
    wind_speed = data['wind']['speed']
    cloud_coverage = data['clouds']['all']
    precipitation = data['rain']['3h'] if 'rain' in data else 0 # Assume no precipitation if there is no rain data
    sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
    
    # Create a function to get the day of the week
    day_of_week = datetime.datetime.now().strftime('%A')
    
    print(f"Purple Phantom: The day of the week is {day_of_week}\nTemperature outside is {temperature:.2f}°F\nWeather Conditions: {main_weather} - {description}\nWind Speed: {wind_speed} m/s\nCloud Coverage: {cloud_coverage}%\nPrecipitation: {precipitation} mm\nSunrise: {sunrise}\nSunset: {sunset}")   
    

# lets make the next function which is showing the current month I will explain all about this function later
def Month():
    """
    This function shows what month we are currently in
    I dont know really how to make it Machine learning so it just going to exactly what its supposed to
    do which is show me what month im in right now
    """
    today = date.today()
    if today.month == 1:
        return "January"
    elif today.month == 2:
        return "February"
    elif today.month == 3:
        return "March"
    elif today.month == 4:
        return "April"
    elif today.month == 5:
        return "May"
    elif today.month == 6:
        return "June"
    elif today.month == 7:
        return "July"
    elif today.month == 8:
        return "August"
    elif today.month == 9:
        return "September"
    elif today.month == 10:
        return "October"
    elif today.month == 11:
        return "November"
    else:
        return "December"
    


# lets add in the next feature which is year I will explain the main goal of this function later
def year():
    """
    This function shows what year we are currently in
    I dont know really how to make it Machine learning so it just going to exactly what its
    supposed to do
    which is show me what year im in right now
    """
    today = date.today()
    return today.year


# lets add in a Machine learning algorithm for news I will explain the main goal of this function later
def get_news():
    """
    This function uses an api from gnews.io to get any news
    that is requested to be seen, so the main goal of this function is to get any news 
    that is requested to be seen and show the title or headline links to them and also save the
    type of news requested into a .csv file with a data set inside of it, for personalization
    purposes.
    """
    # first we need to import all the necessary modules
    # then we define our variables
    API_KEY = 'your-api-key'
    SEARCH_TERM = input("Enter your search term : ")
    RESULTS_NUMBER = int(input('How many results you want? :'))
    URL = f'https://gnews.io/api/v3/search?token={API_KEY}&category=general&language=en&query={SEARCH_TERM}&size={RESULTS_NUMBER}'
    NEWS_TYPE = input("What kind of news do you want (Business/Science/Health) ?")
    # lets make conditions for every possible selection
    if NEWS_TYPE == "Business":
        CATEGORY = "business"
        # lets have Purple phantom print out all of the results for the title and description
        response = rq.get(f"https://gnews.io/api/v3/search?lang=en&category={CATEGORY}&token={API_KEY}")
        # now lets print out Purple phantoms response
        print("\n\nPurple Phantom News Results:\n")
        j = json.loads(response.text)
        i = 0
        while i < min(RESULTS_NUMBER, len(j['results'])):
            print(f"\nTitle: {j['results'][i]['title']}\nDescription:{j['results'][i]['description']}\nURL: {j['results'][i]['url']}\n\n")
            # lets add in something to save the categroy and all the information printed into a csv file in a data set
            with open('News Data.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                # lets have it written in a data set fromat
                writer.writerow([j['results'][i]['title'], j['results'][i]['description']])
                # lets do the other selections
    elif NEWS_TYPE == "Science":
        CATEGORY = "science"
        # lets have Purple phantom print out all of the results for the title and description for the science category
        response = rq.get(f"https://gnews.io/api/v3/search?lang=en&category={CATEGORY}&token={API_KEY}")
        # lets Print Purples response
        print("\n\nPurple Phantom News Results:\n")
        j = json.loads(response.text)
        i = 0
        while i < min(RESULTS_NUMBER, len(j['results'])):
            print(f"\nTitle: {j['results'][i]['title']}\nDescription:{j['results'][i]['description']}\nURL: {j['results'][i]['url']}\n\n")
            # lets add in something to save the categroy and all the information printed into a csv file in a data set
            with open('News Data.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                # lets have it written in a data set fromat
                writer.writerow([j['results'][i]['title'], j['results'][i]['description']])
    elif NEWS_TYPE == "Health":
        CATEGORY = "health"
        response = rq.get(f"https://gnews.io/api/v3/search?lang=en&category={CATEGORY}&token={API_KEY}")
        #lets Print Purple Phantoms response
        print("\n\nPurple Phantoms News Results:\n")
        j = json.loads(response.text)
        i = 0
        while i < min(RESULTS_NUMBER, len(j['results'])):
            print(f"\nTitle: {j['results'][i]['title']}\nDescription:{j['results'][i]['description']}\nURL: {j['results'][i]['url']}\n\n")
            # lets add in something to save the categroy and all the information printed into a csv file in a data set
            with open('News Data.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                # lets have it written in a data set fromat
                writer.writerow([j['results'][i]['title'], j['results'][i]['description']])
        else:
            print("Invalid Input! Please enter either Business, Science or Health.")
            

# lets creat a function called AI sense I will explain the main goal of this function later
def AI_Sense():
    """
    This Function is designed to take read the csv called Prediction_table.csv when the answer is no 
    and then use that type of information to open two csv files and take the keywords and the function name
    from the prediction_table.csv file and put them into the first csv file called percentage_prediction
    The percentage prediction file will be constantly be updating the percentage next to the keyword and function and be used to put a percentage of how many times a specific keyword and function
    has been correctly predicted and stored in the prediction_table.csv file in the data set, the more a certain keyword
    and function have been read and found in the Prediction_table.csv file the higher percentage predicted for the function
    to be selected when that keyword is said so if the prediction is wrong when selecting the function and the answer is no then the csv file
    and then compare those percentage numbers for what specifice keyword was used and select the most used function for that,
    and then Purple Phantom will ask another question for the higher percentage.
    The seconed csv file will be called Possibility percentage.csv this file will constantly take all the words said and the function correctly predicted functions
    and store them into the file with a percentage that keep updating every minute and the more a certain word is said in the sentence with the function that is correctly predicted
    The algorithm will open a third file to store keywords into a key/value pair type of dataset with the higer percentage into a csv file called High percentage keywords
    the key will be the individual word used the most the value is the high percentage given, so if the answer is no the more accurate prediction can be made by Purple phantom
    I will explain step by step on how this works in the Machine learning algorithm
    """
    # lets first read the csv file called Prediction_table.csv
    pred_data = pd.read_csv("Prediction_Table.csv", header=None).values.tolist()
    # now we need to calculate the percentage for the most correct prediction found
    percent_correct = (pred_data.count(1)/len(pred_data))
    # Now lets open the Prediction Percentage.csv file
    with open ("Percentage_Prediction.csv","w+") as perc_file:
    # Lets Make a condition for only copying the keywords and function into the file with the highest Percentage
        writer = csv.writer(perc_file)
    # Lets write the keyword and function into the file with the highest Percentage
        writer.writerow(['Keyword','Function Name','Correctness'])
    # Lets add the percentage value to the same row as the Keyword and Function Name
        writer.writerows([x[:2]+[percent_correct]for x in zip(*[iter(lambda : list(x), None)]*3)])
    # lets add a condition for the reading the keyword in a certain category in the csv file to ask the correct question
    with open("Percentage_Prediction.csv", 'r') as perc_file:
        lines = perc_file.readlines()
    for category, keywords in data.items():
        for keyword in keywords:
            if any(keyword in line for line in lines) == category:
                if category == 'time':
                    print("Purple Phantom: Would you like me to show you the current time (y/n)?")
                    answer = input()
                    if answer.lower() == "yes":
                        Mississippi_time()
                    if answer.lower() == "no":
                        Backup_prediction()
                    elif category == 'date':
                        print("Purple Phantom: Would you like me to show you the todays date (y/n)?")
                        if answer.lower() == "yes":
                            date()
                        if answer.lower() == "no":
                            Backup_prediction()
                    elif category == 'weather':
                        print("Purple Phantom: Would you like me to show you the weather outside (y/n)?")
                        if answer.lower() == "yes":
                            Weather()
                        if answer.lower() == "no":
                            Backup_prediction()
                    elif category == 'month':
                        print("Purple Phantom: Would you like me to show you the current month (y/n)?")
                        if answer.lower() == "yes":
                            Month()
                        if answer.lower() == "no":
                            Backup_prediction()
                    elif category == 'year':
                        print("Purple Phantom: Would you like me to show you the year (y/n)?")
                        if answer.lower() == "yes":
                            year()
                        if answer.lower() == "no":
                            Backup_prediction()
                    elif category == 'temparture':
                        print("Purple Phantom: Would you like me to show you the temparture outside (y/n)?")
                        if answer.lower() == "yes":
                            weather()
                        if answer.lower() == "no":
                            Backup_prediction()
                    elif category == 'location':
                        print("Purple Phantom: Would you like me to find a specific location (y/n)?")
                        if answer.lower() == "yes":
                            get_location()
                        if answer.lower() == "no":
                            Backup_prediction()
                    elif category == 'news':
                        print("Purple Phantom: Would you like me to show you the news (y/n)?")
                        if answer.lower() == "yes":
                            News()
                        if answer.lower() == "no":
                            Backup_prediction()
                    elif category == 'reminder':
                        print("Purple Phantom: Would you like me to show you or set a reminder (y/n)?")
                        if answer.lower() == "yes":
                            set_reminder()
                        if answer.lower() == 'no':
                            Backup_prediction()
                    elif category == 'calendar':
                        print("Purple Phantom: Would you like me to show you or set your calendar (y/n)?")
                        if answer.lower() == 'yes':
                            get_calendar()
                        if answer.lower() == 'no':
                            Backup_prediction()
                    elif category == 'joke':
                        print("Purple Phantom: Would you like me to tell you a joke (y/n)?")
                        if answer.lower() == 'yes':
                            get_joke()
                        if answer.lower() == 'no':
                            Backup_prediction()
                    elif category == 'sports':
                        print("Purple Phantom: Would you like me to show you some information on Georgia (y/n)?")
                        if answer.lower() == 'yes':
                            get_sports()
                        if answer.lower() == 'no':
                            Backup_prediction()
                    elif category == 'music':
                        print("Purple Phantom: Would you like me to play some tunes (y/n)?")
                        if answer.lower() == 'yes':
                            get_music()
                        if answer.lower() == 'no':
                            Backup_prediction()
                    elif category == 'email':
                        print("Purple Phantom: Would you like me to send an email (y/n)?")
                        if answer.lower() == 'yes':
                            
                    
                        
                    
                


    
