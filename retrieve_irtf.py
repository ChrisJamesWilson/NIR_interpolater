import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
import itertools

# Code pertaining to reading and also determining file names in the irtf library

# Enter location of the irtf fits files relative to this directory here:

irtf_file = 'irtf_param.txt'

def irtf_retrieve():
	t = ascii.read(irtf_file)

	numstars = len(t)

	ID = list(itertools.repeat('.', numstars))
	Teff = np.zeros(numstars)
	logg = np.zeros(numstars)
	Z = np.zeros(numstars)

	for i in range(numstars):
		ID[i] = t[i][0]
		Teff[i] = t[i][1]
		logg[i] = t[i][2]
		Z[i] = t[i][3]

	plt.figure()
	plt.scatter(Teff, logg, c=Z)
	plt.xlabel('Teff')
	plt.ylabel('logg')
	plt.gca().invert_xaxis()
	plt.gca().invert_yaxis()
	plt.show()

	t = [ID,Teff,logg,Z]
	return(t)
