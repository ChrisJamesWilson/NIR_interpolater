import numpy as np
import matplotlib.pyplot as plt
import retrieve_irtf as ret
from mpl_toolkits.mplot3d import Axes3D

t = ret.param_retrieve()

plt.figure()

plt.hist(t[3],bins = 30,edgecolor = 'black')

plt.xlabel('Z')
plt.ylabel('Number of Stars')
plt.show()
