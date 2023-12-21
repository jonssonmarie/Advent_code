"""
Day 16: Proboscidea Volcanium
"""

import pandas as pd

file_name = "../../Advent_code_2022/input_data/input_day16"

data = pd.read_csv(file_name, header=None, delimiter=';')

data[['Valve', 'flow_rate']] = data[0].str.split('=', expand=True)
data['Valve'] = data['Valve'].str.replace('Valve', '').str.replace('has flow rate', '')
data['tunnels_lead_to_valve'] = data[1].str.replace('tunnels lead to valves ', '')\
                                       .str.replace('tunnel leads to valve ', '')

data = data.drop(columns=[0, 1])
print()

