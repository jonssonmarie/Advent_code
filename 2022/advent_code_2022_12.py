"""
Day 12: Hill Climbing Algorithm
You try contacting the Elves using your handheld device, but the river you're following must
be too low to get a decent signal.
You ask the device for a heightmap of the surrounding area (your puzzle input).

The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given
by a single lowercase letter, where a is the lowest elevation, b is the next-lowest,
and so on up to the highest elevation, z.
Also included on the heightmap are marks for your current position (S)
and the location that should get the best signal (E).

Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.


You'd like to reach E, but to save energy, you should do it in as few steps as possible.
During each step, you can move exactly one square up, down, left, or right.

To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher
than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n,
but not to elevation o.
(This also means that the elevation of the destination square can be much lower than the elevation of your
current square.)

For example:
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi

Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right,
but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:
v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^

In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<),
or right (>). The location that should get the best signal is still E, and . marks unvisited squares.
This path reaches the goal in 31 steps, the fewest possible.
What is the fewest steps required to move from your current position to the location that should get the best signal?
"""

# New for me
from time import perf_counter as pfc

data = "input_data/input_day12"


def create_coordinates(file):
    with open(file) as f:
        return {
            (x, y): ord(char) - 96
            if char.islower()
            else char
            for y, line in enumerate(f.readlines())
            for x, char in enumerate(line.strip())
        }


coord_values = create_coordinates(data)


def get_all_a(coord_value):
    start_position_a = []
    for pos, value in coord_value.items():
        if coord_value[pos] == 1:
            start_position_a.append(pos)
    return start_position_a


def upper_to_number(coord_value):
    for pos, value in coord_value.items():
        if value == 'S':
            start = pos
            coord_value[start] = 1  # Start position
        elif value == "E":
            end = pos
            coord_value[end] = 26  # End position
    return coord_value, start, end


coord_value, start, end = upper_to_number(coord_values)


def get_and_check_neighbor(data, x, y):
    for moved in [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]]:
        if moved not in data:
            continue
        if data[moved] - data[(x, y)] > 1:
            continue
        yield moved
    """
    Yield: return sends a specified value back to its caller whereas Yield can produce a sequence of values.
     We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory. 
     Yield is used in Python generators. A generator function is defined just like a normal function, but whenever 
     it needs to generate a value, it does so with the yield keyword rather than return. 
     If the body of a def contains yield, the function automatically becomes a generator function. """


def get_shortest_path(data, start, end):

    path_index = 0              # index for path counting
    visited_paths = {start}     # the positions of the visited places
    paths = [[start]]           # all coordinates that been tested and not working

    while path_index < len(paths):
        current_path = paths[path_index]
        last_path = current_path[-1]
        for neighbor in get_and_check_neighbor(data, *last_path):
            if neighbor in visited_paths:
                continue
            if neighbor == end:
                #print("Solution: ", len(current_path))
                return len(current_path)
            paths.append((current_path.copy() + [neighbor]))
            visited_paths.add(neighbor)
        path_index += 1
    return 99999  # used for to not return None


start_pfc = pfc()
print("Solution part 1", get_shortest_path(coord_values, start, end))
print(pfc() - start_pfc)

# part 2
all_start_position_a = get_all_a(coord_values)

calculated_way = []
for start in all_start_position_a:
    number_steps = get_shortest_path(coord_values, start, end)
    calculated_way.append(number_steps)

start_pfc = pfc()
part_2 = min([get_shortest_path(coord_values, start, end) for start in all_start_position_a])
print("Solution part 2", part_2 )
print(pfc() - start_pfc)




