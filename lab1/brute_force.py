import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 - 4*x + 4

x_vals = np.arange(-10, 11)
f_vals = [f(x) for x in x_vals]

min_index = np.argmin(f_vals)
min_x = x_vals[min_index]
min_y = f_vals[min_index]

print(f"Brute Force Minimum at x = {min_x}, f(x) = {min_y}")

plt.figure(figsize=(8, 5))
x_plot = np.linspace(-10, 10, 400)
y_plot = f(x_plot)
plt.plot(x_plot, y_plot, label='f(x) = x² - 4x + 4', color='blue')
plt.plot(min_x, min_y, 'go', label='Global Minimum (Brute Force)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Brute Force Search for Function Minimum')
plt.legend()
plt.grid(True)
plt.savefig('lab1/results/brute_force_result.png')
plt.show()
