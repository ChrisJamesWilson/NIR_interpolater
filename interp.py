
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
import os
from astropy.io import fits
import retrieve_irtf as ret
#from mpl_toolkits.mplot3d import Axes3D

# t is a table of the stars in the irtf library. The coloumns are: ID,   Teff(K),   logg,   Z/Zsun
t = ret.param_retrieve()

Teff = np.array(t[1])
logg = np.array(t[2])
Z = np.array(t[3])

ID = t[0]
t = np.stack((Teff,logg,Z), axis=1)


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
#Teff_new = input('Please enter a Teff between ' + str(max(Teff)) + ' and ' + str(min(Teff)))
Teff_new = 5986
range_logg = max(logg)-min(logg)
#logg_new = input('Please enter a logg between ' + str(max(logg)) + ' and ' + str(min(logg)))
logg_new = 4.11
range_Z = max(Z)-min(Z)
#Z_new = input('Please enter a Z between ' + str(max(Z)) + ' and ' + str(min(Z)))
Z_new = -0.13
new_point = np.array([Teff_new, logg_new, Z_new])

# Removed IRL60 for testing

#plt.figure()
#plt.scatter(Teff, logg, c=Z)
#plt.xlabel('Teff')
#plt.ylabel('logg')
#plt.gca().invert_xaxis()
#plt.gca().invert_yaxis()
#plt.show()

length = len(Z)
#one = np.ones((length,3))
#t_big = np.dot(one, new_point, out=None)
new_point_big = np.tile(new_point,(length,1))
 #Creates an array of a chosen point of length of orginal data, to directly
 #compare the two

Tn = 1
gn = 1
Zn = 1

Diff = abs(new_point_big - t)




Diff[:,0] = Diff[:,0]**Tn
Diff[:,1] = Diff[:,1]**gn
Diff[:,2] = Diff[:,2]**Zn

 # nth power
compare = np.array([Diff[:,0]/range_Teff, Diff[:,1]/range_logg, Diff[:,2]/range_Z])
 # Normalises values based on the parameters respective ranges

#mean = np.sum(compare, axis=1)/3
mean = np.sqrt(Diff[:,0]**2 + Diff[:,1]**2 + Diff[:,2]**2)
 # Finds the relative normalised differences of any empirical star to the defined point
diff_sort = np.sort(mean)

radii = 5e2

stars = np.where(mean < radii)[0]

#close = 5

#star = np.zeros(close)

#for i in range(close):
	#star[i] = int(np.where(mean == diff_sort[i])[0][0])

# Square and squareroot would probably be a better idea here

#########
# Method 1 #
#########

# Method 1 is such that ALL stars are considered for a single point.
# We do so by again normalising the relative differences (mean) to now be
# relative to each other, and using that as a basis for interpolation
 
rel_weight = (1/mean).T

 # Now each of these stars are indexed according to their position in the original
 # data, and this rel_mean value should be a multiplier of their spectral values,
 # summative to the final star

#########
# Method 2 #
#########
 
# # Method 2 is similar to 1, but instead picks a few of the closest values.
#
#ind = np.argsort(mean)
#closest = np.array([np.where(ind==0)[1], np.where(ind==1)[1], np.where(ind==2)[1]])
# # Location of the 3 closest 
#stars = np.array([t[closest[0][0]], t[closest[1][0]], t[closest[2][0]]])
#
#rel_weight = np.array([compare[0][2][closest[0][0]], compare[0][2][closest[1][0]],\
#             compare[0][2][closest[2][0]]])
#             
#rel_weight = rel_weight/sum(rel_weight)
#
# # Has normalised the weighting of these 3 stars vs the chosen point. These 
# # weights must then be multiplies with the corresponding stars
#spec_ID = np.array([ID[closest[0][0]], ID[closest[1][0]], ID[closest[2][0]]])


##########################
 # Dealing with the files
##########################

#os.chdir('./irtf')

int_spectra = np.zeros(15000)

for i in stars:
	int_spectra = int_spectra + ret.get_spectra(ID[int(i)])[:,1]*rel_weight[int(i)]

        # Sets up a length x (i+1) array of the spectras, where the first column
        # is the x axis and the other columns are the chosen stars in order of
        # closest to farthest 
        # Also multiplies the spectra by their relative weights to the chosen point


#for i in range(3):
#	plt.figure()
#	plt.plot(chosen_spectra[:,0],chosen_spectra[:,i+1]/rel_weight[i])


#int_spectra = np.array([chosen_spectra[:,0], chosen_spectra[:,1:].sum(axis=1)]).T

t_1 = ret.get_spectra(ID[int(stars[0])])
#t_2 = ret.get_spectra(ID[int(stars[1])])
#t_3 = ret.get_spectra(ID[int(stars[2])])
t_rl = ret.get_spectra('IRL060')

t2 = np.loadtxt('sometxt.txt')

t2[:,1][abs(t2[:,1])>9e2] = 0

x = np.linspace(0,len(t2),len(t_1))

fp = t2[:,0]

xp = np.linspace(0,len(t2),len(t2))

#gp = np.interp(x,xp,fp)

gp = np.arange(0,len(t_1))

plt.figure()

plt.plot(gp,t_rl[:,1]/t_rl[0,1], 'r', gp, int_spectra/int_spectra[0],'b')


#compar = t_rl - int_spectra

plt.xlabel('Wavelength (\u03BC m)')
plt.ylabel('Normalised Flux')
plt.show()













