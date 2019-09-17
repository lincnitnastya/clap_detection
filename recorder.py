import wave
import math
# alsaaudio since pyaudio gave IOError: [Errno Input overflowed] -9981
import alsaaudio   
import numpy as np




FORMAT = alsaaudio.PCM_FORMAT_S16_LE
CHANNELS = 1
CHUNK = 1024
RATE = 44100
RECORD_SECONDS = 3


def recordAudio(recorder):
    fileName = "1.wav"
    wf = wave.open(fileName, 'w')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(2)
    wf.setframerate(RATE)
    print("***  recording ***")
    for i in range(0, math.floor(1000*RECORD_SECONDS/22)):
        l, data = recorder.read()
        wf.writeframes(data)
    wf.close()
    print("written")
    

def set_and_record():
    recorder = alsaaudio.PCM(type=alsaaudio.PCM_CAPTURE)
    recorder.setchannels(CHANNELS)
    recorder.setrate(RATE)
    recorder.setformat(FORMAT)
    recorder.setperiodsize(CHUNK)
    recordAudio(recorder)
