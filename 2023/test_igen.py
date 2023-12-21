import re
import math
import copy
import numpy as np
from itertools import combinations, permutations, product
import time


data_path = "input_data/input_day_10"
data = open(data_path).read().strip().split('\n')
tiles = [[l for l in line] for line in data]


row = len(tiles)
col = len(data[0])

# find the right pipe as S and replace S with pipe type
for r in range(row):
    for c in range(col):
        if tiles[r][c] == 'S':   #print(tiles[i])  # S index: 83 row: 17
            sr = r
            sc = c
            go_south = (tiles[r - 1][c] in ['|', '7', 'F'])        # South
            go_west = (tiles[r][c - 1] in ['-', '7', 'F'])         # West
            go_north = (tiles[r + 1][c] in ['|', 'L', 'J'])        # North
            go_east = (tiles[r][c + 1] in ['-', 'J', '7'])         # East

            if sum([go_south, go_west, go_north, go_east]) == 2:   # check that all go is not more than two True
                if go_south and go_north:
                    tiles[r][c] = '|'

                elif go_north and go_east:
                    tiles[r][c] = 'L'

                elif go_north and go_west:
                    tiles[r][c] = 'J'

                elif go_north and go_east:
                    tiles[r][c] = 'F'

                elif go_south and go_east:
                    tiles[r][c] = '7'

                elif go_west and go_east:
                    tiles[r][c] = '-'

                else:
                    assert False


# up, right, down, left
dir_row = [-1, 0, 1]
dir_col = [-1, 0, 1]

# count steps
distance = 0


while True:
    r = sr
    c = sc

    distance += 1
    if tiles[r][c] == 'L':
        pass
    if tiles[r][c] == 'J':
        pass
    if tiles[r][c] == '7':
        pass
    if tiles[r][c] == 'F':
        pass
    if tiles[r][c] == '.':
        pass



