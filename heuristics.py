# File: heuristics.py
# Author: Nathan Robertson
# Purpose: Different heuristics for estimating best paths on a grid.


def manhattan(current: (int, int), goal: (int, int)):
    """
    Use this heuristic when you can move in just four directions (up, down, left, right)
    To move from current to goal without diagonals one must traverse x distance and y distance.
    """
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def diagonal(current: (int, int), goal: (int, int)):
    """
    Use this heuristic when you can move in eight directions:
     (up, down, left, right, upper-left, upper-right, lower-left, lower-right)
    """
    return max(
        abs(current[0] - goal[0]),
        abs(current[1] - goal[1])
    )
