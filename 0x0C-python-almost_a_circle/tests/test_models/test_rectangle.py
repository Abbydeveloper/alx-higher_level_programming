#!/usr/bin/python3
"""Defines unittests for the Rectangle class"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Unittests for the Rectangle class"""

    def test_rectangle(self):
        """All tests for the Rectangle class"""

        self.assertIsInstance(Rectangle(10, 3), Base)

        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(3)

        rect1= Rectangle(30, 24)
        rect2 = Rectangle(23, 12)
        self.assertEqual(rect1.id, rect2.id - 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(34, None)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -3, 0)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 2, 4, None)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 2, 4, -3)
