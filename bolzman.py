import matplotlib.pyplot as plt
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

#numpy.seterr(all=None, divide=None, over=None, under=None, invalid=None)[source]
#Set how floating-point errors are handled.
#Note that operations on integer scalar types (such as int16) are handled like floating point, and are affected by these settings.

def boltzman(T):

    k = 8.617e-5
    E1 = -13.6
    E2 = -3.4
    N1 = 2 * (np.exp(-E1 / k*T))
    N2 = 8 * (np.exp(-E2 / k*T))ㅊ
    number = N2/(N1+N2)
    return number

T = np.arange(5000,25000)

number = boltzman(T)

plt.plot(T,number)

plt.show()
