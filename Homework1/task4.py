import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return 4 * x - 1.8 * x ** 2 + 1.2 * x ** 3 - 0.3 * x ** 4


def fp(x):
    return 4 - 3.6 * x + 3.6 * x ** 2 - 1.2 * x ** 3



x_range = range(-10, 10)
x_values = [x for x in x_range]
y_values = [f(x) for x in x_values]


plt.plot(x_values, y_values)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot of f(x) = x^3 - 6x^2 + 11x - 6.1")
plt.ylim((-10, 10))
plt.axhline(y = 0, color = 'r', linestyle = '--')
plt.show()