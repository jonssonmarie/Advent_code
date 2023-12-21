import pandas as pd

grid = pd.read_csv("input_data/input_day8", header=None)[0]\
    .str.split("", expand=True).drop(labels=[0, 100], axis=1)

grid.columns = [i for i in range(0, 99)]

len_rows = len(grid.index)
len_columns = len(grid.columns)

# edges are already visible therefore added to total
all_edges = (len_rows * 2) + ((len_columns - 2) * 2) # 1 top and 1 bottom therefore times 2 , - 2 to not count corners twice
all_total = all_edges

all_scenic_scores = []

for row in range(1, len_rows - 1):
    for col in range(1, len_columns - 1):
        tree = grid[row][col]

        # get all horizontal and vertical trees
        left = [grid[row][col - i] for i in range(1, col + 1)]
        right = [grid[row][col + i] for i in range(1, len_columns - col)]
        up = [grid[row - i][col] for i in range(1, row+1)]
        down = [grid[row + i][col] for i in range(1, len_rows - row)]

        # part one
        if max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree:
            all_total += 1

        # part two
        score = 1  # track scenic scores
        for lst in (left, right, up, down):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                elif lst[i] >= tree:  # can not see beyond tree if equal therefore break
                    tracker += 1
                    break

            score *= tracker

        all_scenic_scores.append(score)
print("Answer part one:", all_total)
print("Answer part two:", max(all_scenic_scores))
