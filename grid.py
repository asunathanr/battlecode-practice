# File: grid.py
# Author: Nathan Robertson
# Purpose: Encapsulate a series of points which form a 2D grid. Is a sparse grid so only impasses are stored.


class Grid:
    def __init__(self, impasses, min_point, max_point):
        self.impasses = impasses
        self.max_point = max_point
        self.min_point = min_point

    def manhattan_neighbors(self, point):
        """
        :param point: A tuple (x, y)
        :return: Valid neighbors in point that are (up, left, right, and down) from point
        """
        raw_neighbors = [self.up(point), self.down(point), self.left(point), self.right(point)]
        # Source: https://stackoverflow.com/questions/16096754/remove-none-value-from-a-list-without-removing-the-0-value
        return list(filter(None.__ne__, raw_neighbors))

    def neighbors(self, point):
        """
        Return adjacent points of a point. Excludes out-of-bounds points and impasses
        """
        raw_neighbors = self.manhattan_neighbors(point) + \
                        [self.lower_right(point), self.lower_left(point), self.upper_right(point), self.upper_left(point)]
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
