import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Input data
n = int(input("Enter number of data points: "))
x1 = np.array([float(input(f"x1[{i}]: ")) for i in range(n)])
x2 = np.array([float(input(f"x2[{i}]: ")) for i in range(n)])
y = np.array([float(input(f"y[{i}]: ")) for i in range(n)])

# Prepare data for sklearn
X = np.column_stack((x1, x2))
model = LinearRegression().fit(X, y)

print(f"Equation: y = {model.intercept_:.4f} + ({model.coef_[0]:.4f})x1 + ({model.coef_[1]:.4f})x2")

# Prediction for visualization (x2 fixed at mean)
x1_line = np.linspace(min(x1), max(x1), 100)
x2_fixed = np.mean(x2)
y_pred = model.predict(np.column_stack((x1_line, np.full_like(x1_line, x2_fixed))))

# Graph (2D projection)
plt.scatter(x1, y, color='blue', label='Data Points')
plt.plot(x1_line, y_pred, color='red', label='Fitted Line (x2 fixed)')
plt.title("Multiple Linear Regression (2D Projection)")
plt.xlabel("x1")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
