from task1graphical import f

def falsepos(func, xl, xu, es=0.1, maxit=20):
    if func(xl)*func(xu)>0:
        return 'initial estimates do not bracket solutions'
    xmold = xl
    for i in range(maxit):
        xr = ((f(xl)*xu) - (f(xu)*xl))/((f(xl))-f(xu))
        ea = abs((xr-xmold)/xr)
        if ea < es: break
        if func(xr)*func(xl)>0:
            xl = xr
        else:
            xu = xr
        xmold = xr
    return xr,func(xr),ea,i+1


lowroot = falsepos(f, -1, 0)

print(lowroot)