import numpy as np
from astropy.io import ascii
from astropy.io import fits
import matplotlib.pyplot as plt
import itertools

# Code pertaining to reading and also determining file names in the irtf library

# Enter location of the irtf fits files relative to this directory here:

irtf_file = 'irtf_param.txt'

def param_retrieve():
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

	t = [ID,Teff,logg,Z]
	return(t)

def get_spectra(ID):
    
    t = fits.getdata('irtf/' + ID + '.fits')
    
    tt = np.zeros([len(t),2])
    tt[:,1] = t
    tt[:,0] = np.arange(0,len(t))    
    
    return(tt)
    
