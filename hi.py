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

if __name__ == '__main__':
    dht11 = DHT11(4)
    while True:
        humidity, temperature = dht11.read_data()
        print(f"{time.time():.3f}  temperature:{temperature}°C  humidity: {math.clamp(abs(humidity),0,100)}%")
        time.sleep(1)
