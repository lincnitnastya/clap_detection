import numpy as np
import more_itertools as mit

from scipy.io import wavfile
from dtw import dtw
from math import floor



LEN_OF_CLAP = len(np.loadtxt('1.txt'))
DISCR_CONSTANT = 10
THRESHOLD = 0.9





def algorithm():
    _, DATA = wavfile.read('1.wav')
    ddata = DATA[::DISCR_CONSTANT]
    y = np.loadtxt('1.txt')[::DISCR_CONSTANT].reshape(-1, 1)
    l2_norm = lambda x, y: (x - y) ** 2
    distances = []

    for piece in(mit.windowed(ddata, n=floor(2 * LEN_OF_CLAP / DISCR_CONSTANT), 
                              step=floor(LEN_OF_CLAP / DISCR_CONSTANT), fillvalue=0)):
        x = np.array(piece).reshape(-1, 1)
        dist, _, _, _ = dtw(x, y, dist=l2_norm)
        distances.append(dist)
    return distances

def compare_with_median(distances):
    RATE, DATA = wavfile.read('1.wav')
    times = np.arange(len(DATA))/float(RATE)
    dtimes =  times[::DISCR_CONSTANT]   
    time_intervals = list(mit.windowed(dtimes, n=floor(2 * LEN_OF_CLAP/10 ), step=floor(LEN_OF_CLAP/10), fillvalue=0))
    median = np.median(distances)
    clap_times = [] 
    for time, item in zip(time_intervals, distances):
        if item < THRESHOLD * median:
            clap_times = clap_times + list(time)
    return clap_times