import numpy as np
import matplotlib.pyplot as plt

print("Equation format: a1*x + b1*y = c1 and a2*x + b2*y = c2")
a1, b1, c1 = map(float, input("Enter a1, b1, c1: ").split())
a2, b2, c2 = map(float, input("Enter a2, b2, c2: ").split())

A = np.array([[a1, b1, c1],
              [a2, b2, c2]])

# Forward elimination
ratio = A[1,0]/A[0,0]
A[1] = A[1] - ratio*A[0]

# Back substitution
y = A[1,2]/A[1,1]
x = (A[0,2] - A[0,1]*y)/A[0,0]

print(f"Solution: x = {x:.4f}, y = {y:.4f}")

# Graph
x_line = np.linspace(-10, 10, 200)
y1 = (c1 - a1*x_line)/b1
y2 = (c2 - a2*x_line)/b2

plt.plot(x_line, y1, label=f"{a1}x + {b1}y = {c1}")
plt.plot(x_line, y2, label=f"{a2}x + {b2}y = {c2}")
plt.scatter(x, y, color='red', label=f"Solution ({x:.2f}, {y:.2f})")
plt.title("Gauss Elimination - Graphical Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
