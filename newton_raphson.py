from sympy import *

def nr_it(x0, y0, f, g):
    fx = diff(f, x).subs([(x, x0), (y, y0)])
    fy = diff(f, y).subs([(x, x0), (y, y0)])
    gx = diff(g, x).subs([(x, x0), (y, y0)])
    gy = diff(g, y).subs([(x, x0), (y, y0)])

    f0 = f.subs([(x, x0), (y, y0)])
    g0 = g.subs([(x, x0), (y, y0)])

    J = Matrix([[fx, fy], [gx, gy]])
    F = Matrix([f0, g0])
    X = Matrix([x0, y0])

    P = (X - J**-1 * F).tolist()
    return P[0][0], P[1][0]


def nr(x0, y0, f, g, err):
    i = 0
    while i < 100:
        print(i, x0, y0)
        x1, y1 = nr_it(x0, y0, f, g)
        if round(x0, err) == round(x1, err) and round(y0, err) == round(y1, err):
            return x1, y1

        x0, y0 = x1, y1
        i = i + 1

    return x1, y1


x, y = symbols('x y')
f = x**2 + x*y - 10
g = y + 3*x*y**2 - 57
x0 = 1.5
y0 = 3.5
err = 10

print(nr(x0, y0, f, g, err))
