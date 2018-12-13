from sense_hat import SenseHat
from random import *
from time import sleep
sense = SenseHat()
x = 4
y = 1
r = (255, 0, 0)
p = (255, 0, 255)
b = (0, 0, 255)
o = (255, 200, 0)
ye = (255, 255, 0)
g = (0, 255, 0)

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
    global x
    x= random.randint(0, 8)
    y= random.randint(0, 8)
    print (x)
    print (y) 

while True:
    x, y, z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)
    if x > 1.5 or y > 1.5 or z > 1.5:
        sense.show_message(choice(replies))
    if replies == 'signs point to yes' or 'Without a doubt' or 'looking good' or 'It is decidendly so':
        show_sparkel
    else:
        sense.clear()
    
    


    
    


