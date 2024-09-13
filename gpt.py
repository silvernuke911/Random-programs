import math
import random

def newton_sqrt(n, x0, tol=1e-15, max_iter=1000):
    def f(x):
        return x**2 - n
    def df(x):
        return 2*x
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise Exception("Newton's method did not converge")

g=10
print(newton_sqrt(g,random.randint(0,g)))
print(math.sqrt(g))