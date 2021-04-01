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
    x = str(x)
    y = str(y)
    size_x = len(str(x))
    size_y = len(str(y))


    n = max(size_x, size_y)
    if n % 2 != 0 and n != 1: # Evaluate if n not even and different to 1
        n = n + 1             # make n even

    #  Add 0's to the left to make both numbers (x, y) the same size
    x = '0' * (n - size_x) + x 
    y = '0' * (n - size_y) + y

    if size_x == 1 or size_y == 1:   #  Base case
        return int(x) * int(y)
    else:                           # Recursive case
        
        a = int(x[: n // 2]) # First half of x
        b = int(x[n // 2 : ])  # Second half of x
        c = int(y[: n // 2])    # First half of y
        d = int(y[n // 2 :]) # Second half of y
        
        p = a + b
        q = c + d
        
        ac = karatsuba_multiplication(a, c)  # Recursive call for a * c
        bd = karatsuba_multiplication(b, d)  # Recursive call for b * d
        pq = karatsuba_multiplication(p, q)  # Recursive call for p * q
        
        adbc = pq - ac - bd
        
        result =  (10 ** n) * ac + (10 ** (n // 2)) * adbc + bd
        return result * sign   # Return result with respective sign


if __name__ == '__main__':
    
    import sys

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    result = karatsuba_multiplication(x, y)
    print('{} * {} = {}'.format(x, y, result))
    

