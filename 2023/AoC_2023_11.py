"""
Day 11: Cosmic Expansion
Part 1:
The image (input) includes empty space (.) and galaxies (#)
any rows or columns that contain no galaxies should all actually be twice as big.
alltså om en rad inte har galaxy lägg till den igen, likadant med kolumn
Expand the universe, then find the length of the shortest path between every pair of galaxies.
What is the sum of these lengths?

Part 2:
Now, instead of the expansion you did before, make each empty row or column one million times larger.
find the length of the shortest path between every pair of galaxies.
What is the sum of these lengths?
"""
import pandas as pd
from collections import Counter
data_path = "input_data/input_day_11"

data = open(data_path).read().strip().split('\n')

# row sublist
lines = [[c for c in row] for row in data]

# columns to row in sublist
lines_transform = pd.DataFrame(lines).T
lines_transform2 = lines_transform.values.tolist()


def find_empty_lines(line):
    all_empty = []
    for r, item in enumerate(line):
        n = Counter(item)
        k = n.keys()
        if not '#' in k:
            all_empty.append(r)
    return all_empty


all_empty_r = find_empty_lines(lines)
all_empty_c = find_empty_lines(lines_transform2)

row = len(lines)
col = len(lines[0])

# each # coordinate in r, c
coordinates = []
for r in range(col):
    for c in range(row):
        if lines[r][c] == '#':
            coordinates.append((r, c))


def solution(coord, part2=False):
    answer = 0
    for i, (r, c) in enumerate(coord):
        for j in range(i, len(coord)):
            r2, c2 = coord[j]
            dist = abs(r2 - r) + abs(c2 - c)

            # check if empty r/c and then add extra r/c
            for item_r in all_empty_r:
                if min(r, r2) <= item_r <= max(r, r2):
                    if part2:
                        dist += 1000000 - 1
                    else:
                        dist += 1

            for item_c in all_empty_c:
                if min(c, c2) <= item_c <= max(c, c2):
                    if part2:
                        dist += 1000000 - 1
                    else:
                        dist += 1

            answer += dist
    if part2:
        print(f'Solution part 2: {answer}')
    else:
        print(f'Solution part 1: {answer}')


solution(coordinates, part2=False)
solution(coordinates, part2=True)

"""
Solution part 1: 9509330
Solution part 2: 635832237682
"""