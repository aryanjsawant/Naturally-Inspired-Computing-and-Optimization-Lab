import matplotlib.pyplot as plt
import numpy as np
import time
import random
import numpy

range_end = 30
range_start = -1 * range_end

def f(x):
    return x*np.sin(4*x) + 2*x*np.sin(2*x)

x_current = random.uniform(range_start, range_end)
path = [x_current]

while True:
    neighbors = [x_current - 0.1, x_current + 0.1]
    neighbors = [x for x in neighbors if range_start <= x <= range_end]
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
x_plot = np.linspace(range_start, range_end, 400)
y_plot = f(x_plot)
ax.plot(x_plot, y_plot, label='f(x) = xsin(4x) + 2xsin(2x)', color='blue')

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
plt.savefig("lab1/results/greedy_hill_climbing_result_for_sine.png")
plt.show()