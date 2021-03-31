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

    #  Numver of digits of both numers (x, y)
    size_x = len(str(x))
    size_y = len(str(y))

    # Difference between the digits of both numbers
    delta = abs(size_x - size_y)

    n = max(size_x, size_y)

    if size_x == 1 or size_y == 1:
        return x * y
    else:
        a = x // 10 ** (size_x // 2)      # First half of x
        b = x - a * 10 ** ( size_x // 2)  # Second half of x
        c = y // 10 ** (size_y // 2)     # First half of y
        d = y - c * 10 ** (size_y // 2)   # Second half of y
        ac = rec_int_mult(a, c)
        ad = rec_int_mult(a, d)
        bc = rec_int_mult(b, c)
        bd = rec_int_mult(b, d)
        result = (10 ** (n - delta)) * ac + (10 ** (n // 2)) * (ad + bc) + bd
        return result * sign

if __name__  == '__main__':
    import sys
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    result = rec_int_mult(x, y)
    print('{} * {} = {}'.format(x, y, result))
        
