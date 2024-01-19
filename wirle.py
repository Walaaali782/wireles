import numpy as np
import matplotlib.pyplot as plt

a = 2
f = 1.0
phase = 0
cycles = 10
T = 1 / f
fs = 300 * f
Ts = 1 / fs
t = np.arange(0, T * cycles, Ts)
x = a * np.sin(2 * np.pi * f * t + phase)
plt.plot(t, x)
plt.show()



# import numpy as np 
# import matplotlib.pyplot as plt
# A = 1 #amplitupe
# F= 2
# sr = 100 #sample rate 
# t = np.arange(0,10,1/sr) #0.001 sec
# P= 0
# y = A * np.sin(2*np.pi*F*t + P)

# plt.figure(figsize=(10,4))
# plt.plot(t,y)
# plt.title("sine wave")
# plt.show()










