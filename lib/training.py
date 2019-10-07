import matplotlib.pyplot as plt
import numpy as np

h=6.626e-34
c= 3.0e+8
k= 1.38e-23
shift = 500 # defining the shift

#wav is the wavelength
def planck(wav, T):
    a= 2.0*h*c**2
    b= (h*c)/(wav*k*T)
    intensity = a/( (wav**5) * (np.exp(b)- 1.0) )
    return intensity

wavelengths= np.arange(1e-9, 2e-6, 1e-9)

intensity = planck( wavelengths, 20000.)
# creating a shifted intensity by padding 0 in the begining
# and removing extra values at the end
#shifted_intensity = np.concatenate((np.zeros(shift),intensity))[:-shift]

#sum_intensity = intensity + shifted_intensity


plt.plot(wavelengths*1e9, intensity, 'm-', label= '20000 K')
#plt.plot(wavelengths*1e9, shifted_intensity, 'b-', label='6000 K shifted')
#plt.plot(wavelengths*1e9, sum_intensity, 'r-', label= 'Summed intensity')

plt.xlabel('Wavelength\n(nm)')
plt.ylabel('Intensity\n(W Sr^-1 m^-3)')
plt.title('Black Body Radiation')
plt.legend()
plt.show()