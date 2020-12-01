#choice randomy returns an element in a list.
from random import choice

#get date
from datetime import date
today = date.today()
date = today.strftime("%B %d, %Y")

#get time
from datetime import datetime
now = datetime.now()
time = now.strftime("%H:%M")

#combine functions and conditionals to get a response from the bot

def get_bot_response(user_response):

    #bot responses
    bot_response_happy = ["Good :)", "Excellent!", "What makes you so happy?"]
    bot_response_sad = ["Oh no :(", "What is making you so upset?", "Would you like to listen to some music?"]

    if user_response == "what day is it":
        return date
    elif user_response == "what time is it":
        return time
    elif user_response == "I am feeling happy":
        return choice(bot_response_happy)
    elif user_response == "I am feeling sad":
        return choice(bot_response_sad)
    else: 
        return "thats wasup"
        pass
        

print("Hello my name is Siri.")
print("Whats your name?")
user_response = input("")
name = user_response
print(f"Hello {name}")
user_response = ""

while user_response != "bye":
    user_response = input("What can I help you with today?")

    if user_response == "bye":
        break

    bot_response = get_bot_response(user_response)
    print(bot_response)