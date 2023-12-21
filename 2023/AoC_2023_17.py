"""
--- Day 17: Clumsy Crucible ---
Part 1
traffic patterns, ambient temperature, and hundreds of other parameters to calculate exactly
how much heat loss can be expected for a crucible entering any particular city block.
Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block.

The starting point, the lava pool, is the top-left city block; the destination,
the machine parts factory, is the bottom-right city block.

it can move at most three blocks in a single direction before it must turn 90 degrees left or right.
The crucible also can't reverse direction; after entering each city block,
it may only turn left, continue straight, or turn right.

Directing the crucible from the lava pool to the machine parts factory, but not moving more than
three consecutive blocks in the same direction, what is the least heat loss it can incur?

"""
data_path = "input_data/input_day_17"

data = open(data_path).read().strip()

lines = [[l for l in line] for line in data.split('\n')]

row = len(lines)
col = len(lines[0])

print()
