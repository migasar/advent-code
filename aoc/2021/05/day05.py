"""Day 5: Hydrothermal Venture"""

import numpy as np
import parse


# Set Input
input_ex = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

puzzle_input = input_ex


def parse(puzzle_input):
    """Transform raw input in list of dict of coordinates"""

    lines = puzzle_input.splitlines()
    coords = []
    pattern = "{x1:d},{y1:d} -> {x2:d},{y2:d}"

    for line in lines:
        match = parse.search(pattern, line)
        coords.append(match.named)

    return coords


def part1(coords):
    """Solve part 1
    Set a grid" and count overlaps of
    (vertical and horizontal) segments on that grid
    """

    grid = np.zeros((len(coords), len(coords)), dtype=int)

    for line in coords:
        if line['x1'] == line['x2']:
            y = [line['y1'], line['y2']]
            for i in range(min(y), max(y)+1):
                grid[i, line['x1']] += 1

        if line['y1'] == line['y2']:
            x = [line['x1'], line['x2']]
            for i in range(min(x), max(x)+1):
                grid[line['y1'], i] += 1

    overlaps = grid[grid >= 2]
    return overlaps


def part2(coords):
    """Solve part 2
    Set a grid and count overlaps of
    (vertical, horizontal and diagonal) segments on that grid
    """

    grid = np.zeros((len(coords), len(coords)), dtype=int)

    for line in coords:
        if line['x1'] == line['x2']:
            y = [line['y1'], line['y2']]
            for i in range(min(y), max(y)+1):
                grid[i, line['x1']] += 1
        if line['y1'] == line['y2']:
            x = [line['x1'], line['x2']]
            for i in range(min(x), max(x)+1):
                grid[line['y1'], i] += 1

        if abs(line['x1'] - line['x2']) == abs(line['y1'] - line['y2']):
            if line['x1'] < line['x2']:
                abs_ = np.arange(line['x1'], line['x2']+1)
            else:
                abs_ = np.arange(line['x2'], line['x1']+1)
                abs_ = abs_[::-1]
            if line['y1'] < line['y2']:
                ord_ = np.arange(line['y1'],line['y2']+1)
            else:
                ord_ = np.arange(line['y2'], line['y1']+1)
                ord_ = ord_[::-1]

            segment = np.stack((abs_, ord_), axis=-1)
            for s in segment:
                grid[s[1], s[0]] += 1

    overlaps = grid[grid >= 2]
    return overlaps


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2
