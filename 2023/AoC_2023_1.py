"""
Day 1: Trebuchet?!
Find first and last digit one each line, if one digit, repeat one time.
Collect these and then concat the strings eg. 2,1 become 21. If eg 39 is read then 3 and 9 shall be separated.
Then sum all.
"""

import re

data = "input_data/input_day_1"

all_numbers = []

with open(data) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        numbers = re.findall(r'\d+', line)
        all_numbers_line = []

        for num in numbers:
            if len(num) > 1:
                for n in num:
                    number = n
                    all_numbers_line.append(number)
            else:
                number = num
                all_numbers_line.append(number)

        all_numbers.append(all_numbers_line)

all_sum = []
for part_num in all_numbers:
    # concat two strings, then convert to integer
    score = int(part_num[0] + part_num[-1])
    all_sum.append(score)
print("Answer part 1", sum(all_sum))

""" 
part two
some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

"""
found_numbers = []
answer_2 = 0
with open(data) as file:
    lines = file.readlines()

    words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    for line in lines:
        all_digits = []
        line = line.strip()

        for i, char in enumerate(line):
            if char.isdigit():
                all_digits.append(char)
            for digit, word in words.items():
                if line[i:].startswith(word):
                    all_digits.append(str(digit))

        score = int(all_digits[0]+all_digits[-1])
        answer_2 += score

print("Answer part 2", answer_2)
