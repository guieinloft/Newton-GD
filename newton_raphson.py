from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def show_fg(x0, y0, f, g):
    lam_f = lambdify([x, y], f, modules=['numpy'])
    lam_g = lambdify([x, y], g, modules=['numpy'])
    
    f0 = lam_f(x0, y0)
    g0 = lam_g(x0, y0)

    diff = abs(f0 - g0)

    xv = np.arange(float(x0-1), float(x0+1), 0.1)
    yv = np.arange(float(y0-1), float(y0+1), 0.1)
    xv, yv = np.meshgrid(xv, yv)
    fv = lam_f(xv, yv)
    gv = lam_g(xv, yv)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    f_gr = ax.plot_surface(xv, yv, fv, cmap='winter')
    g_gr = ax.plot_surface(xv, yv, gv, cmap='autumn')
    fp_gr = ax.plot([x0], [y0], [f0], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5, alpha=0.5, zorder=100)
    gp_gr = ax.plot([x0], [y0], [g0], markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5, alpha=0.5, zorder=100)
    plt.show()


def nr_it(x0, y0, f, g):
    x, y = symbols('x y')
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
        print(i, round(x0, err), round(y0, err))
        show_fg(x0, y0, f, g)
        x1, y1 = nr_it(x0, y0, f, g)
        if round(x0, err) == round(x1, err) and round(y0, err) == round(y1, err):
            return x1, y1

        x0, y0 = x1, y1
        i = i + 1

    return x1, y1

def main():
    x, y = symbols('x y')
    f = x**2 + x*y - 10
    g = y + 3*x*y**2 - 57
    x0 = 1.5
    y0 = 3.5
    err = 5

    print(nr(x0, y0, f, g, err))

if __name__ == '__main__':
    main()
