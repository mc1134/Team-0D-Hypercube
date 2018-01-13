import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io.wavfile import read
from sklearn.preprocessing import normalize
from math import floor

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


# getValue will return the weighted sum of the values in numpy array. Array is 
# assumed to be a normalized1D array so the sum will simply be a weight of the
# indicies of the array, with everything below the threshold ignored. This 
# method will only sum the first half of the indicies because the fft if 
# mirrored
def getValue(array):
	numElements = len(array)
	weightedSum = 0
	threshold = 0.9
	numberOfPeaks = 0   
	for i in range(0, floor(numElements/2)): 
		if array[i] > threshold: 
			weightedSum = weightedSum + array[i] * i
			numberOfPeaks = numberOfPeaks + 1

	return weightedSum/numberOfPeaks	
	

filename = "trashRecording.wav"
rate, data = read(filename)
data = np.array(data)
data = data[:,0]

data_fft = abs(fft(data))
data_fft = normalize1D(data_fft)

	
print(filename + " " + str(getValue(data_fft)))

threshold = 2250 # above this threshold = can. 

if getValue(data_fft) > threshold: 
	print("can")
else 
	print("bottle")


	
