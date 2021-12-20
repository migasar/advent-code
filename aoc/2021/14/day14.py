"""Day 14: Extended Polymerization"""

from collections import Counter


# Set Input
INPUT_EX_1 = """NNCB"""

INPUT_EX_2="""CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

puzzle_input_1 = INPUT_EX_1
puzzle_input_2 = INPUT_EX_2


# Format first input
def parse_template(puzzle_input):
    """Parse input"""

    return list(puzzle_input)


# Format second input
def parse_rules(puzzle_input):
    """Parse input"""

    data = {}
    pattern = "fold along "

    for rule in puzzle_input.splitlines():
        data[rule[:2]] = rule[-1]

    return data


def part1(data, rules=rules, step=10):
    """Solve part 1"""

    template = data

    # Build formula of polymer
    for _ in range(step):
        polymer = []

        for i, v in enumerate(template):
            polymer.append(v)
            if i == (len(template) - 1):
                continue
            else:
                pair = v + template[i + 1]
                polymer.append(rules[pair])
        template = polymer

    # Count occurences of letters in polymer
    elements = Counter(polymer)

    result = max(elements.values()) - min(elements.values())
    return result


def part2(data, rules=rules, step=10):
    """Solve part 2"""

    # frequency = {}
    # for pair in rules:
    #     frequency[pair] = 0

    # for _ in range(step):

    # return result
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_template(puzzle_input_1)
    rules = parse_rules(puzzle_input_2)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2
