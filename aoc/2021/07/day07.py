"""Day 7: The Treachery of Whales"""

import numpy as np


def parse(puzzle_input):
    """Parse input"""
    return [int(x) for x in puzzle_input.split(',')]


def part1(data):
    """Solve part 1"""

    pos = np.array(data)
    moves = dict()

    for p in (range(max(pos) + 1)):
        moves[p] = sum(map(abs, pos - p))

    optimal_pos = min(moves, key=moves.get)
    result = moves[optimal_pos]

    return result


def part2(data):
    """Solve part 2"""

    pos = np.array(data)
    fuel = dict()

    for p in (range(max(pos) + 1)):
        moves = pos - p
        fuel[p] = sum(map(
            lambda x: sum(range(abs(x) + 1)),
            moves
            ))

    optimal_pos = min(fuel, key=fuel.get)
    result = fuel[optimal_pos]

    return result


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2
