from scipy import optimize
import numpy as np

def f(x):
    return 0.0074 * x ** 4 - 0.284 * x ** 3 + 3.355 * x ** 2 - 12.183 * x + 5


root = optimize.newton(f, 17)
print(root)

oldroot = optimize.newton(f, 16.15)
print(oldroot)