#!/usr/bin/python
import time
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io.wavfile import read
from sklearn.preprocessing import normalize
from math import floor

from gpio_96boards import GPIO

GPIO_A = GPIO.gpio_id('GPIO_A')
#GPIO_B = GPIO.gpio_id('GPIO_B')
GPIO_C = GPIO.gpio_id ('GPIO_C')
GPIO_E = GPIO.gpio_id ('GPIO_E') # corr tiltPin
GPIO_G = GPIO.gpio_id ('GPIO_G') # corr tiltDirPin

pins = (
    (GPIO_A, 'out'),
    #(GPIO_B, 'in'),
    (GPIO_C, 'in'),
    (GPIO_E, 'out'),
    (GPIO_G, 'out')
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
            #subprocess.call("./wavSorter.sh")
            if getObject(): #bottle object
                gpio.digital_write(GPIO_E, GPIO.HIGH) # commence tilt
                gpio.digital_write(GPIO_G, GPIO.LOW)
                time.sleep(3)
                gpio.digital_write(GPIO_E, GPIO.LOW)
            else:
                gpio.digital_write(GPIO_E, GPIO.HIGH)
                gpio.digital_write(GPIO_G, GPIO.HIGH)
                time.sleep(3)
                gpio.digital_write(GPIO_E, GPIO.LOW)


def normalize1D(array):
	maxOfArray = np.amax(array)
	minOfArray = np.amin(array)
	rangeOfArray = maxOfArray - minOfArray
	returnArray = np.empty_like(array)
	iterator = 0
	for i in array:
		returnArray[iterator] = (i - minOfArray) / rangeOfArray
		iterator = iterator + 1

	return returnArray

def getValue(array):
	numElements = len(array)
	weightedSum = 0
	threshold = 0.9
	numberOfPeaks = 0
	for i in range(0, int(floor(numElements/2))):
		if array[i] > threshold:
			weightedSum = weightedSum + array[i] * i
			numberOfPeaks = numberOfPeaks + 1

	return weightedSum/numberOfPeaks

def getObject():
    filename = "trashRecording.wav"
    rate, data = read(filename)
    data = np.array(data)
    data = data[:,0]

    data_fft = abs(fft(data))
    data_fft = normalize1D(data_fft)


    print(filename + " " + str(getValue(data_fft)))

    threshold = 2250 # above this threshold = can.

    if getValue(data_fft) > threshold:
        print "can"
    	return 0 # can object
    else:
        print "bottle"
        return 1 # bottle object

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Blink LED on GPIO A (pin 23)')
    args = parser.parse_args()

    with GPIO(pins) as gpio:
        switch(gpio)
