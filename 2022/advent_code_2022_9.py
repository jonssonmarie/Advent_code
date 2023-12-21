"""
If the head is ever two steps directly up, down, left, or right from the tail,
the tail must also move one step in that direction so it remains close enough

Otherwise, if the head and tail aren't touching and aren't in the same row or column,
the tail always moves one step diagonally to keep up

You just need to work out where the tail goes as the head follows a series of motions.
Assume the head and the tail both start at the same position, overlapping.

count up all of the positions the tail visited at least once
"""
import pandas as pd

input_data = pd.read_csv("input_data/input_day9", sep=" ", header=None).rename(columns={0: 'direction', 1: 'step'})

# part one
# initial head, tail position
head = [0, 0]
tail = [0, 0]

# collect all tail positions
locations_tail = {(0, 0)}

for idx, data in input_data.iterrows():
    for i in range(int(data.step)):
        # get step to go from move and set to head, step gives how many times to repeat move in range loop
        move = {'D': [0, 1], 'U': [0, -1], 'L': [-1, 0], 'R': [1, 0]}

        head[0] += move[data.direction][0]
        head[1] += move[data.direction][1]

        # calculate the diff to know were to move
        diff_x = tail[0] - head[0]
        diff_y = tail[1] - head[1]

        if diff_x == -2 and diff_y == 0:
            tail[0] += 1
        elif diff_x == 2 and diff_y == 0:
            tail[0] -= 1
        elif diff_x == 0 and diff_y == -2:
            tail[1] += 1
        elif diff_x == 0 and diff_y == 2:
            tail[1] -= 1
        elif (diff_x == 1 and diff_y == 2) or (diff_x == 2 and diff_y == 1):
            tail[0] -= 1
            tail[1] -= 1
        elif (diff_x == 1 and diff_y == -2) or (diff_x == 2 and diff_y == -1):
            tail[0] -= 1
            tail[1] += 1
        elif (diff_x == -1 and diff_y == -2) or (diff_y == -1 and diff_x == -2):
            tail[0] += 1
            tail[1] += 1
        elif (diff_x == -1 and diff_y == 2) or (diff_y == 1 and diff_x == -2):
            tail[0] += 1
            tail[1] -= 1

        locations_tail.add(tuple((tail[0], tail[1])))

print("Answer part one:", len(locations_tail))

# part two
# initial head, tail position
head10 = [[0, 0] for i in range(10)]
tail10 = [[0, 0] for i in range(10)]

# collect all tail positions
locations_tail2 = {(0, 0)}

for idx, data in input_data.iterrows():
    move = {'D': [0, 1], 'U': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
    for i in range(int(data.step)):
        # get step to go from move and set to head, step gives how many times to repeat move in range loop

        head10[0][0] += move[data.direction][0]
        head10[0][1] += move[data.direction][1]

        for j in range(1, 10):
            # calculate the diff to know were to move
            diff_x = head10[j][0] - head10[j - 1][0]
            diff_y = head10[j][1] - head10[j - 1][1]

            if diff_x < -1 and diff_y == 0:
                head10[j][0] += 1
            elif diff_x > 1 and diff_y == 0:
                head10[j][0] -= 1
            elif diff_x == 0 and diff_y > 1:
                head10[j][1] -= 1
            elif diff_x == 0 and diff_y < -1:
                head10[j][1] += 1
            elif diff_x > 0 and diff_y > 1:
                head10[j][0] -= 1
                head10[j][1] -= 1
            elif diff_x > 0 and diff_y < -1:
                head10[j][0] -= 1
                head10[j][1] += 1
            elif diff_x < 0 and diff_y < -1:
                head10[j][0] += 1
                head10[j][1] += 1
            elif diff_x < 0 and diff_y > 1:
                head10[j][0] += 1
                head10[j][1] -= 1
            elif diff_x > 1 and diff_y > 0:
                head10[j][0] -= 1
                head10[j][1] -= 1
            elif diff_x > 1 and diff_y < 0:
                head10[j][0] -= 1
                head10[j][1] += 1
            elif diff_x < -1 and diff_y < 0:
                head10[j][0] += 1
                head10[j][1] += 1
            elif diff_x < -1 and diff_y > 0:
                head10[j][0] += 1
                head10[j][1] -= 1
        locations_tail2.add(tuple((head10[9][0], head10[9][1])))

print("Answer part two:", len(locations_tail2))
