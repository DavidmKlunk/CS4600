from task1bisect import bisect
from task1false import falsepos
from task1graphical import f

bisectroot = bisect(f, -1, 0)
falseroot = falsepos(f, -1, 0)

print('The projected root by the bisection method is: ' + "{0:.6f}".format(bisectroot[0]))
print('The projected root by the false position method is: ' + "{0:.6f}".format(falseroot[0]))

num = bisectroot[0] - falseroot[0]
denom = (bisectroot[0] + falseroot[0]) / 2
diff = num / denom * 100

print('The percent diffence in the values is: ' + "{0:.6f}".format(diff))