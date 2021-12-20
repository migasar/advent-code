"""IN PROGRESS | Day 4: Giant Squid"""


def parse(puzzle_input_1, puzzle_input_2):
    """Parse input"""

    data_1 = [int(x) for x in puzzle_input_1.split(',')]
    data_2 = puzzle_input_2.splitlines()

    return data_1, data_2


def part1(data_1, data_2):
    """Solve part 1"""

    boards = []
    board_temp = []

    for line in data_2.splitlines():
        if board_temp and not line:
            boards.append(board_temp)
            board_temp = []
        else:
            board_temp.append([int(x) for x in line.split()])

    boards_pattern = []
    for n in range(len(boards)):
        board_replicate = []
        for m in range(len(boards[0])):
            board_line = []
            for o in range(len(boards[0][0])):
                board_line.append(0)
            board_replicate.append(board_line)
        boards_pattern.append(board_replicate)

    pass


def part2(data_1, data_2):
    """Solve part 2"""
    pass


def solve(puzzle_input_1, puzzle_input_2):
    """Solve the puzzle for the given input"""
    data_1, data_2 = parse(puzzle_input_1, puzzle_input_2)
    solution1 = part1(data_1, data_2)
    solution2 = part2(data_1, data_2)

    return solution1, solution2
