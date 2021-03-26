#!/usr/bin/env python3

def merge(C, D):
    """ Take two sorted list C and D (length n/2 each) and
    return a sorted list B of length n. """
    i = 0
    j = 0
    n = len(C + D)
    B = []
    for k in range(n):
        if i >= len(C):
            B.append(D[j])
            j += 1
        elif j >= len(D):
            B.append(C[i])
            i += 1
        elif C[i] < D[j]:
            B.append(C[i])
            i += 1
        else:
            B.append(D[j])
            j += 1
    return B

def merge_sort(A):
    """ Return a list with the same integers sorted from smallest to largest"""
    if len(A) <= 1:
        return A
    else:
        n_2 = len(A) // 2
        C = merge_sort(A[:n_2])
        D = merge_sort(A[n_2:])
        return merge(C, D)


