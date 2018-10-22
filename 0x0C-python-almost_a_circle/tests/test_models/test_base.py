#!/usr/bin/python3
"""Unittest module for class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests for class Base and its methods
    """
    def setUp(self):
        """Set up method"""
        self.a = Base()  # id is 1
        self.b = Base(98)
        self.c = Base(None)  # id is 2
        self.d = Base(-1)
        self.e = Base("hi")
        self.f = Base([1, 2])
        self.x = {"hi": 0, "hello": 1}
        self.g = Base(self.x)

    def tearDown(self):
        """Tear down method"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """test id"""
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 98)
        self.assertEqual(self.c.id, 2)
        self.assertEqual(self.d.id, -1)
        self.assertEqual(self.e.id, "hi")
        self.assertEqual(self.f.id, [1, 2])
        self.assertEqual(self.g.id, self.x)

    def test_id_fail(self):
        """test id fail"""
        self.assertNotEqual(self.c.id, 1)

if __name__ == '__main__':
    unittest.main()
