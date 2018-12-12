# File: a-star-package.py
# Author: Nathan Robertson
# Purpose: Demonstrate the a-star package in pip.

# astar implementation downloaded using pip
import astar
# A sparse grid which only cares about map boundaries and where an impasse is.
from grid import Grid
# "Guesses" as to the cheapest way to get from point A to point B
from heuristics import *

grid = Grid([(5, 5)], (0, 0), (11, 11))
start = (0, 0)
goal = (10, 10)
neighbors_fn = grid.neighbors

path = astar.find_path(start,
                       goal,
                       neighbors_fn,
                       heuristic_cost_estimate_fnct=diagonal)

for node in path:
    print(node)
