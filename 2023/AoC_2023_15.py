"""
--- Day 15: Lens Library ---
Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256.

Part 2:
The label will be immediately followed by a character that indicates the operation to perform:
either an equals sign (=) or a dash (-).
If the operation character is a dash (-), go to the relevant box and remove the lens with the given label if it
is present in the box. Then, move any remaining lenses as far forward in the box as they can go without
changing their order, filling any space made by removing the indicated lens.
(If no lens in that box has the given label, nothing happens.)

If the operation character is an equals sign (=), it will be followed by a number indicating the focal
length of the lens that needs to go into the relevant box; be sure to use the label maker to mark the
lens with the label given in the beginning of the step so you can find it later.

There are two possible situations:
already a lens in the box with the same label, replace the old lens with the new lens:
not moving any other lenses in the box.
No lens in the box with the same label, add the lens last in box
Don't move any of the other lenses when you do this.
No lenses at all in the box, the new lens goes all the way to the front of the box.

Each step begins with a sequence of letters that indicate the label of the lens on which the step operates.
The result of running the HASH algorithm on the label indicates the correct box for that step.
"""


data_path = "input_data/input_day_15"

data = open(data_path).read().strip()
lines = data.split(',')

# part 1
answer = []
for line in lines:
    num = 0
    for i in range(len(line)):
        num = +((num + ord(line[i])) * 17) % 256
    answer.append(num)

print("Part 1: ", sum(answer))

# Part 2
boxes = [[] for i in range(256)]


def box_number(letters):
    box_num = 0
    for char in letters:
        box_num = ((box_num + ord(char)) * 17) % 256
    return box_num


for line in lines:
    if line[-1] == '-':
        lens = line[:-1]
        bn = box_number(lens)
        boxes[bn] = [(l, v) for (l, v) in boxes[bn] if l != lens]

    elif line[-2] == '=':
        lens = line[:-2]
        num = line[-1]
        lens_add = line.replace('=', ' ')
        bn = box_number(lens)

        if lens in [l for (l, v) in boxes[bn]]:
            boxes[bn] = [(l, num if lens == l else v) for (l, v) in boxes[bn]]
        else:
            boxes[bn].append((lens, num))


answer2 = 0
for i, box in enumerate(boxes):
    for j, (l, v) in enumerate(box):
        answer2 += (i+1) * (j+1) * int(v)

print("Part 2: ", answer2)  # rätt 263211
