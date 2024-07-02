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


        """Test with wrong types"""
        with self.assertRaises(TypeError) as x:
            Base.to_json_string()
        self.assertEqual(
             "to_json_string() missing 1 required positional argument: 'list_dictionaries'", str(x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(8)
        self.assertEqual(
             'list_dictionaries must be a list of dictionaries', str(x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string('Hello')
        self.assertEqual(
             'list_dictionaries must be a list of dictionaries', str(x.exception))
        with self.assertRaises(TypeError) as x:
            Base.to_json_string(['Hola', 'Como estas'])
        self.assertEqual(
             'list_dictionaries must be a list of dictionaries', str(x.exception))

    def test_from_json_strong(self):
        """Test from_json_string method"""

        list_1 = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 10, 'width': 1, 'height': 8}
                ]
        json_list_input = Rectangle.to_json_string(list_1)
        list_output = Rectangle.from_json_string(json_list_input)
        response = [{'width': 10, 'height': 4, 'id': 89},
                    {'width': 1, 'height': 8, 'id': 10}]
        self.assertCountEqual(list_output, response)
        self.assertEqual(type(list_output), list)

        list_output_1 = Rectangle.from_json_string('')
        self.assertEqual(list_output_1, [])

        list_output_2 = Rectangle.from_json_string(None)
        self.assertEqual(list_output_2, [])

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""

        rect0 = Rectangle(10, 7, 2, 8)
        rect1 = Rectangle(2, 4)
        Rectangle.save_to_file([rect0, rect1])
        response = ('[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},' +
                    ' {"y": 0, "x": 0, "id": 12, "width": 2, "height": 4}]')
        with open("Rectangle.json", mode="r") as f:
            self.assertEqual(len(f.read()), len(response) - 1)
        Rectangle.save_to_file(None)
        response = "[]"
        with open("Rectangle.json", mode="r") as f:
            self.assertEqual(f.read(), response)
        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as f:
            self.assertEqual(f.read(), response)
        square0 = Square(9, 3, 1, 12)
        square1 = Square(6, 7)
        Square.save_to_file([square0, square1])
        response = ('[{"id": 12, "size": 9, "x": 3, "y": 1},' +
                ' {"id": 3, "size": 6, "x": 7, "y": 0}]')
        with open("Square.json", mode="r") as f:
            self.assertEqual(len(f.read()), len(response))
        Square.save_to_file(None)
        response = "[]"
        with open("Square.json", mode="r") as f:
            self.assertEqual(f.read(), response)
        os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", mode="r") as f:
            self.assertEqual(f.read(), response)
