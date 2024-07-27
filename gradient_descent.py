from sympy import *

def gd_it(x0, y0, g_x, g_y, gamma):
    x1 = x0 - gamma * g_x.subs(x, x0).subs(y, y0)
    y1 = y0 - gamma * g_y.subs(x, x0).subs(y, y0)

    return x1, y1


def gd(func, x0, y0, gamma, err):
    i = 0
    while i < 100:
        print(i, round(x0, err), round(y0, err))
        
        x1, y1 = gd_it(x0, y0, diff(func, x), diff(func, y), gamma)
        
        if round(x0, err) == round(x1, err) and round(y0, err) == round(y1, err):
            return x1, y1
        
        x0, y0 = x1, y1
        i = i + 1
    return x1, y1


x, y = symbols('x y')
func = x**2 + y**2 + 2*x + 4
x0 = 2
y0 = 1
gamma = 0.4
err = 5
print(func, diff(func, x), diff(func, y))
print(gd(func, x0, y0, gamma, err))
