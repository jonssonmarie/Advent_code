"""
The CPU has a single register, X, which starts with the value 1.
It supports only two instructions:
addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
noop takes one cycle to complete. It has no other effect.

For now, consider the signal strength (the cycle number multiplied by the value of the X register)
during the 20th cycle and every 40 cycles after that
(that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
What is the sum of these six signal strengths?
"""


import pandas as pd

input_data = pd.read_csv("input_data/input_day10", sep=" ", header=None, skipinitialspace=True,
                         index_col=False).rename(columns={0: 'instruction', 1: "value_V"})

# part one
values = [1]

for idx, data in input_data.iterrows():
    values.append(int(values[-1]))
    if data.instruction == 'addx':
        values.append(int(data.value_V) + values[-1])


total = []

for x in range(20, 240, 40):
    total.append(x * values[x-1])

print("Answer day 10:", sum(total))


# part two, modulus fick jag goggla
for i in range(len(values)):
    if abs((values[i] - i % 40)) <= 1:
        print("#", end='')
    else:
        print(' ', end='')
    if (i + 1) % 40 == 0:
        print("\n", end='')
    else:
        print(' ', end='')
