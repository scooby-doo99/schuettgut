import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Punktwolke laden (hier als Beispiel eine zufällige Punktwolke)
# Angenommen, die Punktwolke ist in einer Textdatei gespeichert, wobei jede Zeile die Koordinaten eines Punktes enthält
points = np.random.rand(1000, 3)  # Beispiel: 1000 zufällige Punkte im 3D-Raum

# Perspektivische Projektion auf 2D (hier nur einfache z-Achse ignoriert)
x_proj = points[:, 0]
y_proj = points[:, 1]

# 2D Plot erstellen
plt.figure(figsize=(10, 10))
plt.scatter(x_proj, y_proj, c='blue', s=1)
plt.axis('equal')
plt.gca().set_facecolor('white')

# Bild speichern
plt.savefig('point_cloud.png', dpi=300)