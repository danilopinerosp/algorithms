#!/usr/bin/env python3

import sys

def karatsuba_multiplication(x, y):
    """Return the multiplication between x and y"""
    pass

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    multiplication = karatsuba_multiplication(x, y)
    print(multiplication)

except:
    print('ERROR: Only integers supported')
