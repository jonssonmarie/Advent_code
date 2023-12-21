"""
--- Day 16: The Floor Will Be Lava ---

empty space (.), beam continues in the same direction.
mirrors (/ and \), beam is reflected 90 degrees depending on the angle of the mirror
splitters (| and -),
If the beam encounters the pointy end of a splitter (| or -)
beam passes through the splitter as if the splitter were empty space.
If the beam encounters the flat side of a splitter (| or -),
the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing.

The light isn't energizing enough tiles to produce lava; to debug the contraption,
you need to start by analyzing the current situation.
With the beam starting in the top-left heading right, how many tiles end up being energized?

"""

data_path = "input_data/input_day_16"

data = open(data_path).read().strip()
lines = [[l for l in line] for line in data.split('\n')]

ROW = len(lines)
COL = len(lines[0])

dir_r = [-1, 0, 1, 0]
dir_c = [0, 1, 0, -1]
# memo_key_nr = [0, 1, 2, 3]  # up, right, down, left


def update(r, c, d):
    r_ = r + dir_r[d]
    c_ = c + dir_c[d]
    return r_, c_, d


def send_beam(sr, sc, sd):
    pos = [(sr, sc, sd)]
    visited_tiles = set()
    memo = set()  # memo to not rerun that specific r,c d (DP)
    t = True
    while t:
        new_pos = []
        if not pos:
            break

        for (r, c, d) in pos:       # d = wanted dir

            if 0 <= r < ROW and 0 <= c < COL:
                visited_tiles.add((r, c))
                ch = lines[r][c]

                if (r, c, d) in memo:
                    continue
                memo.add((r, c, d))

                if ch == '.':
                    new_pos.append(update(r, c, d))  # keep going in current direction

                elif ch == '/':
                    new_pos.append(update(r, c, {0: 1, 1: 0, 2: 3, 3: 2}[d]))  # key = current dir, value = new dir

                elif ch == '\\':
                    new_pos.append(update(r, c, {0: 3, 1: 2, 2: 1, 3: 0}[d]))

                elif ch == '|':
                    if d in [0, 2]:  # up, down then pass through else split beam
                        new_pos.append(update(r, c, d))
                    else:
                        new_pos.append(update(r, c, 0))
                        new_pos.append(update(r, c, 2))

                elif ch == '-':
                    if d in [1, 3]:  # right, left pass through else split beam
                        new_pos.append(update(r, c, d))
                    else:
                        new_pos.append(update(r, c, 1))
                        new_pos.append(update(r, c, 3))
                else:
                    t = False
        pos = new_pos

    return len(visited_tiles)


print("Part 1: ", send_beam(0, 0, 1))

answer = 0

# Part 2 calculate which beam configuration creates the most energized tiles
for r in range(ROW):
    answer = max(answer, send_beam(r, 0, 1))           # 1 move to right, as part 1
    answer = max(answer, send_beam(r, COL - 1, 3))     # 3 move to left

for c in range(COL):
    answer = max(answer, send_beam(0, c, 2))           # 2 move down
    answer = max(answer, send_beam(ROW - 1, c, 0))     # 0 move up

print("Part 2:", answer)

