import pyfil as pf
import numpy as np
import scipy.signal as sp

x = pf.Voice2Data('Alarm02.wav')
print(np.shape(x))