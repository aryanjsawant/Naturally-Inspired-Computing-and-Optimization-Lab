import matplotlib.pyplot as plt
import numpy as np
import time
import random

def f(x):
    return x**2 - 4*x + 4

x_current = random.randint(-10, 10)
path = [x_current]

while True:
    neighbors = [x_current - 1, x_current + 1]
    neighbors = [x for x in neighbors if -10 <= x <= 10]
    next_x = x_current
    for x in neighbors:
        if f(x) < f(x_current):
            next_x = x
    if next_x == x_current:
        break
    else:
        x_current = next_x
        path.append(x_current)

print(f"Started at x = {path[0]}")
print(f"Hill Climbing stopped at x = {x_current}, f(x) = {f(x_current)}")

plt.ion()
fig, ax = plt.subplots()
x_plot = np.linspace(-10, 10, 400)
y_plot = f(x_plot)
ax.plot(x_plot, y_plot, label='f(x) = x² - 4x + 4', color='blue')

search_dots, = ax.plot([], [], 'ro-', label='Greedy Hill Climbing Path')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Greedy Hill Climbing Visualization')

greedy_x = []
greedy_y = []

for x in path:
    greedy_x.append(x)
    greedy_y.append(f(x))
    search_dots.set_data(greedy_x, greedy_y)
    plt.draw()
    plt.pause(0.5)

plt.ioff()
plt.savefig("lab1/results/greedy_hill_climbing_result.png")
plt.show()