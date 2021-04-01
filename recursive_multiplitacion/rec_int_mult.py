#!/usr/bin/env python3

def rec_int_mult(x, y=0):
    """Return the multiplication between x and y using recursive algorithm."""
    (sign_x, sign_y) = (1, 1)

    # Enable multipliaction of negative numbers
    if x < 0:
        sign_x = -1
        x = x * sign_x
    if y < 0:
        sign_y = -1
        y = y * sign_y

    # sign of the final result
    sign = sign_x * sign_y

    #  Number of digits of both numers (x, y)

    x = str(x)      # Change x to string
    y = str(y)      # Change y to string
    size_x = len(x)
    size_y = len(y)

    n = max(size_x, size_y)

    if n % 2 != 0 and n != 1:
        n = n + 1

    x = '0' * (n - size_x) + x
    y = '0' * (n - size_y) + y
        
    if n == 1:
        return int(x) * int(y)
    else:
        a = int(x[: n // 2])     # First half of x
        b = int(x[n // 2:])      # Second half of x
        c = int(y[:n // 2])     # First half of y
        d = int(y[n // 2:])  # Second half of y
        ac = rec_int_mult(a, c)
        ad = rec_int_mult(a, d)
        bc = rec_int_mult(b, c)
        bd = rec_int_mult(b, d)
        result = (10 ** n) * ac + (10 ** (n // 2)) * (ad + bc) + bd
        return result * sign

if __name__  == '__main__':
    import sys
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    result = rec_int_mult(x, y)
    print('{} * {} = {}'.format(x, y, result))
        
