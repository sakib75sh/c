import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("Equation format: a1*x + b1*y + c1*z = d1 and so on.")
a1, b1, c1, d1 = map(float, input("Enter a1, b1, c1, d1: ").split())
a2, b2, c2, d2 = map(float, input("Enter a2, b2, c2, d2: ").split())
a3, b3, c3, d3 = map(float, input("Enter a3, b3, c3, d3: ").split())

A = np.array([[a1, b1, c1, d1],
              [a2, b2, c2, d2],
              [a3, b3, c3, d3]])

# Gauss-Jordan elimination
n = 3
for i in range(n):
    A[i] = A[i] / A[i][i]
    for j in range(n):
        if i != j:
            A[j] = A[j] - A[j][i]*A[i]

x, y, z = A[0,3], A[1,3], A[2,3]
print(f"Solution: x = {x:.4f}, y = {y:.4f}, z = {z:.4f}")

# 3D Graph
xx, yy = np.meshgrid(np.linspace(-10, 10, 20), np.linspace(-10, 10, 20))
z1 = (d1 - a1*xx - b1*yy)/c1
z2 = (d2 - a2*xx - b2*yy)/c2
z3 = (d3 - a3*xx - b3*yy)/c3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, z1, alpha=0.5, color='red')
ax.plot_surface(xx, yy, z2, alpha=0.5, color='green')
ax.plot_surface(xx, yy, z3, alpha=0.5, color='blue')
ax.scatter(x, y, z, color='black', s=50, label=f"Solution ({x:.2f}, {y:.2f}, {z:.2f})")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.title("Gauss-Jordan Elimination - 3D Graphical Solution")
plt.legend()
plt.show()
