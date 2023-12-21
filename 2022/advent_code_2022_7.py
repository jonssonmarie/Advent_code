import operator
from collections import defaultdict


def read_input_data():
    with open("input_data/input_day7", 'r') as f:
        file_system = f.read().split('\n')
        return file_system


filesystem = read_input_data()
file_path = []
directory_sizes = defaultdict(int)

size_limit = 100000
terminal_prompt = '$'
cd_command = 'cd'
root_dir = '/'
move_up_one_dir = '../..'
dir_label = 'dir'
list_command = 'ls'

# part one
# build file structure
for line in filesystem:
    line = line.split(' ')
    if line[0] == terminal_prompt:
        if line[1] == cd_command:
            if line[2] == root_dir:
                file_path = ['/']
            elif line[2] == move_up_one_dir:
                file_path.pop()  # pop out of path
            else:
                file_path.append(line[2])
    else:
        # check commands etc and add sizes
        if line[0] != dir_label:
            size = int(line[0])
            for i in range(len(file_path)):
                if i <= 1:  # equal or less than $ cd or $ ls
                    directory_sizes[file_path[i]] += size
                else:
                    parent = file_path[i - 1]
                    current = file_path[i]
                    dir_key = f"{parent} / {current}"
                    directory_sizes[dir_key] += size
    # calculate sum
    sum_sizes_less_limit = 0
    for size in directory_sizes.values():
        if size <= size_limit:
            sum_sizes_less_limit += size

print("part one answer:", sum_sizes_less_limit)

# part two
total_disk_space = 70000000
unused_space = 30000000

# find a directory you can delete that will free up enough space to run the update.
current_unused_space = total_disk_space - directory_sizes['/']
min_space_to_clear = unused_space - current_unused_space
sorted_directories = sorted(directory_sizes.items(), key=operator.itemgetter(1))  # iterate through items and return key

found_dir = [size for _, size in sorted_directories if size >= min_space_to_clear]
print("part tow answer directory size to delete:", min(found_dir))
