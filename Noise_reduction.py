import pyfil as pf
import numpy as np
import scipy.signal as sp

t0 = 0
t1 = 5
f1 = 10
f2 = 1000
fs = 44100

t = np.linspace(t0,t1,fs*(t1-t0))

x = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)

pf.plotInTime(x, fs)

pf.plotInFrequency(x, fs)

Y = pf.LPFilter(100, 2000, x, fs)

pf.plotInTime(Y, fs)

pf.plotInFrequency(Y, fs)