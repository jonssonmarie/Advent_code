"""
Day 5: If You Give A Seed A Fertilizer

Every type of seed, soil, fertilizer and so on is identified with a number,
but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.
The rest of the almanac contains a list of maps which describe how to convert numbers from a source category
into numbers in a destination category.

seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination)

Each line within a map contains three numbers: the destination range start, the source range start,
and the range length.

example seed-to-soil map:
destination source range
50          98      2
52          50      48

The first line has a destination range start of 50, a source range start of 98, and a range length of 2.
This line means that the source range starts at 98 and contains two values: 98 and 99.
The destination range is the same length, but it starts at 50, so its two values are 50 and 51.
With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99
corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, 52, 53, 54, 55..., 96, 97.
This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, 54, 55 ..., 98, 99.
So, seed number 53 corresponds to soil number 55. De korresponderar med samma siffra i ordningen i destination
"""

data_path = "input_data/input_day_5"
data = open(data_path).read().strip()

seeds, *maps = data.split('\n\n')
seeds = [int(x) for x in seeds.split(':')[1].split()] #seeds.split(':')[1].split()

# part 1
# What is the lowest location number that corresponds to any of the initial seed numbers?
# the seeds number should be check if found within source, source + r.
# If not then the source correspond to the same destination number


def find_corresponds(seed, map_lst):
    """
    Find corresponding number in maps for a seed from seeds
    :param seed: a seed number from seeds
    :param map_lst: list with all maps
    :return: seed
    """
    for line in map_lst:
        dest, source, r = [int(x) for x in line.split()]
        # check if mapped, seed should be within range of source and source + r
        # e.g seed = 79, source= 50, dest = 52. 79 correspond to pos in map: 79 - 50 + 52 = 81
        if source <= seed < source + r:
            return seed - source + dest
    # else the source corresponds to dest
    return seed


def get_location(s):
    """
    get the location
    :param s:
    :return:
    """
    temp = int(s)
    for map_list in maps:
        map_lst = map_list.split('\n')[1:]
        temp = find_corresponds(temp, map_lst)
    return temp


print("Answer part 1:", min(get_location(s) for s in seeds))  # rätt: 323142486

# Part 2
"""
So, in the first line of the example above:
seeds: 79 14 55 13

This line describes two ranges of seed numbers to be planted in the garden. 
The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. 
The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.
Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.  14 + 13 =  27 

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. 
What is the lowest location number that corresponds to any of the initial seed numbers?
"""


def apply_range(R, m):
    """
    check range
    :param R: seeds start point and end point - exclusive end point
    :param m: a map from maps
    :return: list
    """
    intersect = []
    lines = m.split('\n')[1:]  # remove name

    # include dst, src, r
    map_data = [[int(x) for x in line.split()] for line in lines]

    for (dest, source, r) in map_data:
        src_end = source + r
        not_intersect = []

        while R:
            (st, ed) = R.pop()

            # check boundaries (source, r) and (st,ed)
            before = (st, min(ed, source))
            intersection = (max(st, source), min(src_end, ed))
            after = (max(src_end, st), ed)

            if before[1] > before[0]:
                not_intersect.append(before)
            if intersection[1] > intersection[0]:
                intersect.append((intersection[0] - source + dest, intersection[1] - source + dest))
            if after[1] > after[0]:
                not_intersect.append(after)
        R = not_intersect
    return intersect + R


part_2 = []

# collect (start, range) for seeds
pairs = []
for i in range(0, len(seeds), 2):
    pairs.append((seeds[i], seeds[i+1] - 1))


# start (st), range (re) for seeds
for st, re in pairs:
    # inclusive on the left, exclusive on the right
    # R = start point (st) end point (ed) which is exclusive, think of range(start, stop, end)
    R = [(st, st + re)]
    for f in maps:
        R = apply_range(R, f)

    part_2.append(min(R)[0])
print("Answer part 2:", min(part_2))

# 323142486 för högt  Answer part 2: 358712920 för högt  ok: Answer part 2: 79874951