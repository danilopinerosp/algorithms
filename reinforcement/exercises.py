#!/usr/bin/env python

from random import randrange

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

def own_choice(data):
    """ Return a random element from a non-empty sequence. """
    if not len(data):
        raise TypeError("Empty sequence.")
    idx = randrange(0, len(data))
    return data[idx]

if __name__ == '__main__':

    data = [1, 3, 5, 2, 7, 'hola', 'nana']
    dat = []
    print(own_choice(dat))
    for i in range(5):
        print(own_choice(data))
    
