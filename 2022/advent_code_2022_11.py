import re

"""
In the above example, the first round proceeds as follows:
Monkey 0:
  Monkey inspects an item with a worry level of 79.
    Worry level is multiplied by 19 to 1501.
    Monkey gets bored with item. Worry level is divided by 3 to 500.
    Current worry level is not divisible by 23.
    Item with worry level 500 is thrown to monkey 3.
  Monkey inspects an item with a worry level of 98.
    Worry level is multiplied by 19 to 1862.
    Monkey gets bored with item. Worry level is divided by 3 to 620.
    Current worry level is not divisible by 23.
    Item with worry level 620 is thrown to monkey 3.

Count the total number of times each monkey inspects items over 20 rounds:
Collect the two most active monkeys inspected items. 
The level of monkey business in this situation can be found by multiplying these items together
"""


def read_file():
    file_input = open("input_data/input_day11", "r")
    parsed_input = file_input.read().strip().split('\n\n')

    return parsed_input


monkey_num = 0
operation = {}
starting_items = {}
test = {}
test_if_true = {}
test_if_false = {}
num_handle_items = {}

# read file and split data
for row in read_file():
    data = row.split("\n")
    num_handle_items[monkey_num] = 0
    for elem in data:
        if 'Operation' in elem:
            operation[monkey_num] = elem[23:]
        elif 'Starting' in elem:
            starting_items[monkey_num] = re.findall(r'\d+', elem)
        elif 'Test' in elem:
            test[monkey_num] = re.findall(r'\d+', elem)[0]
        elif 'true' in elem:
            test_if_true[monkey_num] = re.findall(r'\d+', elem)[0]
        elif 'false' in elem:
            test_if_false[monkey_num] = re.findall(r'\d+', elem)[0]
    monkey_num += 1


def monkey_update(monkey_to_update, new_level_bored_monkey):
    """
    Append bored monkey level to new monkey
    :param monkey_to_update: monkey to update
    :param new_level_bored_monkey:
    :return:
    """
    temp_lst = list(starting_items[monkey_to_update])
    temp_lst.append(str(new_level_bored_monkey))
    return temp_lst


def remove_first_item(monkey_number):
    """
    Remove the first item in the monkeys list who passed level forward to update_monkey_num
    :param monkey_number: monkey number
    :return: None
    """
    temp_starting_items = list(starting_items[monkey_number])
    del temp_starting_items[0]
    starting_items[monkey_number] = temp_starting_items


def check_bool(worry_level, num):
    """
    :param worry_level: level of worry depending on each monkey
    :param num: monkey number
    :return: None
    """
    new_level_bored_monkey = worry_level // 3
    check_bool = new_level_bored_monkey % int(test[num])

    if not check_bool:
        update_monkey_num = int(test_if_true[num])
        starting_items[update_monkey_num] = monkey_update(update_monkey_num, new_level_bored_monkey)
        remove_first_item(num)
        num_handle_items[num] = num_handle_items[num] + 1
    else:
        update_monkey_num = int(test_if_false[num])
        starting_items[update_monkey_num] = monkey_update(update_monkey_num, new_level_bored_monkey)
        remove_first_item(num)
        num_handle_items[num] = num_handle_items[num] + 1


for i in range(20):
    for num in range(monkey_num):
        if len(starting_items[num]) > 0:
            for _ in starting_items[num]:
                _ = int(_)

                if '+' in operation[num] and 'old' not in operation[num]:
                    worry_level = _ + int(re.findall(r'\d+', operation[num])[0])
                    check_bool(worry_level, num)

                elif '*' in operation[num] and 'old' not in operation[num]:
                    worry_level = _ * int(re.findall(r'\d+', operation[num])[0])
                    check_bool(worry_level, num)

                elif '*' in operation[num] and 'old' in operation[num]:
                    worry_level = _ * _
                    check_bool(worry_level, num)

                elif '+' in operation[num] and 'old' in operation[num]:
                    worry_level = _ + _
                    check_bool(worry_level, num)


print("num_handle_items", num_handle_items, "\n")

num_handle_items_values = []
for key, value in num_handle_items.items():
    num_handle_items_values.append(value)

num_handle_items_values.sort(reverse=True)
two_max = num_handle_items_values[0:2]
num_handle_items_max = two_max[0] * two_max[1]

print("multiplying =", num_handle_items_max)
