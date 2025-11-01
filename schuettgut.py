import random
import math
import matplotlib.pyplot as plt

def random_points_with_min_distance(n, width, height, min_dist, max_tries=10000):
    """
    Erzeugt n zufällige Punkte im Rechteck [0,width]x[0,height],
    wobei kein Punkt einem anderen näher als min_dist ist.
    """
    points = []
    tries = 0
    
    while len(points) < n and tries < max_tries:
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        new_point = (x, y)
        
        # Prüfe Mindestabstand zu allen bestehenden Punkten
        if all(math.dist(new_point, p) >= min_dist for p in points):
            points.append(new_point)
        
        tries += 1

    if len(points) < n:
        print(f"Nur {len(points)} Punkte nach {tries} Versuchen erzeugt.")
    return points


# === Parameter einstellen ===
n = 50           # gewünschte Anzahl an Punkten
width = 10       # Breite des Bereichs
height = 10      # Höhe des Bereichs
min_dist = 0.8   # Mindestabstand zwischen Punkten

# === Punkte generieren ===
points = random_points_with_min_distance(n, width, height, min_dist)

# === Punkte darstellen ===
x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, c="royalblue", s=50)
plt.title(f"{len(points)} zufällige Punkte mit Mindestabstand {min_dist}")
plt.xlim(0, width)
plt.ylim(0, height)
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True, linestyle="--", alpha=0.4)

# Bild speichern
plt.savefig('point_cloud.png', dpi=300)
