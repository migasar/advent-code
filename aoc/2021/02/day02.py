"""Day 2: Dive"""

import parse


# Parse Input
def parse_input(raw_input):
    """Transform raw input in list of string values"""
    return raw_input.splitlines()


# Part One
def get_position(commands):
    """Count changes in position (horizontal and depth)"""

    forward = 0
    up = 0
    down = 0
    f_pattern = "forward {value}"
    u_pattern = "up {value}"
    d_pattern = "down {value}"

    for c in commands:
        f_match = parse.search(f_pattern, c)
        u_match = parse.search(u_pattern, c)
        d_match = parse.search(d_pattern, c)

        if f_match:
            forward += int(f_match['value'])
        if u_match:
            up += int(u_match['value'])
        if d_match:
            down += int(d_match['value'])

    depth = down - up
    result = forward * depth

    return result


# Part Two
def get_position_with_aim(commands):
    """Count changes in position (horizontal and depth)
        with aim
    """

    forward = 0
    aim = 0
    depth = 0
    f_pattern = "forward {value}"
    u_pattern = "up {value}"
    d_pattern = "down {value}"

    for c in commands:
        f_match = parse.search(f_pattern, c)
        u_match = parse.search(u_pattern, c)
        d_match = parse.search(d_pattern, c)

        if f_match:
            forward += int(f_match['value'])
            depth += (aim * int(f_match['value']))
        if u_match:
            aim -= int(u_match['value'])
        if d_match:
            aim += int(d_match['value'])

    result = forward * depth

    return result
