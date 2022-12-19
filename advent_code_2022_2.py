"""
The score for a single round is the score for the shape you selected
1 for Rock,
2 for Paper,
3 for Scissors
plus the score for the outcome of the round
0 if you lost,
3 if the round was a draw,
6 if you won.

strategy guide:
A Y
B X
C Z

Opponent:
A for Rock,
B for Paper,
C for Scissors.

You:
X for Rock,
Y for Paper,
Z for Scissors.

What would your total score be if everything goes exactly according to your strategy guide?
"""
import pandas as pd

input_data = pd.read_csv("input_data/input_day2", sep="\t", header=None, skip_blank_lines=False, index_col=False)[0]\
    .str.split(" ", expand=True).rename(columns={0: "opponent", 1: "you"})

input_data['you'] = input_data['you'].replace({'X': 'A', 'Y': 'B', 'Z': 'C'})

draw = input_data.query('opponent == you')
draw_A = len(draw.query('opponent== "A"'))
draw_B = len(draw.query('opponent== "B"'))
draw_C = len(draw.query('opponent== "C"'))

shape_A_C = input_data.query('opponent == "A" and you == "C"')  # rock, scissor op win
shape_A_B = input_data.query('opponent == "A" and you == "B"')  # rock, paper   you win
shape_B_A = input_data.query('opponent == "B" and you == "A"')  # paper, rock   op win
shape_B_C = input_data.query('opponent == "B" and you == "C"')  # paper, scissor    you win
shape_C_A = input_data.query('opponent == "C" and you == "A"')  # scissor, rock     you win
shape_C_B = input_data.query('opponent == "C" and you == "B"')  # scissor, paper    op win

your_score = len(draw) * 3 + draw_A * 1 + draw_B * 2 + draw_C * 3 + len(shape_A_B) * (2 + 6) \
             + len(shape_B_C) * (3 + 6) + len(shape_C_A) * (1 + 6) + len(shape_A_C) * 3 + len(shape_B_A) * 1 \
             + len(shape_C_B) * 2

print(your_score)
