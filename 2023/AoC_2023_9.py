"""
Day 9: Mirage Maintenance
"""
data_path = "input_data/input_day_9"

data = open(data_path).read().split('\n')

lines = [line.split() for line in data]
lines = [[int(l) for l in line] for line in lines]


def calculate_diff(line):
    data = [line[:]]

    while not all(y == 0 for y in data[-1]):
        next_row = []
        for i in range(len(data[-1]) - 1):
            next_row.append(data[-1][i + 1] - data[-1][i])

        data.append(next_row)

    for i in range(len(data) - 2, -1, -1):
        data[i].append(data[i][-1] + data[i + 1][-1])
    return data[0][-1]


answer = sum(calculate_diff(line) for line in lines)
print("Part 1:", answer)

answer2 = sum(calculate_diff(line[::-1]) for line in lines)
print("Part 2:", answer2)
# Part 1: 1584748274
# Part 2: 1026


# solution 2
def calculate_diff(line):
    if all(y == 0 for y in line):
        return 0

    diff = []

    for i in range(len(line) - 1):
        first = line[i]
        second = line[i + 1]
        diff.append(second - first)

    return line[-1] + calculate_diff(diff)


answer = 0
for line in lines:
    answer += calculate_diff(line)


print("answer part 1", answer)

answer2 = 0
for line in lines:
    answer2 += calculate_diff(line[::-1])

print("answer part 2", answer2)
