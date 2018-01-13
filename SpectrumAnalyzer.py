import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

# pyaudio fields
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

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
#data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 127

# reads wav file, makes array
from scipy.io.wavfile import read
a = read("wav/sound1.wav") #sound file
data_int = np.array(a[1],dtype=float)

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
freq = (np.abs(data_fft[:len(data_fft)]))

# plot: amplitude vs frequency
plt.plot(freq)
plt.title("Before filtering: Will have main signal (1000Hz) + noise frequency (50Hz)")
plt.xlim(0,10000)

# ----------------------------------------

# create a figure
fig, ax = plt.subplots()

# plot that figure: amplitude vs time
ax.plot(data_int, '-')
plt.show()