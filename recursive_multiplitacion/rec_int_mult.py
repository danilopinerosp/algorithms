#!/usr/bin/env python3

import sys

def rec_int_mult(x, y):
    """Return the multiplication between x and y"""
    x = str(x)
    y = str(y)
    nx = len(x)
    ny = len(y)
    if nx > ny:
        y = '0' * (nx - ny) + y
    elif ny > nx:
        x = '0' * (ny - nx) + x

    n = len(x)
    if n == 1:
        return int(x) * int(y)
    else:
        a = x[0: n // 2]
        b = x[n // 2 : n]
        c = y[0: n // 2]
        d = y[n // 2: n]
        ac = rec_int_mult(a, c)
        ad = rec_int_mult(a, d)
        bc = rec_int_mult(b, c)
        bd = rec_int_mult(b, d)
        return 10 ** n * ac + 10 ** (n // 2) * (ad + bc) + bd
        

x = sys.argv[1]
y = sys.argv[2]

multiplication = rec_int_mult(x, y)

print(multiplication)
