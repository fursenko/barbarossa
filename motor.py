from gpiozero import Motor
from time import sleep

left = Motor(17, 18)
right  = Motor(4, 14)

while True:
    for i in range(0, 6):
        left.forward(i*0.1)
        right.forward(i*0.1)
        sleep(0.4)
        
    for i in range(0, 6):
        left.forward((6 - i) * 0.1)
        right.forward((6 - i) * 0.1)
        sleep(0.4)
        
    for i in range(0, 6):
        left.backward(i*0.1)
        right.backward(i*0.1)
        sleep(0.4)
        
    for i in range(0, 6):
        left.backward((6 - i) * 0.1)
        right.backward((6 - i) * 0.1)
        sleep(0.4)