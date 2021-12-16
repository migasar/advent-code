"""IN PROGRESS | Day 6: Lanternfish"""


# Input
# Set input
input_ex = "3,4,3,1,2"
input_full = "1,3,4,1,5,2,1,1,1,1,5,1,5,1,1,1,1,3,1,1,1,1,1,1,1,2,1,5,1,1,1,1,1,4,4,1,1,4,1,1,2,3,1,5,1,4,1,2,4,1,1,1,1,1,1,1,1,2,5,3,3,5,1,1,1,1,4,1,1,3,1,1,1,2,3,4,1,1,5,1,1,1,1,1,2,1,3,1,3,1,2,5,1,1,1,1,5,1,5,5,1,1,1,1,3,4,4,4,1,5,1,1,4,4,1,1,1,1,3,1,1,1,1,1,1,3,2,1,4,1,1,4,1,5,5,1,2,2,1,5,4,2,1,1,5,1,5,1,3,1,1,1,1,1,4,1,2,1,1,5,1,1,4,1,4,5,3,5,5,1,2,1,1,1,1,1,3,5,1,2,1,2,1,3,1,1,1,1,1,4,5,4,1,3,3,1,1,1,1,1,1,1,1,1,5,1,1,1,5,1,1,4,1,5,2,4,1,1,1,2,1,1,4,4,1,2,1,1,1,1,5,3,1,1,1,1,4,1,4,1,1,1,1,1,1,3,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,5,1,2,1,1,1,1,1,1,1,1,1"

input_ = input_ex

# Transform raw input in list of values
fishes = [int(x) for x in input_.split(',')]

shoal = dict()
for i, v in enumerate(fishes):
    shoal[i] = v


# Part One
# Define algorithm
def shoal_growth(count=5, shoal=shoal):
    """Sequential iteration to simulate the growth of the group of fishes"""

    size = len(shoal)
    for c in range(count):
        shoal_temp = shoal.copy()

        for k, v in shoal.items():
            if v > 0:
                shoal_temp[k] = v - 1
            else:
                shoal_temp[k] = 6
                shoal_temp[size] = 8
                size += 1

        shoal = shoal_temp

    return shoal


# Part Two
# No clue how to do this
