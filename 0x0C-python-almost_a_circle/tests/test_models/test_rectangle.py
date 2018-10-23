#!/usr/bin/python3
"""Unittest module for class Rectangle
"""
import unittest
import os
import io
import sys
import json
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests for class Rectangle and its methods
    """
    def setUp(self):
        """setUp for each test method"""
        self.a = Rectangle(2, 3)  # id is 1
        self.b = Rectangle(4, 5, 1, 1, 10)  # id is 10

    def tearDown(self):
        """Reset counter to 0 for each test method"""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """test for inheritance"""
        self.assertIsInstance(self.a, Base)

    def test_not_inheritance(self):
        """test for not inheritance"""
        self.assertNotIsInstance(Base, Rectangle)

    def test_id(self):
        """test for id"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 10)

    def test_width(self):
        """test for width"""
        self.assertEqual(self.a.width, 2)
        self.assertEqual(self.b.width, 4)
        self.assertRaises(TypeError, self.a.width, "2")
        self.assertRaises(TypeError, self.a.width, [1, 2])
        self.assertRaises(TypeError, self.a.width, {"hello": 1})
        with self.assertRaises(ValueError):
            self.a.width = 0
        with self.assertRaises(ValueError):
            self.a.width = -1

    def test_height(self):
        """test for height"""
        self.assertEqual(self.a.height, 3)
        self.assertEqual(self.b.height, 5)
        self.assertRaises(TypeError, self.a.height, "2")
        self.assertRaises(TypeError, self.a.height, [1, 2])
        self.assertRaises(TypeError, self.a.height, {"hello": 1})
        with self.assertRaises(ValueError):
            self.a.height = 0
        with self.assertRaises(ValueError):
            self.a.height = -1

    def test_x(self):
        """test for x"""
        self.assertEqual(self.a.x, 0)
        self.a.x = 2
        self.assertEqual(self.a.x, 2)
        self.assertEqual(self.b.x, 1)
        self.assertRaises(TypeError, self.a.x, "2")
        with self.assertRaises(ValueError):
            self.a.x = -1

    def test_y(self):
        """test for y"""
        self.assertEqual(self.a.y, 0)
        self.assertEqual(self.b.y, 1)
        self.assertRaises(TypeError, self.a.y, "2")
        with self.assertRaises(ValueError):
            self.a.y = -1

    def test_exceptions(self):
        """test exceptions"""
        self.assertRaises(TypeError, Rectangle, "1", 1)
        self.assertRaises(TypeError, Rectangle, 1, "2")
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")
        self.assertRaises(ValueError, Rectangle, -1, 0)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, -2)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(TypeError, Rectangle, 1, 1, [1])
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(self.a.area(), 6)
        self.assertEqual(self.b.area(), 20)
        self.assertNotEqual(self.a.area(), 9)

    def test_display(self):
        """test display method"""
        a_output = io.StringIO()
        b_output = io.StringIO()
        sys.stdout = a_output
        self.a.display()
        a_expected_output = """##\n##\n##\n"""
        self.assertEqual(a_expected_output, a_output.getvalue())

        sys.stdout = b_output
        self.b.display()
        b_expected_output = """\n ####\n ####\n ####\n ####\n ####\n"""
        self.assertEqual(b_expected_output, b_output.getvalue())
        sys.stdout = sys.__stdout__

    def test_str_method(self):
        """test __str__ magic method"""
        a_expected_output = "[Rectangle] (1) 0/0 - 2/3\n"
        b_expected_output = "[Rectangle] (10) 1/1 - 4/5\n"
        a_output = io.StringIO()
        b_output = io.StringIO()
        sys.stdout = a_output
        print(self.a)
        self.assertEqual(a_expected_output, a_output.getvalue())
        sys.stdout = b_output
        print(self.b)
        self.assertEqual(b_expected_output, b_output.getvalue())
        sys.stdout = sys.__stdout__

    def test_update_0(self):
        """test method update()"""
        self.b.update(89)
        output = io.StringIO()
        sys.stdout = output
        print(self.b)
        expected = "[Rectangle] (89) 1/1 - 4/5\n"
        self.assertEqual(expected, output.getvalue())

        self.b.update(89, 2)
        output = io.StringIO()
        sys.stdout = output
        print(self.b)
        expected = "[Rectangle] (89) 1/1 - 2/5\n"
        self.assertEqual(expected, output.getvalue())

        self.b.update(89, 2, 3)
        output = io.StringIO()
        sys.stdout = output
        print(self.b)
        expected = "[Rectangle] (89) 1/1 - 2/3\n"
        self.assertEqual(expected, output.getvalue())

        self.b.update(89, 2, 3, 4)
        output = io.StringIO()
        sys.stdout = output
        print(self.b)
        expected = "[Rectangle] (89) 4/1 - 2/3\n"
        self.assertEqual(expected, output.getvalue())

        self.b.update(89, 2, 3, 4, 5)
        output = io.StringIO()
        sys.stdout = output
        print(self.b)
        expected = "[Rectangle] (89) 4/5 - 2/3\n"
        self.assertEqual(expected, output.getvalue())

    def test_update_1(self):
        """test updated method update()"""
        r1 = Rectangle(10, 10, 10, 10, 1)

        r1.update(height=1)
        output = io.StringIO()
        sys.stdout = output
        print(r1)
        expected = "[Rectangle] (1) 10/10 - 10/1\n"
        self.assertEqual(expected, output.getvalue())

        r1.update(width=1, x=2)
        output = io.StringIO()
        sys.stdout = output
        print(r1)
        expected = "[Rectangle] (1) 2/10 - 1/1\n"
        self.assertEqual(expected, output.getvalue())

        r1.update(y=1, width=2, x=3, id=89)
        output = io.StringIO()
        sys.stdout = output
        print(r1)
        expected = "[Rectangle] (89) 3/1 - 2/1\n"
        self.assertEqual(expected, output.getvalue())

        r1.update(x=1, height=2, y=3, width=4)
        output = io.StringIO()
        sys.stdout = output
        print(r1)
        expected = "[Rectangle] (89) 1/3 - 4/2\n"
        self.assertEqual(expected, output.getvalue())

        r1.update(88, x=1, height=2)
        output = io.StringIO()
        sys.stdout = output
        print(r1)
        expected = "[Rectangle] (88) 1/3 - 4/2\n"
        self.assertEqual(expected, output.getvalue())

    def test_to_dictionary(self):
        """test public method to_dictionary"""
        to_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0}
        self.assertDictEqual(to_dict, self.a.to_dictionary())
        to_dict = {'id': 10, 'width': 4, 'height': 5, 'x': 1, 'y': 1}
        self.assertDictEqual(to_dict, self.b.to_dictionary())

    def test_to_json_string(self):
        """test public method to_json_string"""
        dictionary = self.a.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(Base.to_json_string([dictionary]),
                         json.dumps([dictionary]))

    def test_save_to_file(self):
        Rectangle.save_to_file([self.a, self.b])
        with open("Rectangle.json", "r", encoding="utf8") as f:
            json_objs = f.read()
        list_of_dicts = json.loads(json_objs)
        self.assertDictEqual(list_of_dicts[0], self.a.to_dictionary())
        self.assertDictEqual(list_of_dicts[1], self.b.to_dictionary())

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf8") as f:
            json_objs = f.read()
        empty_list = json.loads(json_objs)
        self.assertEqual(empty_list, [])

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf8") as f:
            json_objs = f.read()
        empty_list = json.loads(json_objs)
        self.assertEqual(empty_list, [])

    def test_from_json_string(self):
        Rectangle.save_to_file([self.a, self.b])
        with open("Rectangle.json", "r", encoding="utf8") as f:
            json_objs = f.read()
        list_of_dicts = Rectangle.from_json_string(json_objs)
        self.assertDictEqual(list_of_dicts[0], self.a.to_dictionary())
        self.assertDictEqual(list_of_dicts[1], self.b.to_dictionary())

        empty_list = Rectangle.from_json_string(None)
        self.assertEqual(empty_list, [])

        empty_list = Rectangle.from_json_string("")
        self.assertEqual(empty_list, [])

    def test_create(self):
        a_dict = {'id': 98}
        expected = {'id': 98, 'height': 1, 'width': 1, 'x': 0, 'y': 0}
        rect = Rectangle.create(**a_dict)
        self.assertDictEqual(rect.to_dictionary(), expected)

        a_dict = {'id': 98, 'height': 2}
        expected = {'id': 98, 'height': 2, 'width': 1, 'x': 0, 'y': 0}
        rect = Rectangle.create(**a_dict)
        self.assertDictEqual(rect.to_dictionary(), expected)

        a_dict = {'id': 98, 'height': 2, 'width': 3}
        expected = {'id': 98, 'height': 2, 'width': 3, 'x': 0, 'y': 0}
        rect = Rectangle.create(**a_dict)
        self.assertDictEqual(rect.to_dictionary(), expected)

        a_dict = {'id': 98, 'height': 2, 'width': 3, 'x': 1}
        expected = {'id': 98, 'height': 2, 'width': 3, 'x': 1, 'y': 0}
        rect = Rectangle.create(**a_dict)
        self.assertDictEqual(rect.to_dictionary(), expected)

        a_dict = {'id': 98, 'height': 2, 'width': 3, 'x': 1, 'y': 1}
        expected = {'id': 98, 'height': 2, 'width': 3, 'x': 1, 'y': 1}
        rect = Rectangle.create(**a_dict)
        self.assertDictEqual(rect.to_dictionary(), expected)

    def test_load_from_file(self):
        os.remove("Rectangle.json")
        empty = Rectangle.load_from_file()
        self.assertEqual([], empty)

        Rectangle.save_to_file([self.a])
        list_dict = Rectangle.load_from_file()
        self.assertDictEqual(list_dict[0].to_dictionary(),
                             self.a.to_dictionary())

if '__name__' == '__main__':
    unittest.main()
