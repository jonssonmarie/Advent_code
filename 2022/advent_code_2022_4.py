import pandas as pd

input_data = pd.read_csv("input_data/input_day4", sep=",", header=None, skipinitialspace=True,
                         index_col=False).rename(columns={0: 'elv1', 1: 'elv2'})

input_data[["start_1", "end_1"]] = input_data['elv1'].str.split("-", n=1, expand=True).astype('int16')
input_data[["start_2", "end_2"]] = input_data['elv2'].str.split("-", n=1, expand=True).astype('int16')

input_data['check_equal'] = input_data.eval('(start_1 <= start_2 and end_1 >= end_2)' or
                                            '(start_2 <= start_1 and end_2 >= end_1)')
print("part one: ", input_data['check_equal'].sum())

# part two

input_data['check_equal2'] = input_data.eval('(end_1 >= start_2 and end_2 >= start_1)')

print("part two:", input_data['check_equal2'].sum())

