"""
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

import pandas as pd
import numpy as np

input_df = pd.read_csv("input_day1", sep=" ", header=None, skip_blank_lines=False)
input_df.columns = ["calories"]

c = input_df['calories'].isna()
s = c.cumsum()
df_dict = dict(iter(input_df['calories'].groupby(s)))

list_key_sum = []

for key, value in df_dict.items():
    print(value)
    sum_cal = np.sum(value)
    comb = [key, sum_cal]
    list_key_sum.append(comb)

max_df = pd.DataFrame(list_key_sum, columns=["elv", "sum_calories"])

max_cal = pd.eval(max_df['sum_calories'].max())
query = max_df.query(f"sum_calories == {max_cal}")
print("Max calories carried by elv: ", query)
