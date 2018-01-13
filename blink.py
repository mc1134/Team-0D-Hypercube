#!/usr/bin/python
import time
import subprocess

from gpio_96boards import GPIO

GPIO_A = GPIO.gpio_id('GPIO_A')
GPIO_B = GPIO.gpio_id('GPIO_B')
GPIO_C = GPIO.gpio_id ('GPIO_C')
pins = (
    (GPIO_A, 'out'),
    (GPIO_B, 'in'),
    (GPIO_C, 'in')
)

def blink(gpio):
    for i in range(5):
        gpio.digital_write(GPIO_A, GPIO.HIGH)
        print ("readGPIO_A = ", gpio.digital_read(GPIO_A))

        time.sleep(i)
        gpio.digital_write(GPIO_A, GPIO.LOW)
        time.sleep(1)

def switch(gpio):
    gpio.digital_write(GPIO_A, GPIO.LOW)
    #for i in range(0,100):
    while True:    
        #print ("readGPIO_A = ", gpio.digital_read(GPIO_A))
        #print ("readGPIO_C = ", gpio.digital_read(GPIO_C))
        #print (" ")
        if gpio.digital_read(GPIO_C) == GPIO.HIGH:
            gpio.digital_write(GPIO_A, GPIO.HIGH)
            subprocess.call("./recordScript.sh")
            #time.sleep(4)
            subprocess.call("./wavSorter.sh")
        else:
            gpio.digital_write(GPIO_A, GPIO.LOW)
            #time.sleep(1)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Blink LED on GPIO A (pin 23)')
    args = parser.parse_args()

    with GPIO(pins) as gpio:
        switch(gpio)
