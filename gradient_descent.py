from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def show_fg(x0, y0, f):
    lam_f = lambdify([x, y], f, modules=['numpy'])
    
    f0 = lam_f(x0, y0)

    xv = np.arange(float(x0-1), float(x0+1), 0.1)
    yv = np.arange(float(y0-1), float(y0+1), 0.1)
    xv, yv = np.meshgrid(xv, yv)
    fv = lam_f(xv, yv)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    f_gr = ax.plot_surface(xv, yv, fv, cmap='winter')
    fp_gr = ax.plot([x0], [y0], [f0], markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5, alpha=0.5, zorder=100)
    plt.show()


def gd_it(x0, y0, func, gamma):
    x, y = symbols('x y')
    fx = diff(func, x)
    fy = diff(func, y)
    x1 = x0 - gamma * fx.subs([(x, x0), (y, y0)])
    y1 = y0 - gamma * fy.subs([(x, x0), (y, y0)])

    return x1, y1


def gd(func, x0, y0, gamma, err):
    i = 0
    printf = '%d: %.' + str(err) + 'f, %.' + str(err) + 'f'
    while i < 100:
        print(printf % (i, x0, y0))
        show_fg(x0, y0, func)
        
        x1, y1 = gd_it(x0, y0, func, gamma)
        
        if round(x0, err) == round(x1, err) and round(y0, err) == round(y1, err):
            return x1, y1
        
        x0, y0 = x1, y1
        i = i + 1
    return x1, y1


def main():
    x, y = symbols('x y')
    func = x**2 + y**2 + 2*x + 4
    x0 = 2
    y0 = 1
    gamma = 0.4
    err = 5
    print(func, diff(func, x), diff(func, y))
    print(gd(func, x0, y0, gamma, err))

if __name__ == '__main__':
    main()
