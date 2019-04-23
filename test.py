import numpy as np
import matplotlib.pyplot as plt
import retrieve_irtf as ret
from mpl_toolkits.mplot3d import Axes3D

t = ret.param_retrieve()

for i in range(len(t[0])):
	ID = t[0][i]
	Teff = t[1][i]
	logg = t[2][i]
	Z = t[3][i]
	file_name = ret.set_spectra_name(Teff, logg, Z, ID)
	tt = np.loadtxt(file_name + '.txt')
	if i == 0:
		diff = np.zeros(len(t[0]))
	diff[i] = np.mean(tt[:,2])


plt.figure()

cm = plt.cm.get_cmap('viridis')
plot = plt.scatter(t[1], t[2], c=diff, cmap=cm)
plt.colorbar(plot)
#plt.scatter(Teff_new,logg_new, c='r')
plt.xlabel('Teff')
plt.ylabel('logg')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.show()

plt.figure()

cm = plt.cm.get_cmap('viridis')
plot = plt.scatter(t[1], t[3], c=diff, cmap=cm)
plt.colorbar(plot)
#plt.scatter(Teff_new,logg_new, c='r')
plt.xlabel('Teff')
plt.ylabel('Z')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

plt.show()
