# Team-0D-Hypercube

## SuSy: Sustainable Symphony 

Have you ever stopped in front of a trash can and not known where to throw 
your waste? Does this chicken bone go in the landfill, compost, or recycling?
What about this unused ketchup packet? Napkin? Paper cup? 

Description: Sustainable Symphony (SuSy) is a waste sorting device that utilizes 
waveform classification to distiguish different materials being disposed. 
With this classification deterimined on a Dragonboard 410c, an Arduino UNO
operates a servo to tilt the waste into the appropriate bin. An invention like
SuSy will make our product disposal easier for the normal person, and help
make our world more sustainable by automatically sorting our waste. 


### dragon.py 
Main python script that runs on dragonboard. If the button is pressed, the 
script will begin recording a trashRecording.wav. Then, the program will
analyze the recording and classify which direction to dump the trash. A 
2 bit encoded GPIO output to the Arduino will tell the Arduino which direction
to turn the servo to tilt the trash. Run this on the Dragonboard to start the
device. The program loops, so it will always be waiting for the next person 
to press the button and put in trash. 

### analyzeWav.py 
Waveform visualization and threshold testing. 

### Sweep.ino
The Arduino code that will receive the data from Dragonboard and perform the 
proper tilting. 

### wav 
Folder containing all the training .wav files

### SpectrumAnalyzer.py
Deprecated analyzer




