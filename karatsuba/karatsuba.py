#!/usr/bin/env python3

def karatsuba_multiplication(x, y = 0):
    """Return the multiplication between x and y using Karatsuba multiplication algorithm"""
    (sign_x, sign_y) = (1, 1)

    # Enable multiplication of negative numbers
    if x < 0:
        sign_x = -1
        x = x * sign_x
    if y < 0:
        sign_y = -1
        y = y * sign_y

    # Sign of the final result
    sign = sign_x * sign_y

    # Number of digits of both numbers (x, y)
    size_x = len(str(x))
    size_y = len(str(y))

    # Difference between the digits of both numbers
    delta = abs(size_x - size_y)
    
    n = max(size_x, size_y)
    
    if size_x == 1 or size_y == 1:   #  Base case
        return x * y
    else:                           # Recursive case
        
        a = x // 10 ** (size_x // 2)    # First half of x
        b = x - a * 10 ** (size_x // 2)  # Second half of x
        c = y // 10 ** (size_y // 2)    # First half of y
        d = y - c * 10 ** (size_y // 2) # Second half of y
        
        p = a + b
        q = c + d
        
        ac = karatsuba_multiplication(a, c)  # Recursive call for a * c
        bd = karatsuba_multiplication(b, d)  # Recursive call for b * d
        pq = karatsuba_multiplication(p, q)  # Recursive call for p * q
        
        adbc = pq - ac - bd
        
        result =  (10 ** (n - delta)) * ac + (10 ** (n // 2)) * adbc + bd
        return result * sign   # Return result with respective sign


if __name__ == '__main__':
    
    import sys

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    result = karatsuba_multiplication(x, y)
    print('{} * {} = {}'.format(x, y, result))
    

