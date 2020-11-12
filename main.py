# Raspberry Pi Project
from grove.factory import Factory

run = True
pin = 12
button = Factory.getButton("GPIO-HIGH", pin)

while run:
    if button.is_pressed():
        print('Button is pressed')
    else:
        print('Button is released')
