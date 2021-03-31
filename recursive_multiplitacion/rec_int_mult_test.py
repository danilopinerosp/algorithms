#!/usr/bin/env python3

import unittest
from rec_int_mult import rec_int_mult

class TestRecIntMult(unittest.TestCase):

    def test_single_digist(self):
        expected = 30
        self.assertEqual(rec_int_mult(6, 5), expected)

    def test_different_digits(self):
        expected = 6000
        self.assertEqual(rec_int_mult(40, 150), expected)

    def test_negative_numbers(self):
        expected = -150
        self.assertEqual(rec_int_mult(-15, 10), expected)

    def test_multiple_digits(self):
        expected = 12040974
        self.assertEqual(rec_int_mult(4698, 2563), expected)

    def test_one_number(self):
        expected = 0
        self.assertEqual(rec_int_mult(4565), expected)

    def test_large_numbers_zeros(self):
        expected = 1003250720050501
        self.assertEqual(rec_int_mult(100020001, 10030501), expected)

    def test_large_same_size(self):
        expected = 50540736961471275
        self.assertEqual(rec_int_mult(345345345, 146348395), expected)

    def test_large_different_size(self):
        expected = 60118107496
        self.assertEqual(rec_int_mult(7655432, 7853), expected)
    

unittest.main()
