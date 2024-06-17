#!/usr/bin/python3
"""unittests for max_integer function"""

import unittest

max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer function"""

    def test_unordered_list(self):
        """Test for unordered list of intgers"""
        unordered = [4, 3, 6, 7]
        self.assertEqual(max_integer(unordered), 7)


    def test_ordered_list(self):
        """Test for ordered list of integers"""
        ordered = [ 3, 4, 6, 7]
        self.assertEqual(max_integer(ordered), 7)


    def test_empty_list(self):
        """Test for an empty list"""
        empty_list  = []
        self.assertEqual(max_integer(empty_list), None)


    def test_mas_at_beginning(self):
        """Test for max integer at beginning of list"""
        max_at_beginning = [7, 4, 3, 6]
        self.assertEqual(max_integer(max_at_beginning), 7)

    def test_list_with_one_element(self):
        """Test for list with only one element"""
        list_with_one_element = [5]
        self.assertEqual(max_integer(list_with_one_element), 5)


    def test_floating_numbers(self):
        """Test for floating numbers"""
        floating_numbers = [3.0, 2.8, 4.8, 2.1]
        self.assertEqual(max_integer(floating_numbers), 4.8)


    def test_negative_numbers_only(self):
        """Test for negative numbers"""
        negative_numbers_only = [-3, -2, -5, -8]
        self.assertEqual(max_integer(negative_numbers_only), -2)


if __name__ == '__main__':
    unittest.main()
