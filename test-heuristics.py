import unittest
from heuristics import *
from point import Point


class HeuristicTest(unittest.TestCase):
    def setUp(self):
        self.start = Point(0, 0)
        self.end = Point(10, 10)

    def test_manhattan(self):
        self.assertEqual(20, manhattan(self.start, self.end))

    def test_diagonal(self):
        self.assertEqual(10, diagonal(self.start, self.end))