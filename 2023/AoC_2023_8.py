"""
Day 8: Haunted Wasteland

AAA - my start place
ZZZ - place to reach

Starting with AAA, you need to look up the next element based on the next left/right instruction in your input.
AAA = (BBB, CCC) (left, right)

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)

Example, start with AAA and go right (R) by choosing the right element of AAA, CCC.
Then, L means to choose the left element of CCC, ZZZ.
By following the left/right instructions, you reach ZZZ in 2 steps.

If you run out of left/right instructions, repeat the whole sequence of instructions as necessary:
RL really means RLRLRLRLRLRLRLRL... and so on.

How many steps are required to reach ZZZ?
"""

from collections import Counter, defaultdict
import math

data_path = "input_data/input_day_8"
data = open(data_path).read()

network = data.split('\n')[2:]

instructions = data.split('\n\n')[0]
nodes = [item.split('=') for item in network]
nodes = [[item[0], item[1].replace('(', '').replace(')', '').replace(',', '')] for item in nodes]

# Part 1
# start position
pos = 'AAA'

# create a dict with L and R for the nodes in the network
left_right = {'L': {}, 'R': {}}

# apply data to left_right dict
for line in nodes:
    node = line[0].strip()
    left_right['L'][node] = line[1].strip().split()[0]
    left_right['R'][node] = line[1].strip().split()[1]

num_step = 0
while pos != 'ZZZ':
    mod = num_step % len(instructions)  # gives index within range
    pos = left_right[instructions[mod]][pos]
    num_step += 1

print("Answer part 1", num_step)


# part 2
"""
If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same 
time until they all simultaneously end up at nodes that end with Z.
(If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.)

Denna hade jag inte kunnat lösa utan hjälp från youtube, hade glömt av gcd
"""

lr = {'L': {}, 'R': {}}

for line in nodes:
    node = line[0].strip()
    left = line[1].strip().split()[0]
    right = line[1].strip().split()[1]

    lr['L'][node] = left
    lr['R'][node] = right


def hcf(xs):
    ans = 1
    for x in xs:
        ans = (x * ans // math.gcd(x, ans))
    return ans


a_positions = []
for k in lr['L']:
    if k.endswith('A'):
        a_positions.append(k)


def part2(a_position):
    t = {}
    num_step = 0

    while True:
        np = []
        for i, pos in enumerate(a_position):
            mod = num_step % len(instructions)  # gives index within range
            pos = lr[instructions[mod]][pos]
            if pos.endswith('Z'):
                t[i] = num_step + 1  # go to next step, do not need to go back to A
                if len(t) == len(a_position):
                    return hcf(t.values())
            np.append(pos)
        a_position = np
        num_step += 1


print("Solution part 2:", part2(a_positions))
