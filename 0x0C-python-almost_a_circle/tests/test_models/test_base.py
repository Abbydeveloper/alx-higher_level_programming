#!/usr/bin/python3
"""Define unittests for base.py"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test fo rinistantiation of the Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """Check for Id"""

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

    def test_type_and_instance(self):
        """Test for type and instance"""

        base_5 = Base()
        self.assertEqual(type(base_5), Base)
        self.assertTrue(isinstance(base_5, Base))

    def test_join_string(self):
        """Test to_json_string method"""

        attr_dict = {'x': 4, 'y': 9, 'width': 10, 'height': 9, 'id':1}
        json_d = Base.to_json_string([attr_dict])
        self.assertTrue(isinstance(attr_dict, dict))
        self.assertTrue(isinstance(json_d, str))

        json_d_1 = Base.to_json_string([])
        self.assertEqual(json_d_1, '[]')
        json_d_2 = Base.to_json_string(None)
        self.assertEqual(json_d_1, '[]')
