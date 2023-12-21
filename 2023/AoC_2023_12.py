"""
Day 12: Hot Springs

spring : operational (.) or damaged (#) or simply unknown (?).
Also duplicate for some of this information in a different format!

This list always accounts for every damaged spring, and each number is the entire size of its contiguous group
(that is, groups are always separated by at least one operational spring: #### would always be 4, never 2,2)

For each row, count all of the different arrangements of operational and broken springs that meet the given criteria.
What is the sum of those counts?

kolla row len
kolla springdata tex 3,1,1
kolla antal platser som är upptagna med . och # och ?
kolla pos ?
kolla antal # se var ? ska bli map springdata och hur # & ? sitter per row.
Sen räkna ut kombinationer per rad

Beräkning:
antalet kombinationer då k element av n element väljs:   Där k är ? och n är spring_data

P(n,k) = n! / (n − k)! * k!
där 0 ≤ k ≤ n.

"""
data_path = "input_data/input_day_12"


def num_arrangements(springrow, condition):
    table = {}

    # dynamic programming with memoization in the table, goes quick but take a lot of memory

    def num_arr(i, j):
        # i = springrow length, j = condition legth (numbers)
        # subroutine to find num of arrangements, restrict to first i characters, and first j nums
        # choose to search from right to left
        if (i, j) in table:  # table to be searched if already run
            return table[(i, j)]
        if i == 0 and j == 0:
            return 1  # only one way to satisfy, both are empty
        elif i == 0:  # empty string can not match anything
            return 0
        elif j == 0:  # no numbers, means springs are working, all springs is wanted . and ? as result
            return int(all(char != '#' for char in springrow[:i]))
        elif springrow[i - 1] == '.':
            result = num_arr(i - 1, j)

        else:
            num = condition[j - 1]  # take the last number

            if num > i or any(char == '.' for char in springrow[i - num: i]):
                result = 0  # not possible numbers can not be bigger than len(springrow)
                # and . is not allowed within the length of condition item
            elif i > num and springrow[i - num - 1] == '#':
                result = 0  # not matched
            else:
                result = num_arr(max(i - num - 1, 0), j - 1)
            if springrow[i - 1] == '?':
                result += num_arr(i - 1, j)

        table[(i, j)] = result      # save in table to be able to find result quicker
        return result

    return num_arr(len(springrow), len(condition))


total1 = 0
total2 = 0

data = open(data_path).read().strip().split('\n')
lines = [line for line in data]
for line in lines:
    l1, r = line.strip().split()
    r1 = tuple(int(x) for x in r.split(','))
    l2 = '?'.join([l1] * 5)
    r2 = r1 * 5
    total1 += num_arrangements(l1, r1)
    total2 += num_arrangements(l2, r2)

# part 1
print(total1)

# part 2
print(total2)


# must be . inbetween damage springs and ?, ? can also be . or #

"""
#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1

???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
