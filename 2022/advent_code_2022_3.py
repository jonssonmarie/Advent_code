import string
import pandas as pd

input_data = pd.read_csv("input_data/input_day3", sep=" ", header=None, skipinitialspace=True,
                         index_col=False).rename(columns={0: 'backpack_content'})

# split string in half check if duplicate
duplicates = []

for idx, row in input_data.iterrows():
    sep = len(row.backpack_content) // 2  # gives 1/2 length
    comp_1 = row.backpack_content[:sep]
    comp_2 = row.backpack_content[sep:]

    for elem in comp_1:
        if elem in comp_2:
            duplicates.append(elem)
            break

# letters position in alphabet give point
points = 0

for dupl_letter in duplicates:
    for i, letter in enumerate(string.ascii_letters, 1):
        if letter == dupl_letter:
            points += i

print(points)
