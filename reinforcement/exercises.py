#!/usr/bin/env python

def is_multiple(n, m):
    """ Return True if n is a multiple of m, and False otherwise. """
    if n % m == 0:
        return True
    return False

def is_even(k):
    """ Return True if k is even, and False otherwise. """
    result = False
    for i in range(k + 1):
        if result == False:
            result = True
        else:
            result = False
    return result

def minmax(data):
    """ Return the smallest and largest numbers of data in the form of a tuple o length two. """
    minimum = None
    maximum = None
    for i in data:
        if minimum == None or i < minimum:
            minimum = i
        elif maximum == None or i > maximum:
            maximum = i
    return minimum, maximum

def sum_squares(n):
    """ Return the sum of the squares of all the positive integers smaller than n."""
    return sum([i * i for i in range(n)])

def sum_squares_odd(n):
    """ Return the sum of the squares of all the odd positive integers smaller than n. """
    return sum([i * i  for i in range(n) if i % 2 != 0])

if __name__ == '__main__':
    a = [1, 3, 4, 5, -7, 4]
    b = [5, 6, 100, 100, -6, -1000]
    print(minmax(a))
    print(minmax(b))

    for i in range(10):
        print(sum_squares_odd(i))
    
