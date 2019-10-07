import numpy as np
import matplotlib.pyplot as plt


def boltzman(T):
    k = 8.617e-5
    E1 = -13.6
    E2 = -3.4
    N1 = 2 * (np.exp(-E1 / (k * T + 1e-8)))
    N2 = 8 * (np.exp(-E2 / (k * T + 1e-8)))
    number = N2 / (N1 + N2 + 1e-8)
    return number


T = np.arange(5000, 25000)

number = boltzman(T)

plt.plot(T, number)
plt.show()
