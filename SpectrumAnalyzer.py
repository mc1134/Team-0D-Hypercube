import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# pyaudio fields
CHUNK = 1024 * 4 #how much audio is processed at a time, how many samples per frame to display
FORMAT = pyaudio.paInt16 #depends on bits per sample
CHANNELS = 1 #basically num of microphones
RATE = 44100 #samples per second

# instantiate pyaudio
p = pyaudio.PyAudio()
stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate=RATE,
	input=True,
	output=True,
	frames_per_buffer=CHUNK
)

# make pyaudio array
data = stream.read(CHUNK)

# struct unpack turns the bytes of stream into integers
#data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 127

# reads wav file, makes array
from scipy.io.wavfile import read
a = read("wav/can2.wav") #sound file
data_int = np.array(a[1],dtype=float)
data_transform = fft(data_int)
data_transform_abs = abs(data_transform)

<<<<<<< HEAD
# fig, ax = plt.subplots()

plt.figure(1)
plt.plot(data_transform_abs, '-')
#plt.show()

plt.figure(2)
plt.plot(data_int)
plt.show()
=======
# sine wave fields
frequency = 1000
noisy_freq = 50
num_samples = 48000
sampling_rate = 48000.0 #SR/NS<1 shifts right, SR/NS>1 shifts left

# sine wave tests
sine_wave = [np.sin(2 * np.pi * frequency * x1 / sampling_rate) for x1 in range(num_samples)]
sine_noise = [np.sin(2 * np.pi * noisy_freq * x1/  sampling_rate) for x1 in range(num_samples)]
sine_wave = np.array(sine_wave)
sine_noise = np.array(sine_noise)

# makes sine wave array (with noise = convoluted sine wave array)
#data_int = sine_wave + sine_noise

# ----------------------------------------

# fast fourier transform
data_fft = np.fft.fft(data_int)
freq = (np.abs(data_fft))

N = num_samples

# fft.fftfreq stuff; does the same as "fast fourier transform" except much more compact
#freq = np.fft.fftfreq(N)
#ind=np.arange(1,N/2+1)
#psd=abs(data_fft[ind])**2+abs(data_fft[-ind])**2
#plt.plot(freq[ind],psd,'k-')

# plot: amplitude vs frequency
plt.plot(freq)
plt.title("Relative strength vs frequency")
plt.xlim(0,30000)

# ----------------------------------------

# create a figure
fig, ax = plt.subplots()

# plot that figure: amplitude vs time
ax.plot(data_int, '-')
plt.title("Signal vs time")
plt.show()
>>>>>>> 36433ad73ae395941d8c0bf2612ee1f7fbc3bcb8
