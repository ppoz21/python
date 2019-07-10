def f(x):
    y = -x**2/200
    return y


def g(x):
    y = 1+x**2/100-x/200
    return y


def trapez(a, b, h):
    pole = (a+b)*h/2
    return pole


def calka():
    i = 0.0
    pole = 0.0
    while i < 10:
        pole += (trapez(f(i), f(i+0.01), 0.01))+(trapez(g(i), g(i+0.01), 0.01))
        i += 0.01
    return pole


def minC():
    begin = 0
    for x in range(0, 1000000000):
        if g(x) - f(x) >= 26:
            begin = x
            break
    print('A: (', begin, ', ', f(begin), ')')
    print('B: (', begin, ', ', g(begin), ')')
    print('C: (', begin+100, ', ', f(begin), ')')
    print('D: (', begin+100, ', ', g(begin), ')')


print('Pole figury: ', calka(), '\n')
minC()

