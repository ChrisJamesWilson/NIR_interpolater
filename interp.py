
import numpy as np
import retrieve_irtf
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

# t is a table of the stars in the irtf library. The coloumns are: ID,   Teff(K),   logg,   Z/Zsun
t = retrieve_irtf.irtf_retrieve()

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
#Teff_new = input('Please enter a Teff between '+str(max(Teff))+' and '+min(Teff))
Teff_new = 5500
range_logg = max(logg)-min(logg)
#logg_new = input('Please enter a logg between '+str(max(logg))+' and '+min(logg))
logg_new = 3.7
range_Z = max(Z)-min(Z)
#Z_new = input('Please enter a Z between '+str(max(Z))+' and '+min(Z))
Z_new = -1
new_point = np.array([Teff_new, logg_new, Z_new])

plt.figure()
plt.scatter(Teff, logg, c=Z)
plt.xlabel('Teff')
plt.ylabel('logg')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.show()

length = len(Z)
#one = np.ones((length,3))
#t_big = np.dot(one, new_point, out=None)
new_point_big = np.tile(new_point,(length,1))
 #Creates an array of a chosen point of length of orginal data, to directly
 #compare the two

Diff = abs(new_point_big - t)
compare = np.array([[Diff[:,0]/range_Teff, Diff[:,1]/range_logg, Diff[:,2]/range_Z]])
 # Normalises values based on the parameters respective ranges

mean = np.sum(compare, axis=1)/3
 # Finds the relative normalised differences of any empirical star to the defined point
 
 # Square and squareroot would probably be a better idea here
 
#########
# Method 1 #
#########
 
 # Method 1 is such that ALL stars are considered for a single point.
 # We do so by again normalising the relative differences (mean) to now be
 # relative to each other, and using that as a basis for interpolation
 
rel_mean = mean/np.sum(mean)
 # Now each of these stars are indexed according to their position in the original
 # data, and this rel_mean value should be a multiplier of their spectral values,
 # summative to the final star

#########
# Method 2 #
#########
 
 # Method 2 is similar to 1, but instead picks a few of the closest values.

ind = np.argsort(mean)
closest = np.array([np.where(ind==0)[1], np.where(ind==1)[1], np.where(ind==2)[1]])
 # Location of the 3 closest 
stars = np.array([t[closest[0][0]], t[closest[1][0]], t[closest[2][0]]])
rel_weight = np.array([compare[0][2][closest[0][0]], compare[0][2][closest[1][0]],\
             compare[0][2][closest[2][0]]])
rel_weight = rel_weight/sum(rel_weight)
 # Has normalised the weighting of these 3 stars vs the chosen point. These 
 # weights must then be multiplies with the corresponding stars

















