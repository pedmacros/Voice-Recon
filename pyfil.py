import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundcard as sc
from scipy.io import wavfile
import scipy.signal as sp

def record(t,fs):
    mic = sc.default_microphone()
    samples = fs*t
    x = mic.record(samples,fs)
    return(x)

def readWav(fileName):
    x = wavfile.read(fileName)
    return(x)

def saveWav(fileName, fs, x):
    wavfile.write(fileName, fs, x)
    
def play(x,fs):
    sd.play(x, fs)

def FFT(x):
    N = int(np.size(x,0)/2)
    X = np.fft.fft(x)
    X = np.abs(X)
    X = X[:N]

def plotInTime(x,fs):
    t=np.arange(0,np.size(x,0)/fs,1/fs)
    plt.figure()
    plt.plot(t,x)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    
def plotInFrequency(x,fs):
    N=int(np.size(x,0)/2)
    if np.size(x,0)==1:
        X=np.fft.fft(x,axis=1)
    else:
        X=np.fft.fft(x,axis=0)
    X=np.abs(X)
    X=X[:N]
    f=np.arange(0,fs/2,fs/2/N)
    print(np.shape(X))
    print(np.shape(f))
    plt.figure()
    plt.plot(f,X)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)  
    
def LPFilter(fc, N, x, fs):
    fc=np.array(fc)
    wCut=(fc/(fs/2))
    
    b=sp.firwin(N,wCut)
    a=[1.]
    w,H=sp.freqz(b, a, worN=512, plot=None)
    f=(w/(np.pi))*(fs/2)
    
    y=sp.lfilter(b,a,x,axis=0)
    
    xMax=x.max()
    yMax=y.max()
    y=y*xMax/yMax
    y=y.astype('int16')
    return(y)