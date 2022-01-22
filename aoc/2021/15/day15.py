"""Day 15: Chiton"""

import pathlib
import sys

import numpy as np

# Get Input
INPUT_EX = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


# Set Input
puzzle_input = INPUT_EX

# Format Input
def parse_input(puzzle_input):
    """Parse input"""

    data = np.array([
        [int(x) for x in list(col)] for col in puzzle_input.splitlines()
    ])
    return data


data = parse_input(puzzle_input)




def part1(data):
    """Solve part 1"""

    return None


def part2(data):
    """Solve part 2"""

    return None


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_input(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2
