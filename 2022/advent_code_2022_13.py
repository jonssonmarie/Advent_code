"""
--- Day 13: Distress Signal ---
You climb the hill and again try contacting the Elves. However, you instead receive a signal you weren't expecting:
a distress signal.
Your handheld device must still not be working properly; the packets from the distress signal got decoded out of order.
You'll need to re-order the list of received packets (your puzzle input) to decode the message.

Your list consists of pairs of packets; pairs are separated by a blank line.
You need to identify how many pairs of packets are in the right order.
Each packet is always a list and appears on its own line.
When comparing two values, the first value is called left and the second value is called right.

Then:
- If both values are integers, the lower integer should come first.
If the left integer is lower than the right integer, the inputs are in the right order.
If the left integer is higher than the right integer, the inputs are not in the right order.
Otherwise, the inputs are the same integer; continue checking the next part of the input.
- If both values are lists, compare the first value of each list, then the second value, and so on.
If the left list runs out of items first, the inputs are in the right order.
If the right list runs out of items first, the inputs are not in the right order.
If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of
the input.
- If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then
retry the comparison.
For example, if comparing [0,0,0] and 2, convert the right value to [2]
(a list containing 2); the result is then found by instead comparing [0,0,0] and [2].

"""
import pandas as pd
from copy import deepcopy


def compare(first_lst, second_lst):
    """
    :param first_lst: first pairs of packets; pairs are separated by a blank line.
    :param second_lst: second pair of packets
    :return: -1 if the first_lst is bigger, 1 if the second_lst is bigger, 0 if they are the same
    """
    while len(first_lst) > 0 and len(second_lst) > 0:
        left = first_lst.pop(0)
        right = second_lst.pop(0)

        if type(left) == int and type(right) == int:
            if left < right:
                return 1
            elif left > right:
                return -1
        if type(left) == list and type(right) == list:
            nested = compare(left, right)
            if nested != 0:
                return nested
        if type(left) == list and type(right) == int:
            nested = compare(left, list([right]))
            if nested != 0:
                return nested
        if type(left) == int and type(right) == list:
            nested = compare(list([left]), right)
            if nested != 0:
                return nested
    if len(first_lst) < len(second_lst):
        return 1
    elif len(first_lst) > len(second_lst):
        return -1
    else:
        return 0


def read_data():
    with open("../../Advent_code_2022/input_data/input_day13", "r") as data:
        _data = data.readlines()
        parsed_data = [line.strip() for line in _data]
    return parsed_data


parsed = read_data()
"""
What are the indices of the pairs that are already in the right order? 
Determine which pairs of packets are already in the right order. What is the sum of the indices of those pairs?
"""
# part one
lst_correct = []
pairs_correct = []
i = 1

while len(parsed) > 0:
    first = eval(parsed.pop(0))
    second = eval(parsed.pop(0))

    if len(parsed) > 0:
        parsed.pop(0)  # funkade inte utan att ta pop på hela, måste ta bort dem efter att ha hämtat dem

    decoded_pairs = compare(first, second)
    if decoded_pairs == 1:
        lst_correct.append(i)
    i += 1

print(sum(lst_correct))


# part two
parsed = read_data()
idx_2 = 0
idx_6 = 0

while len(parsed) > 0:
    row = parsed.pop(0)

    if len(row) == 0:
        continue
    row = eval(row)

    if compare(deepcopy(row), [[2]]) == 1:
        idx_2 += 1
    if compare(deepcopy(row), [[6]]) == 1:
        idx_6 += 1

print(idx_2, idx_6)
position_of_2 = idx_2 + 1
position_of_6 = idx_6 + 2
print(f"{position_of_2 = }, {position_of_6 = }")
print("multiplication =", position_of_2 * position_of_6)
