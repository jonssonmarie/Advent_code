import re
from collections import defaultdict


def read_file():
    file_input = open("input_data/input_day5", "r")
    read_file_input = file_input.read()
    parsed_file = read_file_input.split('\n')
    return parsed_file


def split_data(data):
    input_data = data
    instructions = []
    num_stacks = 0
    stack_string = []

    for line in input_data:
        line.split('\n')
        if "[" in line:
            stack_string.append(line)
        elif 'move' in line:
            instructions.append(line)
        elif line != '':
            num_stacks = int(line[-1])
    return instructions, num_stacks, stack_string


instructions, num_stacks, stack_strings = split_data(read_file())


def load_stack(stack_string, num_stack):
    stack_layout = {int(i + 1): [] for i in range(num_stack)}

    for row in reversed(stack_string):
        for i in range(num_stack):
            stack_char = row[4 * i:4 * i + 3].replace("[", "").replace("]", "")
            if stack_char != '':
                stack_layout[i + 1].append(stack_char)
    return stack_layout


stack_layout = load_stack(stack_strings, num_stacks)


def return_top_layer(stack_layouts):
    top_layer = ''
    for values in stack_layouts.values():
        if values:
            top_layer += values[-1]
    return top_layer


# part 1
def get_answer_part_one(move_instruction, stack_layouts):
    for inst in move_instruction:
        instruction_values = re.findall(r'\d+', inst)
        num_stacks_to_move = int(instruction_values[0])  # number of stacks to move
        from_stack = int(instruction_values[1])          # move from stack
        to_stack = int(instruction_values[2])            # move to stack

        # remove '  ' in from_stack
        stack_parsed = [s for s in stack_layouts[from_stack] if s.strip()]
        stack_to_move = reversed(stack_parsed[-num_stacks_to_move:])
        stack_layouts[from_stack] = stack_layouts[from_stack][:-num_stacks_to_move]
        stack_layouts[to_stack] += stack_to_move

    return return_top_layer(stack_layouts)


print("Answer for part one:", get_answer_part_one(instructions, stack_layout))
# TLNGFGMFN


# part 2

# get original stack_layout
stack_layout = load_stack(stack_strings, num_stacks)


def get_answer_part_two(move_instruction, stack_layouts):
    for inst in move_instruction:
        instruction_values = re.findall(r'\d+', inst)
        num_stacks_to_move = int(instruction_values[0])
        from_stack = int(instruction_values[1])
        to_stack = int(instruction_values[2])

        # remove ' '
        stack_layouts[from_stack] = [s for s in stack_layouts[from_stack] if s.strip()]
        stack_layouts[to_stack] = [s for s in stack_layouts[to_stack] if s.strip()]

        stack_to_move = (stack_layouts[from_stack][-num_stacks_to_move:])
        stack_layouts[from_stack] = stack_layouts[from_stack][:-num_stacks_to_move]
        stack_layouts[to_stack] += stack_to_move

    return return_top_layer(stack_layouts)


print("Answer for part two:", get_answer_part_two(instructions, stack_layout))
# FGLQJCMBD