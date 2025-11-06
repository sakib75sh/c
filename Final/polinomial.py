import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

# Input
n = int(input("Enter number of data points: "))
x = np.array([float(input(f"x[{i}]: ")) for i in range(n)])
y = np.array([float(input(f"y[{i}]: ")) for i in range(n)])
degree = int(input("Enter degree of polynomial: "))

# Fit polynomial
coeffs = np.polyfit(x, y, degree)
poly_eq = np.poly1d(coeffs)
print(f"Polynomial Equation:\n{poly_eq}")

# Plot
x_line = np.linspace(min(x), max(x), 200)
y_line = poly_eq(x_line)

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_line, y_line, color='red', label=f'Polynomial Degree {degree}')
plt.title("Polynomial Regression")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
