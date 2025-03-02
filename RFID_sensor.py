import RPi.GPIO as GPIO
import MFRC522
import signal 

continue_reading = True

#cleans everything up when aborted
def end_read(signal,frame):
    global continue_reading
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522

while continue_reading:

    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
#john note: i'm way too tired to do this and i need to finish the gui components
# i linked a resource in the idea board to assist us with this part,
#it's pretty straight forward