# Raspberry Pi Project
from grovepi import *
import time
import getNews

engine = pyttsx3.init()
run = True
button = 3


while True:
    if(digitalRead(button)):
        time.sleep(0.1)
        print("button was pressed")
        engine.say(getNews)
        engine.runAndWait()
