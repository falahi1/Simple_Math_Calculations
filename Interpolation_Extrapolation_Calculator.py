import matplotlib.pyplot as plt
from math import *

# Function to calculate the divided difference table
def newton_divided_difference(x_points, y_points):
    n = len(x_points)
    table = [y_points]  # Initial table with y-values
    for j in range(1, n):
        column = []
        for i in range(n - j):
            diff = (table[j - 1][i + 1] - table[j - 1][i]) / (x_points[i + j] - x_points[i])
            column.append(diff)
        table.append(column)
    return table

# Function to evaluate the Newton's interpolated polynomial at a given x
def evaluate_newton_polynomial(x_points, table, x):
    n = len(x_points)
    result = table[0][0]
    product = 1
    for i in range(1, n):
        product *= (x - x_points[i - 1])
        result += table[i][0] * product
    return result

# Main program starts here
n = int(input("Please enter the nth order (number of points): "))
p = int(input("Please enter the number of points: "))

# Lists to store the x and y data points
x_points = []
y_points = []

# Input the x and y data points
for i in range(p):
    x = float(input(f"Enter x[{i}]: "))
    y = float(input(f"Enter y[{i}]: "))
    x_points.append(x)
    y_points.append(y)

# Now, we have to choose an x value for interpolation or extrapolation
x_val = float(input("Please enter the x value to perform interpolation or extrapolation: "))

# Calculate the divided difference table
table = newton_divided_difference(x_points, y_points)

# Evaluate the result using Newton's Interpolated Polynomial
result = evaluate_newton_polynomial(x_points, table, x_val)

# Output the result
print(f"The result at x = {x_val} is: {result}")

# Plot the data points and the interpolating polynomial
x_plot = [i * 0.1 for i in range(int(min(x_points) * 10), int(max(x_points) * 10) + 1)]
y_plot = [evaluate_newton_polynomial(x_points, table, xi) for xi in x_plot]

# Plot the original data points
plt.plot(x_points, y_points, 'ro', label='Original Points')

# Plot the Newton interpolated polynomial curve
plt.plot(x_plot, y_plot, 'g-', label='Interpolated Polynomial')

# Plot the specific point for interpolation/extrapolation
plt.plot(x_val, result, 'bo', label=f'Interpolated/Extrapolated Point ({x_val}, {result})')

# Adding labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Newton Interpolation and Extrapolation')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
