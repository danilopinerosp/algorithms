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

def own_reverse(data):
    """ Return the integers of data in reverse order. """
    reverse_list = []
    for i in range(len(data) - 1, -1, -1):
        reverse_list.append(data[i])
    return reverse_list

def pair_odd_product(data):
    """ Return True if there is distinct pair of values in the sequence whose product is odd, and False otherwise.. """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if (data[i] * data[j]) % 2 != 0:
                return True
    return False

def distinct_numbers(data):
    """ Return True if all the numbers in the sequence data are different from each other, and False otherwise. """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return False
    return True

if __name__ == '__main__':

    d = [1, 2, 3, 4, 5, 2]
    c = [2, 4, 6]
    print(distinct_numbers(d))
    print(distinct_numbers(c))
    
    
