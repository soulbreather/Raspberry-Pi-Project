# Raspberry Pi Project
from grovepi import *
import time
import getNews
import pyttsx3

engine = pyttsx3.init()
run = True
button1 = 3
button2 = 6
realNews = getNews.getNewsHeadline()
fakeNews = getNews.getFakeNewsHeadline()

print(realNews)
print(fakeNews)

print("fake or not game is running")

while True:
    if(digitalRead(button1)):
        time.sleep(0.1)
        print("button 1 was pressed")
        engine.say(realNews)
        engine.runAndWait()

    if(digitalRead(button2)):
        time.sleep(0.1)
        print("button 2 was pressed")
        engine.say(fakeNews)
        engine.runAndWait()
