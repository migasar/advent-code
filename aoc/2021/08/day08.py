"""IN PROGRESS | Day 8: Seven Segment Search"""


# Set Input
input_ex = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

puzzle_input = input_ex


def parse(puzzle_input):
    """Parse input"""

    lines = [line.split(' | ') for line in puzzle_input.splitlines()]
    data = [[seq.split(' ') for seq in line] for line in lines]

    return data



def part1(data):
    """Solve part 1"""

    frequency = dict()

    for i in data:
        for j in i[1]:
            if len(j) in frequency:
                frequency[len(j)] += 1
            else:
                frequency[len(j)] = 1

    result = frequency[2] + frequency[4] + frequency[3] + frequency[7]

    return result


# IN PROGRESS | Not Working
def part2(data):
    """Solve part 2"""

    codex = {
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': ''
    }

    digit_patterns = {
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: ''
    }

    digit_letters = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c', 'f'],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'e', 'f', 'g'],
        7: ['a', 'c', 'f'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g']
    }

    digit_lengths = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6
    }

    for i in data:
        for j in i[0]:
            if len(j) == 2:
                if not digit_patterns[1]:
                    digit_patterns[1] = ''.join(sorted(list(j)))
            if len(j) == 4:
                if not digit_patterns[4]:
                    digit_patterns[4] = ''.join(sorted(list(j)))
            if len(j) == 3:
                if not digit_patterns[7]:
                    digit_patterns[7] = ''.join(sorted(list(j)))
            if len(j) == 7:
                if not digit_patterns[8]:
                    digit_patterns[8] = ''.join(sorted(list(j)))

    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2
