from sense_hat import SenseHat
from random import randint
from random import choice 
from time import sleep
sense = SenseHat()
x = 4
y = 1
sense.show_message("Ask a question", scroll_speed=0.06)
sleep(3)

replies = ['Signs point to yes',
           'Without a doubt',
           'Do not count on it',
           'looking good',
           'cannot predict now',
           'It is decidendly so',
           'Outlook not so good'
           ]

def show_sparkel():
    while True:
        x= randint(0, 7)
        y= randint(0, 7)
        r = randint(0, 255)
        b = randint(0, 255)
        g = randint(0, 255)
        sense.set_pixel(x, y, r, g, b)

while True:
    x, y, z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)
    if x > 1.5 or y > 1.5 or z > 1.5:
        sense.show_message(choice(replies),0.0625)
        if replies == 'signs point to yes' or 'Without a doubt' or 'looking good' or 'It is decidendly so':
            show_sparkel()
        else:
            sense.clear()
        
        


        
        


