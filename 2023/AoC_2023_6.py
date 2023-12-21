"""
Day 6: Wait For It
"""
data_path = "input_data/input_day_6"
data = open(data_path).read().strip()
line = data.split('\n')

# For part 1
time1 = line[0].split()[1:]
record_distance = line[1].split()[1:]
race_data_part1 = list(zip(time1, record_distance))

# For part 2
id, time2 = line[0].split(':')
time2 = ''.join(time2.split())
id2, record_distance2 = line[1].split(':')
record_distance2 = ''.join(record_distance2.split())
race_data_part2 = [time2, record_distance2]

clean_all_ways = []


def clean(ways):
    for way in ways:
        clean_all_ways.extend(way)


def find_result(rtime, record):
    all_ways = []

    rtime = int(rtime)
    record = int(record)

    better_than_the_record = []

    for hold_button in range(1, rtime):
        speed = 1 * hold_button
        my_distance = speed * (rtime - hold_button)

        if my_distance > record:
            better_than_the_record.append(my_distance)

    num_ways = len(better_than_the_record)
    all_ways.append(num_ways)
    return all_ways


# Part 1
all_ways = [(find_result(td[0], td[1])) for td in race_data_part1]
clean(all_ways)
margin = clean_all_ways[0] * clean_all_ways[1] * clean_all_ways[2] * clean_all_ways[3]
print("Answer part 1:", margin)

# Part 2
all_ways2 = find_result(race_data_part2[0], race_data_part2[1])
print("Answer part 2:", all_ways2)
