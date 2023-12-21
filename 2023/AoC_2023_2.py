"""
Day 2: Cube Conundrum

Part 1
Determine which games would have been possible if the bag had been loaded with
only 12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?
Means collect the ID and then make sum calculation
"""
from collections import defaultdict
data = "input_data/input_day_2"

# Part 1
number_id = 0
lines = open(data).read().strip()
test = open(data).readlines()

for line in lines.split('\n'):
    ok = True
    id, line = line.split(':')

    for cubes in line.strip().split(';'):
        for cube in cubes.split(','):
            digit, color = cube.split()
            if int(digit) > {'red': 12, 'green': 13, 'blue': 14}.get(color):
                ok = False
    if ok:
        number_id += int(id.split()[-1])

print("part 1", number_id)


"""
part 2
what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""
total_score = 0

for line in lines.split('\n'):
    id, line = line.split(':')
    V = defaultdict(int)
    for cubes in line.strip().split(';'):
        for cube in cubes.split(','):
            digit, color = cube.split()
            V[color] = max(V[color], int(digit))

    score = 1
    for v in V.values():
        score *= v
    total_score += score

print("part 2", total_score)




