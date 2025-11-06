import numpy as np
import matplotlib.pyplot as plt

# Input for 2 equations
print("Equation format: a1*x + b1*y = c1 and a2*x + b2*y = c2")
a1, b1, c1 = map(float, input("Enter a1, b1, c1: ").split())
a2, b2, c2 = map(float, input("Enter a2, b2, c2: ").split())

A = np.array([[a1, b1],
              [a2, b2]])
B = np.array([c1, c2])

detA = np.linalg.det(A)
if detA == 0:
    print("No unique solution (Lines are parallel or coincident).")
else:
    X = np.linalg.solve(A, B)
    x_val, y_val = X
    print(f"Solution: x = {x_val:.4f}, y = {y_val:.4f}")

    # Graph representation
    x = np.linspace(-10, 10, 200)
    y1 = (c1 - a1*x)/b1
    y2 = (c2 - a2*x)/b2

    plt.plot(x, y1, label=f"{a1}x + {b1}y = {c1}")
    plt.plot(x, y2, label=f"{a2}x + {b2}y = {c2}")
    plt.scatter(x_val, y_val, color='red', label=f"Solution ({x_val:.2f}, {y_val:.2f})")
    plt.title("Cramer's Rule - Graphical Solution")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
