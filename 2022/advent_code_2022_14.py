"""
Regolith Reservoir
"""
import numpy as np

file_name = "../../Advent_code_2022/input_data/input_day14"


def create_rocks(file):
    """
    converted . # and o to numbers .= 0, # = 1, o = 2
    :param file: file and path
    :return: max_y, maximum length in y from the input file
    """
    with open(file, 'r') as data:
        lines = data.readlines()
        lines = [pos.strip() for pos in lines]

        # create grid, used numpy array since I got fragmented dataframe warning
        cave = np.zeros((1000, 200))
        max_y = 0

        for sublist in lines:
            sublist = sublist.split(' -> ')

            for elem in range(len(sublist) - 1):
                first_coord, sec_coord = sublist[elem], sublist[elem + 1]
                all_x = [int(first_coord.split(',')[0]), int(sec_coord.split(',')[0])]
                all_y = [int(first_coord.split(',')[1]), int(sec_coord.split(',')[1])]
                for x in range(min(all_x), max(all_x) + 1):
                    for y in range(min(all_y), max(all_y) + 1):
                        if y > max_y:
                            max_y = y
                        cave[x, y] = 1
    return max_y, cave


def add_sand(df, coordinate):
    """
    add sand at the coordinate
    :param df: grid file
    :param coordinate: the coordinate to add sand to
    :return: updated grid file
    """
    if df[coordinate[0], coordinate[1]] == 0:
        df[coordinate[0], coordinate[1]] = 2
    return df


def move(df, coordinate, max_y):
    """
    check which move to perform and send the coordinate back
    :param df: gird file
    :param coordinate: coordinate to check if possible to move to or not
    :return: coordinate or (-1,-1) which means end
    """

    while coordinate[1] + 1 <= max_y:

        # straight down
        if df[coordinate[0], coordinate[1] + 1] == 0:
            coordinate = (coordinate[0], coordinate[1] + 1)

        # 1 step down and left
        elif df[coordinate[0] - 1, coordinate[1] + 1] == 0:
            coordinate = (coordinate[0] - 1, coordinate[1] + 1)

        # 1 step down and right
        elif df[coordinate[0] + 1, coordinate[1] + 1] == 0:
            coordinate = (coordinate[0] + 1, coordinate[1] + 1)

        else:
            return coordinate
    return (-1, -1)


def move2(df, coordinate, max_y):
    """
    check which move to perform and send the coordinate back for part two
    :param df: grid file
    :param coordinate: coordinate to check if possible to move to or not
    :return: coordinate
    """

    while coordinate[1] + 1 < max_y + 2:

        # straight down
        if df[coordinate[0], coordinate[1] + 1] == 0:
            coordinate = (coordinate[0], coordinate[1] + 1)

        # 1 step down and left
        elif df[coordinate[0] - 1, coordinate[1] + 1] == 0:
            coordinate = (coordinate[0] - 1, coordinate[1] + 1)

        # 1 step down and right
        elif df[coordinate[0] + 1, coordinate[1] + 1] == 0:
            coordinate = (coordinate[0] + 1, coordinate[1] + 1)

        else:
            return coordinate
    return coordinate


def pour_sand(coordinate):
    """
    start to pour sand from 500, 0.
    :param coordinate: coordinate to start with
    :return: number of tiles before sand start to flow into the abyss
    """
    max_y, cave = create_rocks(file_name)
    tiles = 0
    new_coordinate = move(cave, coordinate, max_y)

    while new_coordinate != (-1, -1):
        cave = add_sand(cave, new_coordinate)
        tiles += 1

        new_coordinate = move(cave, coordinate, max_y)
    return tiles


tiles = pour_sand((500, 0))
print("Number of tiles before sand start to flow into the cabyss:", tiles)


def pour_sand_2(coordinate):
    """
    start to pour sand from 500, 0
    :param coordinate: coordinate to check
    :return: number of tiles when stopping the flow of sand into the cave.
    """
    max_y, cave = create_rocks(file_name)

    tiles2 = 0
    new_coordinate = move2(cave, coordinate, max_y)

    while cave[500, 0] == 0:
        cave = add_sand(cave, new_coordinate)
        tiles2 += 1
        new_coordinate = move2(cave, coordinate, max_y)
    return tiles2


tiles2 = pour_sand_2((500, 0))
print("Number of tiles before sand start to flow into the cabyss:", tiles2)
