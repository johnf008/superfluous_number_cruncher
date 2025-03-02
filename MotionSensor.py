import RPi.GPIO as GPIO
import time
import threading
from gpiozero import MotionSensor
from signal import pause 

pir = MotionSensor(12)  #I think this defines the sensor
#figure out how to 



def motion_function():
    print("Motion Detected")  #this will most likely set the screen to true

def no_motion_function():
    print("No Motion detected")  #turn everything off

pir.when_motion = motion_function
pir.when_no_motion = no_motion_function
while True:
	pir.wait_for_motion()
	print("You moved")
	pir.wait_for_no_motion()

pause()