import astar
import random
from grid import Grid
from heuristics import *
import time


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


rows = 100
cols = 100
grid = gen_grid(rows, cols)

neighbors_fn = grid.neighbors

start = (0, 0)
goal = (rows - 1, cols - 1)
start_time = time.clock()
path = astar.find_path(start, goal, neighbors_fn, heuristic_cost_estimate_fnct=diagonal)
end_time = time.clock() - start_time

print("Took ", end_time, " to generate path.")

print("Impasses at: ", grid.impasses)

for node in path:
    print(node)
