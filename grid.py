from point import Point
import heuristics

# File: grid.py
# Author: Nathan Robertson
# Purpose: Encapsulate a series of points which form a 2D grid


class Grid:
    def __init__(self, empasses, min_point, max_point):
        self.impasses = empasses
        self.max_point = max_point
        self.min_point = min_point

    def neighbors(self, point):
        """ Return adjacent points of a point """
        raw_neighbors = [self.up(point), self.down(point), self.left(point), self.right(point), self.lower_left(point),
                         self.lower_right(point), self.upper_left(point), self.upper_right(point)]
        return list(filter(None.__ne__, raw_neighbors))

    def up(self, point):
        x, y = point
        return self.make_point((x, y + 1))

    def upper_left(self, point):
        x, y = point
        return self.make_point((x - 1, y + 1))

    def upper_right(self, point):
        x, y = point
        return self.make_point((x + 1, y + 1))

    def down(self, point):
        x, y = point
        return self.make_point((x, y - 1))

    def lower_left(self, point):
        x, y = point
        return self.make_point((x - 1, y - 1))

    def lower_right(self, point):
        x, y = point
        return self.make_point((x + 1, y - 1))

    def left(self, point):
        x, y = point
        return self.make_point((x - 1, y))

    def right(self, point):
        x, y = point
        return self.make_point((x + 1, y))

    def make_point(self, new_point):
        if self.in_grid_range(new_point) and not self.is_impasse(new_point):
            return new_point
        return None

    def is_impasse(self, point):
        if point in self.impasses:
            return True
        return False

    def in_grid_range(self, point):
        return self.min_point <= point < self.max_point
