"""Day 15: Beacon Exclusion Zone """
import pandas as pd

file_name = "../../Advent_code_2022/input_data/input_day15"

# read data
data = pd.read_csv(file_name, header=None, delimiter=':')

# clean data for Sensor
data[["sensor_x", "sensor_y"]] = data[0].str.split(',', expand=True)
data["sensor_x"] = data["sensor_x"].str.replace('Sensor at x=', '').astype(int)
data["sensor_y"] = data["sensor_y"].str.replace('y=', '').astype(int)

# Clean data för beacon
data[["beacon_x", "beacon_y"]] = data[1].str.split(',', expand=True)
data["beacon_x"] = data["beacon_x"].str.replace('closest beacon is at x=', '').astype(int)
data["beacon_y"] = data["beacon_y"].str.replace('y=', '').astype(int)

# drop old columns
data = data.drop(columns=[0, 1], axis=1)


def check_beacon_zone(grid, sens_x, sens_y, dist, y_index):
    # checks a zone within y +/- manhattan distance and x +/- manhattan distance
    # if y = 2000000 then add x-coordinate else change the half width that creates a +/- change in x for
    # extend/reduce search in x.

    half_width = 0

    for y in range(sens_y - dist, sens_y + dist + 1):
        if y == y_index:
            for x in range(sens_x - half_width, sens_x + half_width + 1):
                grid.add(x)

        if y < sens_y:
            half_width += 1
        else:
            half_width -= 1


row_y = 2000000


def solve(df, y_index):
    # In the row where y=2000000, how many positions cannot contain a beacon?
    # loop each row to find if sensors y-coordinate overlap y=2000000
    lines_overlaps = set()
    device_line_overlaps = set()

    for label, col in df.iterrows():
        sensor_x = col.iloc[0]
        sensor_y = col.iloc[1]
        beacon_x = col.iloc[2]
        beacon_y = col.iloc[3]

        if sensor_y == y_index:
            device_line_overlaps.add(sensor_x)
        if beacon_y == y_index:
            device_line_overlaps.add(beacon_x)

        manhattan_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        if y_index in range(sensor_y - manhattan_distance, sensor_y + manhattan_distance):
            check_beacon_zone(lines_overlaps, sensor_x, sensor_y, manhattan_distance, y_index)

    print(len(lines_overlaps - device_line_overlaps))


solve(data, row_y)

"""
Part two
distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

you need to determine its tuning frequency, 
which can be found by multiplying its x coordinate by 4000000 
and then adding its y coordinate.

tuning_frequency = 4000000 * x_coordinate + y_coordinate

The x and y coordinates can each be at most 20. 
Find the only possible position for the distress beacon. What is its tuning frequency?
"""


