"""Day 10: Syntax Scoring"""

import pathlib
import sys


# Set Input
input_ex = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

puzzle_input = input_ex


def parse(puzzle_input):
    """Parse input"""

    data = [list(line) for line in puzzle_input.splitlines()]
    return data


def part1(data):
    """Solve part 1"""

    close_brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
    error_values = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    for line in data:
        stack = []
        for c in line:
            if c in close_brackets:
                if not stack or stack[-1] != close_brackets[c]:
                    score += error_values[c]
                    break
                stack.pop()
            else:
                stack.append(c)

    return score


def part2(data):
    """Solve part 2"""

    close_brackets = {')': '(', ']': '[', '}': '{', '>': '<'}

    # Discard corrupted lines
    valid_lines = []
    for line in data:
        stack = []
        valid = True
        for c in line:
            if c in close_brackets:
                if not stack or stack[-1] != close_brackets[c]:
                    valid = False
                    break
                stack.pop()
            else:
                stack.append(c)
        if valid:
            valid_lines.append(line)

    # Find lone opening brackets
    added_brackets = []
    for line in valid_lines:
        stack = []
        for c in line:
            if c in close_brackets:
                stack.pop()
            else:
                stack.append(c)
        added_brackets.append(stack)

    # Score each completed line
    completion_values = {'(': 1, '[': 2, '{': 3, '<': 4}
    scoreboard = []
    for line in added_brackets:
        score = 0
        for b in line[::-1]:
            score = (score * 5) + completion_values[b]
        scoreboard.append(score)

    # Get median score
    middle_index = int((len(scoreboard))/2)
    result = sorted(scoreboard)[middle_index]

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
