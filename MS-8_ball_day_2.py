from sense_hat import SenseHat
from random import choice
from time import sleep
x = 4
y = 1
red = (255, 0, 0)
purple = (255, 0, 255)
blue =
sense = SenseHat()
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
while True:
    x, y, z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)
    if x > 1.5 or y > 1.5 or z > 1.5




    :
        sense.show_message(choice(replies))
    else:
        sense.clear()

    




