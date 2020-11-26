# Raspberry Pi Project
from grovepi import *
from grove_rgb_lcd import *
import random
import time
import getNews
import pyttsx3

engine = pyttsx3.init()
run = True
button_read = 3
button_real = 6
button_fake = 5

try:
    highscore_file = open("highscore.txt", "r")
    highscore = highscore_file.read()
    highscore_file.close()
except:
    highscore_file = open("highscore.txt", "x")
    highscore = 0
    highscore_file.close()



score = 0

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 120)     # setting up new voice rate

if(highscore == ""):
    highscore = 0

congrats = "Congratulations you were right!"
too_bad = "Too bad, you were wrong!"


def newsselector():
    selected_news = random.randint(0, 1)
    if(selected_news == 0):
        news_to_be_read = getNews.getNewsHeadline()
        real_or_fake = "real"
    else:
        news_to_be_read = getNews.getFakeNewsHeadline()
        real_or_fake = "fake"

    return news_to_be_read, real_or_fake


selected_news, real_or_fake = newsselector()


def changeHighscore(score, highscore):
    if(int(score) > int(highscore)):
        highscore_file = open("highscore.txt", "w")
        highscore_file.write(str(score))
        highscore = score
        highscore_file.close()
    return highscore


print("The Fake or Real Game is running")
setText("Score: " + str(score) + "\n" + "Highscore: " + str(highscore))

while run:
    print("i am still running")
    while (digitalRead(button_read) or digitalRead(button_fake) or digitalRead(button_real)):
        # print("I am inside")
        # print(score)
        setText("Score: " + str(score) + "\n" + "Highscore: " + str(highscore))
        if(digitalRead(button_read)):
            time.sleep(0.1)
            print("the news will be read")
            engine.say(selected_news)
            engine.runAndWait()
            time.sleep(0.5)

        if(digitalRead(button_real)):
            time.sleep(0.1)
            print("You pressed real")
            if(real_or_fake == "real"):
                score += 1
                engine.say(congrats)
                engine.runAndWait()

            else:
                highscore = changeHighscore(score, highscore)
                score = 0
                engine.say(too_bad)
                engine.runAndWait()
            selected_news, real_or_fake = newsselector()
            time.sleep(0.5)

        if(digitalRead(button_fake)):
            time.sleep(0.1)
            print("You pressed fake")
            if(real_or_fake == "fake"):
                score += 1
                engine.say(congrats)
                engine.runAndWait()

            else:
                highscore = changeHighscore(int(score), int(highscore))
                score = 0
                engine.say(too_bad)
                engine.runAndWait()
            selected_news, real_or_fake = newsselector()
            time.sleep(0.5)
        setText("Score: " + str(score) + "\n" + "Highscore: " + str(highscore))
