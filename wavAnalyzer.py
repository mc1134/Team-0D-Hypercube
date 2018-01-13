import pyaudio
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16 # data type determined by bits/sample for .wav
CHANNELS = 1 # mono Input
RATE = 48000 # Hz for .wav file

p = pyaudio.PyAudio # pyaudio object initialization
stream = p.open (
        format = FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
)

data = stream.read(CHUNK) # array of bytes

data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
#2*chunk is length of data

fig, ax = plt.subplots()
ax.plot(data_int, '-')
plt.show

rate, data = wav.read('bottle1.wav')
print "rate: %d" % rate
#print("data: "+data)
plt.plot(data, '-')
fft_out = fft(data)
#matplotlib inline
#plt.plot(data, np.abs(fft_out))
#plt.show()
