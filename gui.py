
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import sys


OUTPUT_PATH = Path(__file__).parent
def get_base_path():
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)  / "assets" / "frame0"
    return Path(__file__).parent  / "assets" / "frame0"

ASSETS_PATH = get_base_path()



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x600")
window.configure(bg = "#FFFFFF")

#### DHT11

#hi
#idk_what_this_does
#am_lost (from ben)

from gpiozero import OutputDevice, InputDevice, Factory
import time


##########
#pseudorandom normal change
import random as rnd
import time
import math

def NoRan(OldVal,Temperature,TimeDifference=0):
    OldVal2 = OldVal+0.25
    Temperature2=(rnd.randint(-Temperature*1000,Temperature*1000)/1000+0.00001)
    NewValue = OldVal2+(OldVal2*Temperature2)*TimeDifference
    print(OldVal2," -> x -> ",NewValue)
    return NewValue, time.time

timestamp = time.time
oldvalue=0
for i in range(100):
    oldvalue,timestamp = NoRan(oldvalue,2,time.time()-timestamp())
########


print("0")

class DHT11():
    MAX_DELAY_COUNT = 100
    BIT_1_DELAY_COUNT = 10
    BITS_LEN = 40

    def __init__(self, pin, pull_up=False):
        self._pin = pin
        self._pull_up = pull_up
    print("1")


    def read_data(self):
        timestamp = time.time
        bit_count = 0
        delay_count = 0
        bits = ""

        # -------------- send start --------------
        gpio = OutputDevice(self._pin)
        gpio.off()

        gpio.close()
        gpio = InputDevice(self._pin, pull_up=self._pull_up)
        
        print("2")
        # -------------- wait response --------------
        while not (gpio.value == 1 or gpio.value == 0):
            print("2.1 ",gpio.value)
            #pass
        print("2.2")
        # -------------- read data --------------
        while bit_count < self.BITS_LEN:
            print("2.3")
            while gpio.value == 0:
                print("2.4")
                time.sleep(0.001)

            # st = time.time()
            while gpio.value == 1:
                #print("2.5")
                delay_count += 1
                time.sleep(0.001)
                if delay_count > self.MAX_DELAY_COUNT:
                    break
            if delay_count > self.BIT_1_DELAY_COUNT:
                bits += "1"
            else:
                bits += "0"
        
            print(f"3 {delay_count},{bit_count}")

            delay_count = 0
            bit_count += 1

        # -------------- verify --------------
        humidity_integer = int(bits[0:8], 2)
        humidity_decimal = int(bits[8:16], 2)
        temperature_integer = int(bits[16:24], 2)
        temperature_decimal = int(bits[24:32], 2)
        check_sum = int(bits[32:40], 2)

        _sum = humidity_integer + humidity_decimal + temperature_integer + temperature_decimal

        # print(bits)
        # print(humidity_integer, humidity_decimal, temperature_integer, temperature_decimal)
        # print(f'sum:{_sum}, check_sum:{check_sum}')
        # print()

        if check_sum != _sum:
            humidity,timestamp = NoRan(oldvalue,2,time.time()-timestamp())
            temperature = 0.0
        else:
            humidity = float(f'{humidity_integer}.{humidity_decimal}')
            temperature = float(f'{temperature_integer}.{temperature_decimal}')

        # -------------- return --------------
        print("4")
        return humidity, temperature

#........................ . ............. .... 

dht11 = DHT11(4)
while True:
    humidity, temperature = dht11.read_data()
    print(f"{time.time():.3f}  temperature:{temperature}°C  humidity: {math.clamp(abs(humidity),0,100)}%")
    time.sleep(1)


#### DHT11 end


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    512.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    517.0,
    224.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    516.0,
    110.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    160.0,
    431.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=71.0,
    y=332.0,
    width=178.0,
    height=196.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    526.0,
    431.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=437.0,
    y=332.0,
    width=178.0,
    height=196.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    892.0,
    431.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=803.0,
    y=332.0,
    width=178.0,
    height=196.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=dht11.read_data,
    relief="flat"
)
button_1.place(
    x=813.0,
    y=21.0,
    width=190.0,
    height=73.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    343.0,
    445.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    708.0,
    445.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()
