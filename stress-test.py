import astar
import random
from grid import Grid
from heuristics import *
import timeit


def gen_grid(rows, cols) -> Grid:
    return Grid(gen_impasses(rows, cols, 5), (0, 0), (rows, cols))


def gen_impasses(rows, cols, chance):
    impasses = []
    for i in range(1, rows):
        for j in range(1, cols):
            if is_impass(chance):
                impasses.append((i, j))
    return impasses


def is_impass(chance) -> bool:
    return random.randint(0, 100) < chance


rows = 50
cols = 50
grid = gen_grid(rows, cols)

neighbors_fn = grid.neighbors

start = (0, 0)
goal = (rows - 1, cols - 1)
print(timeit.timeit(lambda: (astar.find_path(start, goal, neighbors_fn, heuristic_cost_estimate_fnct=diagonal)), number=10))
