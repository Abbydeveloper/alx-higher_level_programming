#!/usr/bin/python3
"""Defines unittests for the Rectangle class"""

import io
import contextlib
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
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(34, None)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -3, 0)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 2, 4, None, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 2, 4, -3, 5)


        """Test area method"""

        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)

        rect1 = Rectangle(10, 5)
        self.assertEqual(rect1.area(), 50)

        """Test __str__ Method"""

        f = io.StringIO()
        rect = Rectangle(4, 6, 2, 1, 12)
        with contextlib.redirect_stdout(f):
            print(rect)
        string = f.getvalue()
        response = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(response, string)

        """Test display method (without x and y, and without y also)"""

        f = io.StringIO()
        rect = Rectangle(2, 4, 3, 2, 0)
        with contextlib.redirect_stdout(f):
            rect.display()
        string = f.getvalue()
        response = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(string, response)

        f = io.StringIO()
        rect = Rectangle(5, 3)
        with contextlib.redirect_stdout(f):
            rect.display()
        string = f.getvalue()
        response = "#####\n#####\n#####\n"
        self.assertEqual(string, response)

        with self.assertRaises(TypeError) as x:
            rect = Rectangle(9, 6)
            rect.display(9)
        self.assertEqual(str(x.exception), 'display() takes 1 positional argument but 2 were given')

        """Test to_dictionary method"""

        rect = Rectangle(10, 2, 1, 9)
        """Test Update"""

        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual(89, rect.id)
        rect.update(89, 2)
        self.assertEqual(2, rect.width)
        rect.update(89, 2, 3)
        self.assertEqual(3, rect.height)
        rect.update(89, 2, 3, 4)
        self.assertEqual(4, rect.x)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual(5, rect.y)
        rect.update()
        self.assertEqual(str(rect), "[Rectangle] (89) 4/5 - 2/3")
        rect.update(width=1, height=2, x=3, y=4)
        self.assertEqual(1, rect.width)
        self.assertEqual(2, rect.height)
        self.assertEqual(3, rect.x)
        self.assertEqual(4, rect.y)
        """Test Rectangle.create()"""
