import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# User input
n = int(input("Enter number of equations: "))

# Input augmented matrix [A|B]
A = np.zeros((n, n))
B = np.zeros(n)
for i in range(n):
    row = list(map(float, input(f"Enter coefficients of equation {i+1} and constant term (separated by space): ").split()))
    if len(row) != n+1:
        raise ValueError(f"Please enter {n} coefficients and 1 constant term")
    A[i] = row[:n]
    B[i] = row[-1]

# Gauss Elimination (forward elimination)
aug = np.hstack((A, B.reshape(-1,1)))  # Augmented matrix
for i in range(n-1):
    for j in range(i+1, n):
        if aug[i,i] == 0:
            raise ZeroDivisionError("Zero pivot encountered.")
        ratio = aug[j,i]/aug[i,i]
        aug[j] = aug[j] - ratio*aug[i]

# Back substitution
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (aug[i,-1] - np.dot(aug[i,i+1:n], x[i+1:n]))/aug[i,i]

# Print solution
for i in range(n):
    print(f"x{i+1} = {x[i]:.4f}")

# Visualization (only for 2 or 3 equations)
if n == 2:
    # 2D plot
    x_line = np.linspace(min(x)-2, max(x)+2, 200)
    y1 = (B[0] - A[0,0]*x_line)/A[0,1]
    y2 = (B[1] - A[1,0]*x_line)/A[1,1]
    plt.plot(x_line, y1, label=f"Eq1")
    plt.plot(x_line, y2, label=f"Eq2")
    plt.scatter(x[0], x[1], color='red', label=f"Solution ({x[0]:.2f}, {x[1]:.2f})")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title("Gauss Elimination - 2D Graph")
    plt.legend()
    plt.grid(True)
    plt.show()

elif n == 3:
    # 3D plot
    xx, yy = np.meshgrid(np.linspace(min(x)-2, max(x)+2, 20),
                         np.linspace(min(x)-2, max(x)+2, 20))
    z1 = (B[0] - A[0,0]*xx - A[0,1]*yy)/A[0,2]
    z2 = (B[1] - A[1,0]*xx - A[1,1]*yy)/A[1,2]
    z3 = (B[2] - A[2,0]*xx - A[2,1]*yy)/A[2,2]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xx, yy, z1, alpha=0.5, color='red')
    ax.plot_surface(xx, yy, z2, alpha=0.5, color='green')
    ax.plot_surface(xx, yy, z3, alpha=0.5, color='blue')
    ax.scatter(x[0], x[1], x[2], color='black', s=50, label=f"Solution ({x[0]:.2f}, {x[1]:.2f}, {x[2]:.2f})")
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("x3")
    plt.title("Gauss Elimination - 3D Graph")
    plt.legend()
    plt.show()
else:
    print(f"Graph visualization not available for {n} equations. Solution computed successfully.")
