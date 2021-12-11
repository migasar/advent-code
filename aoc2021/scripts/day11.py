"""Day 11: Dumbo Octopus"""

import pathlib
import sys

import numpy as np


# Set Input
input_ex = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

puzzle_input = input_ex


def parse(puzzle_input):
    """Parse input"""

    data = np.array([
        [int(x) for x in list(col)] for col in puzzle_input.splitlines()
        ])
    return data


def part1(data, step=100):
    """Solve part 1"""

    flashes = 0
    grid = np.copy(data)

    for _ in range(step):
        grid += 1

        while [z for z in zip(*np.where(grid > 9))] != []:
            mob = [z for z in zip(*np.where(grid > 9))]

            for flash in mob:
                flashes += 1
                grid[flash] = 0
                row, col = flash
                adjacents = [
                    # row + 1
                    [min(row+1, (len(grid)-1)), min(col+1, (len(grid[0])-1))],
                    [min(row+1, (len(grid)-1)), col],
                    [min(row+1, (len(grid)-1)), max(0,col-1)],
                    # row
                    [row, min(col+1, (len(grid[0])-1))],
                    [row, max(0,col-1)],
                    # row - 1
                    [max(0,row-1), min(col+1, (len(grid[0])-1))],
                    [max(0,row-1), col],
                    [max(0,row-1), max(0,col-1)]
                ]

                for adj in list(set(tuple(a) for a in adjacents)):
                    if grid[adj] == 0:
                        continue
                    else:
                        grid[adj] += 1

    return flashes


def part2(data):
    """Solve part 2"""

    steps = 0
    grid = np.copy(data)

    while not np.all(grid == 0):
        steps += 1
        grid += 1

        while [z for z in zip(*np.where(grid > 9))] != []:
            mob = [z for z in zip(*np.where(grid > 9))]

            for flash in mob:
                grid[flash] = 0
                row, col = flash
                adjacents = [
                    # row + 1
                    [min(row+1, (len(grid)-1)), min(col+1, (len(grid[0])-1))],
                    [min(row+1, (len(grid)-1)), col],
                    [min(row+1, (len(grid)-1)), max(0,col-1)],
                    # row
                    [row, min(col+1, (len(grid[0])-1))],
                    [row, max(0,col-1)],
                    # row - 1
                    [max(0,row-1), min(col+1, (len(grid[0])-1))],
                    [max(0,row-1), col],
                    [max(0,row-1), max(0,col-1)]
                ]

                for adj in list(set(tuple(a) for a in adjacents)):
                    if grid[adj] == 0:
                        continue
                    else:
                        grid[adj] += 1

    return steps


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
