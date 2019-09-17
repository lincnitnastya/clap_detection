import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile


def plotter(clap_times):
    RATE, DATA = wavfile.read('1.wav')
    plt.figure(figsize=(60, 30))
    times = np.arange(len(DATA))/float(RATE)
    plt.plot(times, DATA, alpha=0.5)
    plt.grid()
    plt.scatter(clap_times, np.zeros(len(clap_times)), 
                color='black', s=200, alpha=1, label="clap intervals")
    plt.xlabel('time (s)', size=20)
    plt.ylabel('amplitude', size=20)
    plt.rcParams.update({'font.size': 20})
    plt.legend()
    #plt.show()
    plt.savefig('1.png')
    
