#!/usr/bin/env python3

import unittest
from karatsuba import karatsuba_multiplication

class TestKaratsuba(unittest.TestCase):

    def test_single_digits(self):
        expected = 30
        self.assertEqual(karatsuba_multiplication(6, 5), expected)

    def test_different_digits(self):
        expected = 6000
        self.assertEqual(karatsuba_multiplication(40, 150), expected)

    def test_negative_numbers(self):
        expected = -150
        self.assertEqual(karatsuba_multiplication(-15, 10), expected)

    def test_multiple_digits(self):
        expected = 12040974
        self.assertEqual(karatsuba_multiplication(4698, 2563), expected)

    def test_one_number(self):
        expected = 0
        self.assertEqual(karatsuba_multiplication(4565), expected)

    def test_large_numbers_zeros(self):
        expected = 1003250720050501
        self.assertEqual(karatsuba_multiplication(100020001, 10030501), expected)

    def test_large_same_size(self):
        expected = 50540736961471275
        self.assertEqual(karatsuba_multiplication(345345345, 146348395), expected)

    def test_large_different_size(self):
        expected = 60118107496
        self.assertEqual(karatsuba_multiplication(7655432, 7853), expected)
        

unittest.main()
