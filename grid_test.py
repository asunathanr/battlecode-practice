import unittest
from grid import Grid
from point import Point

class GridTest(unittest.TestCase):

    def setUp(self):
        self.grid = Grid([], Point(0, 0), Point(10, 10))

    def test_in_grid_range(self):
        self.assertTrue(self.grid.in_grid_range(Point(0, 0)))
        self.assertFalse(self.grid.in_grid_range(Point(-1, 0)))
        self.assertTrue(self.grid.in_grid_range(Point(5, 5)))

    def test_neighbors(self):
        neighbors = list(self.grid.neighbors(Point(1, 1)))
        self.assertEqual([Point(0, 1), Point(1, 0)], neighbors)