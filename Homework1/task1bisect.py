from task1graphical import f


def bisect(func,xl,xu,es=0.1,maxit=20):
    if func(xl)*func(xu)>0:
        return 'initial estimates do not bracket solutions'
    xmold = xl
    for i in range(maxit):
        xm = (xl+xu)/2
        ea = abs((xm-xmold)/xm)
        if ea < es: break
        if func(xm)*func(xl)>0:
            xl = xm
        else:
            xu = xm
        xmold = xm
    return xm,func(xm),ea,i+1


lowroot = bisect(f, -1, 0)

print(lowroot)