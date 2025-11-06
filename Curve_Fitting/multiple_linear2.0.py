import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Input data
n = int(input("Enter number of data points: "))
m = int(input("Enter number of independent variables/features: "))

# Read features
X = np.zeros((n, m))
for j in range(m):
    X[:, j] = [float(input(f"x{j+1}[{i}]: ")) for i in range(n)]

# Read dependent variable
y = np.array([float(input(f"y[{i}]: ")) for i in range(n)])

# Fit model
model = LinearRegression()
model.fit(X, y)

# Print equation
equation = f"y = {model.intercept_:.4f}"
for i in range(m):
    equation += f" + ({model.coef_[i]:.4f})x{i+1}"
print("Equation:", equation)

# 2D/3D visualization if possible
if m == 1:
    # Simple 2D plot
    x_line = np.linspace(min(X[:,0]), max(X[:,0]), 100).reshape(-1,1)
    y_pred = model.predict(x_line)
    plt.scatter(X[:,0], y, color='blue', label='Data Points')
    plt.plot(x_line, y_pred, color='red', label='Fitted Line')
    plt.xlabel("x1")
    plt.ylabel("y")
    plt.title("Multiple Linear Regression (1 feature)")
    plt.legend()
    plt.grid(True)
    plt.show()

elif m == 2:
    # 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:,0], X[:,1], y, color='blue', label='Data Points')
    x1_line = np.linspace(min(X[:,0]), max(X[:,0]), 20)
    x2_line = np.linspace(min(X[:,1]), max(X[:,1]), 20)
    x1_grid, x2_grid = np.meshgrid(x1_line, x2_line)
    y_grid = model.predict(np.column_stack((x1_grid.ravel(), x2_grid.ravel()))).reshape(x1_grid.shape)
    ax.plot_surface(x1_grid, x2_grid, y_grid, color='red', alpha=0.5)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("y")
    plt.title("Multiple Linear Regression (2 features)")
    plt.show()

else:
    print(f"Cannot visualize more than 2 features. Model fitted for {m} features.")
