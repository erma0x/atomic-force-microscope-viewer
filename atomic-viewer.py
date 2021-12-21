
import pylab
import numpy as np
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


z = pylab.loadtxt("data/topography_in_nanometers.txt",skiprows=11, unpack = True)

print("lung di z =", len(z))


result = np.where(z == 121.033581)
result2 = np.where(z == 121.368675)
print(result,result2)


a=0
data=np.zeros((129,129))

for i in range(0,128):         # i=coord di y, j=coord di x
    for j in range(0,128):
        data[i,j] = z[a]
        a+=1

res = np.where(data == 121.033581)
res2 = np.where(data == 121.368675)
print(res,res2)

# Make data.
X = np.arange(0, 129, 1)
Y = np.arange(0, 129, 1)
X, Y = np.meshgrid(X, Y)

fig = plt.figure(figsize=(15,12))
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(X, Y, data, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


ax.set_zlim(0, max(z))
ax.set_xlim(127, 0)

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

asse=np.linspace(0,len(z)-1,len(z))

pylab.figure( )
pylab.plot(asse, z)

plt.show()





