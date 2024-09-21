import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return -12 - 21 * x + 18 * (x ** 2) - 2.75 * (x ** 3)


x_range = range(-1, 4)
x_values = [x for x in x_range]
y_values = [f(x) for x in x_values]


plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = -12 - 21x + 18x^2 - 2.75x^3")
plt.ylim((-5, 5))
plt.axhline(y = 0, color = 'r', linestyle = '--')
plt.show()
