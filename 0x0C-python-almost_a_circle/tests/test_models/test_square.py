#!/usr/bin/python3

"""Defines tests for the Square class"""

import io
import contextlib
import unittest
from models.base import Base
from models.square import Square


class Test_Square(unittest.TestCase):
    """Unittests for the Square class"""

    def test_square(self):
        """All tests for the Square class"""

        self.assertIsInstance(Square(10), Base)

        with self.assertRaises(TypeError):
            Square()

        sq1 = Square(10)
        sq2 = Square(3)
        self.assertEqual(sq1.id, sq2.id)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('Hi')
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3)
        with self.assereRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, 'Hello', 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -2, 2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 4, 'Hi')
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 4, -2)


        """Test area method"""

        sq = Square(10)
        self.assertEqual(sq.area(), 100)

        sq = Square(20, 3, 2)
        self.assertEqual(sq.area(), 400)

        """Test __str__ method"""
        f = io.StringIO()
        sq = Square(3, 4, 2, 5)
        with contextlib.redirect_stdout(f):
            print(sq)
        string = f.getvalue()
        response = "[Square] {5} 4/2 - 3\n"
        self.assertEqual(response, string)

        """Test display method"""

        f = io.StringIO()
        sq = Square(3)
        with contextlib.redirect_stdout(f):
            sq.display()
        string = f.getvalue()
        response = "###\n###\n###\n"
        self.assertEqual(response, string)

        """Test update method"""
        sq = Square(12)
        sq.update(3)
        self.assertEqual(3, sq.id)
        sq.update(x=2)
        self.assertEqual(2, sq.x)
        sq.update(size= 8, y=5)
        self.assertEqual(5, sq.y)
        self.assertEqual(8, sq.size)
        sq.update()
        self.assertEqual(3, sq.id)
        self.assertEqual(2, sq.x)
        self.assertEqual(8, sq.size)
        self.assertEqual(5, sq.y)
