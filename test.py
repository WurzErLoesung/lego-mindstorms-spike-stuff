from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

def wtf(buffer):
    fs = ForceSensor('A')
    with open('read_all.txt', 'r') as f:
        c = 'a'
        while c:
            c = f.read(buffer).encode()
            print(c)
            fs.wait_until_pressed()
            fs.wait_until_released()
            print('\n\n\n')

wtf()