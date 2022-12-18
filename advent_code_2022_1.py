"""
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

import pandas as pd
import numpy as np

input_df = pd.read_csv("input_data/input_day1", sep=" ", header=None, skip_blank_lines=False)
input_df.columns = ["calories"]

check_nan_bool = input_df['calories'].isna()    # set True or False
cluster_input = check_nan_bool.cumsum()         # Return the cumulative sum of the elements along a given axis.

df_dict = dict(iter(input_df['calories'].groupby(cluster_input)))
# iter(obj, sentinel)
# obj : Object which has to be converted to iterable ( usually an iterator )
# sentinel : value used to represent end of sequence.

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
