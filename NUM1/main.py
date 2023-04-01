# Dominik Juszczyk
# Python 3.8
# Metody numeryczne, grupa nr 4
# Zadanie numeryczne NUM1

import sympy as sp
from numpy import *
from matplotlib import pyplot as plt


def a(fun, point, h, htype):
    x = point
    f2 = eval(fun)
    x = point + h
    f1 = eval(fun)
    return htype((f1 - f2) / h)


def b(fun, point, h, htype):
    x = point + h
    f1 = eval(fun)
    x = point - h
    f2 = eval(fun)
    return htype((f1 - f2) / (2 * h))


def error(fun, point, h, htype, appr):
    x = sp.Symbol('x')
    derivative = sp.diff(fun, x)
    result = htype(derivative.evalf(subs={x: point}))
    return absolute(appr(fun, point, h, htype) - result)


def plot(fun, point, htype):
    if htype == float32:
        start = -8
        title = 'float'
    elif htype == float64:
        start = -16
        title = 'double'
    else:
        raise TypeError('wrong htype')

    plt.xscale('log')
    plt.yscale('log')

    xaxis = logspace(start, -1, num=1000, dtype=htype)      # endpoint=True, base=10
    ya = error(fun, point, xaxis, htype, a)
    yb = error(fun, point, xaxis, htype, b)
    plt.plot(xaxis, ya, label='a)')
    plt.plot(xaxis, yb, label='b)')

    plt.xlabel('h')
    plt.ylabel('E(h)')
    plt.title(title)
    plt.legend()
    plt.show()


plot('cos(x)', 0.3, float32)
plot('cos(x)', 0.3, float64)
