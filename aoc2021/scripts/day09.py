"""Day 9: Smoke Basin"""

import pathlib
import sys

import numpy as np
from itertools import product


# Set Input
input_ex = """2199943210
3987894921
9856789892
8767896789
9899965678"""

puzzle_input = input_ex


def parse(puzzle_input):
    """Parse input"""

    data = np.array([[int(x) for x in list(col)] for col in puzzle_input.splitlines()])
    return data



def part1(data):
    """Solve part 1"""

    low_values = [
        data[r, c]
        for r,c in product(*map(range, data.shape))
        if data[r, c] == data[max(0, r-1):r+2,max(0, c-1):c+2].min()
        ]

    result = sum(np.array(low_values) + 1)
    return result


def measure_basin(r, c, zone=[], m=data):
    """Measure of a basin with recursive call of adjacent points"""

    if m[r, c] < 9 and [r, c] not in zone:
        zone.append([r, c])

        adjacents = [
            [min(r+1, (len(m)-1)), c],
            [max(0,r-1), c],
            [r, min(c+1, (len(m[0])-1))],
            [r, max(0,c-1)]
        ]
        for position in adjacents:
            measure_basin(position[0], position[1], zone)

    return zone


def part2(data):
    """Solve part 2"""

    low_points = [
        [r, c]
        for r,c in product(*map(range, data.shape))
        if data[r, c] == data[max(0, r-1):r+2, max(0, c-1):c+2].min()
        ]

    sizes = []
    for point in low_points:
        basin = measure_basin(point[0], point[1], zone=[])
        sizes.append(len(basin))

    result = np.prod(sorted(sizes, reverse= True)[:3])
    return result


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
