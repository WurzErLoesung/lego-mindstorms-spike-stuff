from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
import stuff.function

def main():
    hub = PrimeHub()
    while True:
        hub.light_matrix.show_image('HAPPY')
        wait_for_seconds(5)
        hub.light_matrix.show_image('SAD')
        wait_for_seconds(5)