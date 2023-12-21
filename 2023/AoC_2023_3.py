"""
Day 3: Gear Ratios
part 1:
The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one.
If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

part 2:
The missing part wasn't the only issue - one of the gears in the engine is wrong.
A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.
This time, you need to find the gear ratio of every gear and add them all up so that the engineer can
figure out which gear needs to be replaced.
"""
from collections import defaultdict

data_path = "input_data/input_day_3"

data = open(data_path).read().strip()
lines = data.split("\n")
grid = [[c for c in line] for line in lines]

# for part 2
numbers_adjacent_to_gears = defaultdict(list)

answer = 0  # part 1

# grid lengths
row = len(grid)
column = len(grid[0])

# remove '-' and change to '+', since '-' is not recognised
for number in range(len(grid)):
    for char in range(len(grid[number]) + 1):
        if char < column and grid[number][char] == '-':
            grid[number][char] = '+'


for number in range(len(grid)):
    part_exist = False
    check = 0
    gears = set()   # for part 2

    # range given from current row + 1
    for char in range(len(grid[number]) + 1):
        # check that char position within column and char is a digit
        if char < column and grid[number][char].isdigit():
            check = (check * 10) + int(grid[number][char])
            # use check * 10 to increase from 5 to 57 etc 57*10 +3 = 573 instead of using str or list and add to

            # check one step after/forward, and both row and column wise
            for r in [-1, 0, 1]:
                for c in [-1, 0, 1]:
                    # check within column and row range
                    if 0 <= number + r < row and 0 <= char + c < column:
                        ch = grid[number + r][char + c]
                        # check if symbol and not digit or .
                        if not ch.isdigit() and ch != '.':
                            part_exist = True
                        # for part 2
                        if ch == '*':
                            gears.add((number + r, char + c))
        elif check > 0:
            # for part 2
            for gear in gears:
                numbers_adjacent_to_gears[gear].append(check)
            # for part 1
            if part_exist:
                answer += check
            check = 0   # reset
            part_exist = False
            gears = set()  # for part 2

print("Solution 1:", answer)

# for part 2
answer_2 = 0

for k, val in numbers_adjacent_to_gears.items():
    if len(val) == 2:
        answer_2 += val[0] * val[1]

print("Solution 2:", answer_2)
