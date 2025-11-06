import numpy as np
import matplotlib.pyplot as plt

f_str = input("Enter original function f(x): ")   # Example: x**3 - x - 2
g_str = input("Enter iteration function g(x): ")  # Example: (x+2/x**2)**(1/3)
f = lambda x: eval(f_str)
g = lambda x: eval(g_str)

x0 = float(input("Enter initial guess x0: "))
tol = float(input("Enter tolerance: "))

def iteration(x0, tol):
    while True:
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1

root = iteration(x0, tol)
print("Approximate Root =", root)

# Plot
X = np.linspace(root-5, root+5, 400)
Y = [f(xi) for xi in X]
plt.plot(X, Y, label=f"f(x) = {f_str}")
plt.axhline(0, color='black')
plt.scatter(root, f(root), color='red', label=f"Root ≈ {root:.4f}")
plt.title("Iteration Method")
plt.legend()
plt.grid(True)
plt.show()
