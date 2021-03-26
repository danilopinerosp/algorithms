#!/usr/bin/env python3

from merge_sort import merge_sort
import unittest

class TestMergeSorte(unittest.TestCase):
    def test_even(self):
        testcase = [3, 4, 0, 1, 7, 2]
        expected = [0, 1, 2, 3, 4, 7]
        self.assertEqual(merge_sort(testcase), expected)

    def test_empty(self):
        testcase = []
        expected = []
        self.assertEqual(merge_sort(testcase), expected)

    def test_odd(self):
        testcase = [3, 2, 6, 1, 4]
        expected = [1, 2, 3, 4, 6]
        self.assertEqual(merge_sort(testcase), expected)

    def test_repeated(self):
        testcase = [1, 2, 1, 3, 3, 1]
        expected = [1, 1, 1, 2, 3, 3]
        self.assertEqual(merge_sort(testcase), expected)
        

unittest.main()
