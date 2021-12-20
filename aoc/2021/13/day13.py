"""Day 13: Transparent Origami"""

import pathlib
import sys

import numpy as np
import parse


# Set Input
INPUT_EX_1 = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0"""

INPUT_EX_2="""fold along y=7
fold along x=5"""

puzzle_input_1 = INPUT_EX_1
puzzle_input_2 = INPUT_EX_2


def parse_dots(puzzle_input):
    """Parse input"""

    data = np.array([
        [int(x) for x in line.split(',')] for line in puzzle_input.splitlines()
        ])

    return data


def parse_folds(puzzle_input):
    """Parse input"""

    data = []
    fold_pattern = "fold along {axis}={number}"

    for line in puzzle_input.splitlines():
        fold_match = parse.search(fold_pattern, line)
        data.append([fold_match['axis'],
                     int(fold_match['number'])])

    return data


def part1(dots, folds):
    """Solve part 1"""

    # Find shape of board
    board = np.zeros((dots[:, 1].max() + 1, dots[:, 0].max() + 1), dtype=int)

    # Fill board with dots
    for x,y in dots:
        board[(y, x)] = 1

    # Split the board
    # Find the folder line
    fold = folds[0][1]

    # Fold on horizontal line
    if folds[0][0] == 'y':
        board_up = board[:fold].copy()
        board_down = board[fold+1:].copy()
        new_board = board_up + np.flip(board_down, 0)

    # Fold on vertical line:
    else:
        board_left = board[:, fold:].copy()
        board_right= board[:, :fold+1].copy()
        new_board = board_left + np.flip(board_right, 1)

    # Counting number of dots in folded board
    result = np.count_nonzero(new_board)
    return result


def part2(dots, folds):
    """Solve part 2"""

    # Find shape of board
    board = np.zeros((895, 1311), dtype=int)

    # Fill board with dots
    for x,y in dots:
        board[(y, x)] = 1

    # Split the board
    for axis in folds:
        # Find the folder line
        print(f"{axis=}")
        fold = axis[1]

        # Fold on horizontal line
        if axis[0] == 'y':
            board_up = board[:fold:,:]
            board_down = board[-fold::,:]
            board = board_up + np.flip(board_down, 0)
        # Fold on vertical line:
        else:
            board_left = board[:, :fold:]
            board_right= board[:, -fold::]
            board = board_left + np.flip(board_right, 1)

        # Counting number of dots in folded board
        #count = np.count_nonzero(board)

    # Rebuild the board by displaying symbols for non-zeros values,
    # to obtain a readable answer
    # board!=0
    grid = []
    for line in board:
        grid_line = ''
        for c in line:
            if c == 0:
                grid_line += ' '
            else:
                grid_line += '#'
        grid.append(grid_line)

    # return result
    print(grid)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data_1 = parse_dots(puzzle_input_1)
    data_2 = parse_folds(puzzle_input_2)
    solution1 = part1(data_1, data_2)
    solution2 = part2(data_1, data_2)

    return solution1, solution2
