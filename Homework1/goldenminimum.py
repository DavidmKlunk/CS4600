import numpy as np
from task4 import f

def goldmin(f,xl,xu,Ea,maxit=30):
    phi = (1 + np.sqrt(5))/2
    d = (phi - 1)*(xu-xl)
    x1 = xl + d ; f1 = f(x1)
    x2 = xu - d ; f2 = f(x2)
    for i in range(maxit):
        xint = xu - xl
        if f1 > f2:
            xopt = x1
            xl = x2
            x2 = x1
            f2 = f1
            x1 = xl + (phi-1)*(xu - xl)
            f1 = f(x1)
        else:
            xopt = x2
            xu = x1
            x1 = x2
            f1 = f2
            x2 = xu - (phi - 1)*(xu - xl)
            f2 = f(x2)
        if xopt != 0:
            ea = (2-phi)*abs(xint/xopt)
            if ea <= Ea: break
    return xopt, f(xopt), ea, i+1


tl = -2
tu = 4
Ea = .01
result = goldmin(f,tl,tu,Ea)
print(result)