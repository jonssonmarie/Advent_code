"""
Day 13: Point of Incidence
ash (.)
rocks (#)

To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection;
to that, also add 100 multiplied by the number of rows above each horizontal line of reflection.

part 2: you discover that every mirror has exactly one! smudge
"""
data_path = "input_data/input_day_13"
data = open(data_path).read().strip()

summarize = 0
summarize2 = 0
for lines in data.split('\n\n'):

    line = lines.split('\n')
    col = len(line[0])
    row = len(line)

    for cc in range(col - 1):  # vertical
        ok = True
        smudge = 0  # part 2
        for c in range(col):
            # from reflection line go to left side and right side to find match
            left_side = cc - c
            right_side = cc + c + 1

            if 0 <= left_side < right_side < col:
                for r in range(row):
                    if line[r][left_side] != line[r][right_side]:
                        ok = False
                        smudge += 1  # part 2

        if ok:
            summarize += cc + 1
        if smudge == 1:  # part 2
            summarize2 += cc + 1

    for r in range(row - 1):  # horisontal
        ok = True
        smudge = 0  # part 2
        for rr in range(row):
            up = r - rr
            down = r + rr + 1
            if 0 <= up < down < row:
                for c in range(col):
                    if line[up][c] != line[down][c]:
                        ok = False
                        smudge += 1  # part 2

        if ok:
            summarize += (r + 1) * 100
        if smudge == 1:  # part 2
            summarize2 += (r + 1) * 100


print("Part 1:", summarize)
print("Part 2:", summarize2)
