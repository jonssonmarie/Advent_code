"""
Day 14: Parabolic Reflector Dish

rounded rocks (O)
cube-shaped rocks (#)
empty spaces (.)

In short: if you move the rocks, you can focus the dish.
Tilt the platform so that the rounded rocks all roll north.
Afterward, what is the total load on the north support beams?

Part 2:
Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east
After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction.
"""
from collections import Counter

data_path = "input_data/input_day_14"
data = open(data_path).read().strip().split('\n')
line = [[l for l in lines] for lines in data]


# rotate line
def rotate_data(l):
    col = len(l[0])
    row = len(l)

    rotated_lines = [[r for r in range(row)] for c in range(col)]
    for r in range(row):
        for c in range(col):
            # roll north, then west, then south, then east.
            rotated_lines[c][row - 1 - r] = l[r][c]
    return rotated_lines


def roll_rocks(l):
    col = len(l[0])
    row = len(l)

    for c in range(col):
        for rr in range(row):
            for r in range(row):
                if l[r][c] == 'O' and l[r - 1][c] == '.' and r > 0:
                    l[r][c] = '.'
                    l[r - 1][c] = 'O'
    return l


def calculate_answer(lin):
    ans = 0
    row = len(lin)

    for i, l in enumerate(lin):
        num = Counter(l)
        for key in num:
            if key == 'O':
                n = num[key]
                ans += n * (row - i)

    return ans


memo = {}
t = 0
target = 1000000000

while t < target:
    t += 1
    for n in range(4):
        line = roll_rocks(line)
        if n == 0 and t == 1:
            print("part 1:", calculate_answer(line))
        line = rotate_data(line)

    # calculate cycle length
    line_hash = tuple(tuple(row) for row in line)
    # after some loops the same pattern occur so to save time do not count them again, save them in memo
    if line_hash in memo:
        cycle_length = t - memo[line_hash]   # key
        num_reduce = (target - t) // cycle_length
        t += num_reduce * cycle_length
    memo[line_hash] = t

print("Part 2: ", calculate_answer(line))
# rätt part 2: 106390
# rätt part 1: 106186
