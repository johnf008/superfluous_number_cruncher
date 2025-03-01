import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup.setup(7, GPIO.OUT)

for i in range(50):
    GPIO.output(7,True)
    time.sleep(1)
    GPIO.output(7, False)
    time.sleep(1)
    

GPIO.cleanup() #prevents unusual behavior

