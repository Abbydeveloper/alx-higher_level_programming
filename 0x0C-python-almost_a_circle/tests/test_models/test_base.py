#!/usr/bin/python3
"""Define unittests for base.py"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Test fo rinistantiation of the Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        base_0 = Base()
        self.assertEqual(base_0.id, 1)

        base_1 = Base()
        self.assertEqual(base_1.id, 2)

        base_2 = Base(12)
        self.assertEqual(base_2.id, 12)

        base_3 = Base(0)
        self.assertEqual(base_3.id, 0)

        base_4 = Base(-5)
        self.assertEqual(base_4.id, -5)
