from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until
from spike.control import Timer as SpikeTimer
from spike.operator import *
from math import *
import uasyncio as asyncios

# INITIALIZATION
hub = PrimeHub()
MotionSensor = hub.motion_sensor
MotionSensor.reset_yaw_angle()
drive = MotorPair('B', 'F')
ColorLeft = ColorSensor('E')
ColorRight = ColorSensor('A')
ColorBack = ColorSensor('D')

# TV
drive.set_default_speed(35)
drive.move(55)
drive.move(-15)

# Windmill
drive.move(5, steering=100)
drive.move(42)
drive.set_default_speed(45)

drive.start(-100, 10)
wait_until(MotionSensor.get_yaw_angle, equal_to, 50)
drive.stop()
wait_for_seconds(0.5)
drive.set_default_speed(40)
drive.move(45)