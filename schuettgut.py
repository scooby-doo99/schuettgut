import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import linalg as norm

# Punktwolke laden (hier als Beispiel eine zufällige Punktwolke)
# Angenommen, die Punktwolke ist in einer Textdatei gespeichert, wobei jede Zeile die Koordinaten eines Punktes enthält

density=100

d = 0.4

points1 = np.random.rand(density, 2)  # Beispiel: 1500 zufällige Punkte im 2D-Raum
points2 = np.random.rand(density, 2)

# Projektion in 2D
x_proj = points1[:, 0]
y_proj = 1.4*pow(points1[:, 0],2.0)-points1[:, 1]*pow(points1[:, 0],4.0)
#print(points[:, 0]*points[:, 1]*0)

#print(points1[:, 0:(density)])
#print(points1[:, 1:(density)])

r = norm.norm(points1[:, 0]+points1[:, 1])

print(r)

u = points1[:, 0]
v = points1[:, 1]

x_proj = points2[:, 0]
y_proj = points2[:, 1]

for j in range(density):
    if math.sqrt(pow(x_proj[j],2)+pow(y_proj[j],2))-0*math.sqrt(pow(x_proj[j-1],2)+pow(y_proj[j-1],2)) < 1:
        u[j]=0
        v[j]=0

for j in range(density):
    if math.sqrt(pow(x_proj[j],2)+pow(y_proj[j],2))-0*math.sqrt(pow(x_proj[j-1],2)+pow(y_proj[j-1],2)) > 1:
        x_proj[j]=0
        y_proj[j]=0

# 2D Plot erstellen
plt.figure(figsize=(10, 10))
plt.scatter(x_proj, y_proj, c='blue', s=1330)
plt.scatter(u, v, c='green', s=1393)
plt.axis('equal')
plt.gca().set_facecolor('white')

# Bild speichern
plt.savefig('point_cloud.png', dpi=300)
