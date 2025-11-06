import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Input
n = int(input("Enter number of data points: "))
x = np.array([float(input(f"x[{i}]: ")) for i in range(n)]).reshape(-1, 1)
y = np.array([int(input(f"y[{i}] (0/1): ")) for i in range(n)])  # binary target

# Fit Logistic Regression
model = LogisticRegression()
model.fit(x, y)

print(f"Intercept: {model.intercept_[0]:.4f}, Coefficient: {model.coef_[0][0]:.4f}")

# Predict probability
x_line = np.linspace(min(x), max(x), 200).reshape(-1,1)
y_prob = model.predict_proba(x_line)[:,1]

# Graph
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_line, y_prob, color='red', label='Logistic Fit')
plt.title("Logistic Regression (sklearn)")
plt.xlabel("x")
plt.ylabel("Probability (y=1)")
plt.grid(True)
plt.legend()
plt.show()
