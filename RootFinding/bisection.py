
import numpy as np
import matplotlib.pyplot as plt

# Take user input
func = input("Enter function f(x): ")   # Example: x**3 - x - 2
f = lambda x: eval(func)

a = float(input("Enter a: "))
b = float(input("Enter b: "))
tol = float(input("Enter tolerance: "))

# Bisection method
def bisection(a, b, tol):
    if f(a)*f(b) > 0:
        print("Invalid interval! f(a) and f(b) must have opposite signs.")
        return None
    while abs(b - a) > tol:
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return c

root = bisection(a, b, tol)
print("Approximate Root =", root)

# Plot graph
X = np.linspace(a-2, b+2, 400)
Y = [f(x) for x in X]
plt.plot(X, Y, label=f"f(x) = {func}")
plt.axhline(0, color='black')
plt.scatter(root, f(root), color='red', label=f"Root ≈ {root:.4f}")
plt.title("Bisection Method")
plt.legend()
plt.grid(True)
plt.show()
