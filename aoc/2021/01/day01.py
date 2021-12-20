"""Day 1: Sonar Sweep"""


# Parse Input
def sanitized_input(raw_input):
    """Transform raw input in list of values"""
    return [int(line) for line in raw_input.splitlines()]


# Part One
def count_depth_increase(depths):
    """Count depth increase"""

    increased_count = 0
    for count, value in enumerate(depths):
        if count > 0:
            previous = depths[count - 1]
            if value > previous:
                increased_count += 1

    return increased_count


# Part Two
def count_depth_window_increase(depths):
    """Count group of depths increase"""

    increased_count = 0
    for c in range(len(depths)):
        if (c + 2) >= len(depths):
            break

        if c > 0:
            window = depths[c] + depths[c + 1] + depths[c + 2]
            previous = depths[c - 1] + depths[c] + depths[c + 1]
            if window > previous:
                increased_count += 1

    return increased_count
