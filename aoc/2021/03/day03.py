"""IN PROGRESS | Day 3: Binary Diagnostic"""

import numpy as np


def parse(puzzle_input):
    """Parse input"""

    data = []

    for line in puzzle_input.splitlines():
        input_line = []
        for c in list(line):
            input_line.append(int(c))
        data.append(input_line)

    return data


def part1(data):
    """Solve part 1"""

    bits_ = np.array(data).astype(int)
    column_sums = bits_.sum(axis=0)

    binaries_gamma = ['1' if b > 500 else '0' for b in column_sums]
    gamma = int(''.join(binaries_gamma), 2)

    binaries_epsilon = ['1' if b <= 500 else '0' for b in column_sums]
    epsilon = int(''.join(binaries_epsilon), 2)

    result = gamma * epsilon
    return result


def part2(data):
    """Solve part 2"""
    return None


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2
