
import numpy as np
import retrieve_irtf

# t is a table of the stars in the irtf library. The coloumns are: ID,   Teff(K),   logg,   Z/Zsun
t = retrieve_irtf.irtf_retrieve()

Teff = np.array(t[1])
logg = np.array(t[2])
Z = np.array(t[3])


#usrTeff = input('Please input a desired Teff in kelvin: ')
usrTeff = 5000

while usrTeff < 0:
	print('Cannot have negative Temperature')
	usrTeff = input('Please input a desired Teff in kelvin: ')

#usrlogg = input('Please input a desired logg: ')
usrlogg = 2.0

rad = 2.5
#rad = input('Please enter a radius for the interpolator: ')

range_Teff = max(Teff)-min(Teff)
range_logg = max(logg)-min(logg)


