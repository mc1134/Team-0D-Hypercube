import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate=RATE,
	input=True,
	output=True,
	frames_per_buffer=CHUNK
)

data = stream.read(CHUNK)
#data_int = np.array(struct.unpack(str(2 * CHUNK) + 'B', data), dtype='b')[::2] + 127

from scipy.io.wavfile import read
a = read("wav/shortLastCarnival.wav")
data_int = np.array(a[1],dtype=float)

fig, ax = plt.subplots()

ax.plot(data_int, '-')
plt.show()