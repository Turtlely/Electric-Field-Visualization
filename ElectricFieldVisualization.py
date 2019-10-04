from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def electricField(q1,x2,y2,z2):

	k = 9000000000

	rx = x2
	ry = y2
	rz = z2

	absr = np.sqrt((rx**2)+(ry**2)+(rz**2))

	Ux = rx/absr
	Uy = ry/absr
	Uz = rz/absr

	ex = ((k*q1)/(absr**2))* Ux
	ey = ((k*q1)/(absr**2))* Uy
	ez = ((k*q1)/(absr**2))* Uz

	return ex,ey,ez


electricX = []
electricY = []
electricZ = []

start = -3
end = 10

#calculate field in a square zone 
for x in range(start, end+1):
	for y in range(start, end+1):
		for z in range(start, end+1):
			field = electricField(0.01,x,y,z)
			electricX.append(field[0])
			electricY.append(field[1])
			electricZ.append(field[2])

fig = plt.figure()
ax = Axes3D(fig)

#plot
ax.scatter(electricX, electricY, electricZ, c='r', marker='o')
ax.scatter(0,0,0,c='b',marker='o')
plt.show()