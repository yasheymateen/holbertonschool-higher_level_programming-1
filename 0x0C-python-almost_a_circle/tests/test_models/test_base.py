#!/usr/bin/python3
"""Unittest module for class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests for class Base and its methods
    """
    def setUp(self):
        self.a = Base()  # id is 1
        self.b = Base(98)
        self.c = Base(None)  # id is 2
        self.d = Base(-1)
        self.e = Base("hi")
        self.f = Base([1, 2])
        self.x = {"hi": 0, "hello": 1}
        self.g = Base(self.x)

    def test_id(self):
        self.assertEqual(self.a.id, 1)
        self.assertEqual(self.b.id, 98)
        self.assertEqual(self.c.id, 2)
        self.assertEqual(self.d.id, -1)
        self.assertEqual(self.e.id, "hi")
        self.assertEqual(self.f.id, [1, 2])
        self.assertEqual(self.g.id, self.x)

    def test_id_fail(self):
        self.assertNotEqual(self.a.id, 1)

if __name__ == '__main__':
    unittest.main()
