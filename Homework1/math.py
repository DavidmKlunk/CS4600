from task2graphically import f


x0 = 1
fx0 = f(x0)
s = .01


def numerator(x):
    return f(x) * s * x


def denominator(x):
    first = f(x + (s * x))
    return first - f(x)


x1 = (x0 - (numerator(x0) / denominator(x0)))
print(x1)
x2 = (x1 - (numerator(x1) / denominator(x1)))
print(x2)
x3 = (x2 - (numerator(x2) / denominator(x2)))
print(x3)
x4 = (x3 - (numerator(x3) / denominator(x3)))
print(x4)
x5 = (x4 - (numerator(x4) / denominator(x4)))
print(x5)
