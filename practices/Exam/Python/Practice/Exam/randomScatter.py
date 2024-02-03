import matplotlib.pyplot as plt
import random

# Generate 30 random 2D points
num_points = 30
x_values = [random.uniform(0, 10) for _ in range(num_points)]
y_values = [random.uniform(0, 10) for _ in range(num_points)]

# Plot the points using a scatter plot
plt.scatter(x_values, y_values, color='blue', label='Random Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Random 2D Points')
plt.legend()
plt.grid(True)
plt.show()
