# Raspberry Pi Project
from grovepi import *
import random
import time
import getNews
import pyttsx3

engine = pyttsx3.init()
run = True
button_read = 3
button_real = 6
button_fake = 5

congrats = "Congratulations you were right!"
too_bad = "Too bad, you were wrong!"


def newsselector():
    selected_news = random.randint(0,1)
    if(selected_news == 0):
        news_to_be_read = getNews.getNewsHeadline()
        real_or_fake = "real"
    else:
        news_to_be_read = getNews.getFakeNewsHeadline()
        real_or_fake = "fake"

    return news_to_be_read, real_or_fake

selected_news, real_or_fake = newsselector()

print("The Fake or Real Game is running")

while True:
    if(digitalRead(button_read)):
        time.sleep(0.1)
        print("the news will be read")
        engine.say(selected_news)
        engine.runAndWait()
        

    if(digitalRead(button_real)):
        time.sleep(0.1)
        print("You pressed real")
        if(real_or_fake == "real"):
            engine.say(congrats)
            engine.runAndWait()
        else:
            engine.say(too_bad)
            engine.runAndWait()
        selected_news, real_or_fake = newsselector()

    if(digitalRead(button_fake)):
        time.sleep(0.1)
        print("You pressed fake")
        if(real_or_fake == "fake"):
            engine.say(congrats)
            engine.runAndWait()
        else:
            engine.say(too_bad)
            engine.runAndWait()
        selected_news, real_or_fake = newsselector()
