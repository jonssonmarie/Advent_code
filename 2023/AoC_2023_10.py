"""
Day 10: Pipe Maze

The pipes are arranged in a two-dimensional grid of tiles:
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile,
but your sketch doesn't show what shape the pipe has.

Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position
to the point farthest from the starting position?
hur många möts vid en knutpunkt vid varje tillägg, det ger siffran

"""
from collections import defaultdict

data_path = "input_data/input_day_10"

data = open(data_path).read().strip().split('\n')

tiles = [[l for l in line] for line in data]

row = len(tiles)
col = len(data[0])
# with S
# FF7-||||.J7F-J7.LJL7L--JLJLJF7F-J||L7|L---7F-7LJF-JF7F7F7||JF7L-7LJFJL-7|F7FJ|-|L7F   S   ||LJFJL--7FJ|||FJ||FJLJ|FF7F7.7J||.LF77.|||7F7.|7.FJ||L|


tile_definition = {}

# find the right pipe as S and replace S with pipe type
for i in range(col):
    for j in range(row):
        if tiles[i][j] == 'S':   #print(tiles[i])  # S index: 83 row: 17

            go_down = (tiles[i - 1][j] in ['|', '7', 'F'])          # South
            go_left = (tiles[i][j - 1] in ['-', '7', 'F'])          # West
            go_up = (tiles[i + 1][j] in ['|', 'L', 'J'])            # North
            go_right = (tiles[i][j + 1] in ['-', 'J', '7'])         # East

            if sum([go_up, go_right, go_down, go_left]) == 2:   # check that all go is not more than two True
                if go_up and go_down:
                    tiles[i][j] = '|'
                    dir = []

                elif go_up and go_right:
                    tiles[i][j] = 'L'
                    dir = []

                elif go_up and go_left:
                    tiles[i][j] = 'J'
                    dir = []

                elif go_down and go_right:
                    tiles[i][j] = 'F'
                    dir = []

                elif go_down and go_left:
                    tiles[i][j] = '7'
                    dir = []

                elif go_left and go_right:
                    tiles[i][j] = '-'
                    dir = []

                else:
                    assert False



















# up, right, down, left
dir_row = [-1, 0, 1, 0]
dir_col = [0, 1, 0, -1]

# move and check up, down, left, right
distance = 0
r = sr
c = sc
d = sd
distance += 1
while True:
    # go through all directions in row, col
    if tiles[r][c] == 'L':
        if d not in [2, 3]:
            break
        elif d == 2:
            d = 1
        else:
            d = 0
    if tiles[r][c] == 'J':
        if d not in [1, 2]:
            break
        elif d == 1:
            d = 0
        else:
            d = 3
    if tiles[r][c] == '7':
        if d not in [0, 1]:
            break
        elif d == 1:
            d = 0
        else:
            d = 2
    if tiles[r][c] == 'F':
        if d not in [10, 3]:
            break
        elif d == 0:
            d = 0
        else:
            d = 1
    if tiles[r][c] == '.':
        break
    if (r, c) == (sr, sc):
        print(distance//2)

