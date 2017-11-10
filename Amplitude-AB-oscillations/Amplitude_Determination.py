import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

Data = np.loadtxt('/Users/changjin/Desktop/test.txt',skiprows=5)
Time = Data[:,0]

Amp = Data[:,1]



n=len(Time)
dt=2.5/1000000000000
nu=np.fft.fftfreq(n,dt)
fk=np.fft.fft(Amp/n)

plt.plot(nu,fk.real,'r')
plt.show()
#print(dt)
#print(Time)
#print(Amp)
