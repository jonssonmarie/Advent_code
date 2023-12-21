"""
Day 4: Scratchcards

Part 1:
you have to figure out which of the numbers you have appear in the list of winning numbers.
The first match makes the card worth one point and each match after the first doubles the point value of that card.

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and
eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have,
four of them (48, 83, 17, and 86) are winning numbers!
That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches
after the first).
# ('|')
How many points are they worth in total?

Part 2:
There's no such thing as "points". Instead, scratchcards only cause you to win more scratchcards equal
to the number of winning numbers you have.
Specifically, you win copies of the scratchcards below the winning card equal to the number of matches.
So, if card 1 were to have 5 matching numbers, you would win one copy each of cards 1, 2, 3, 4, and 5.
Process all of the original and copied scratchcards until no more scratchcards are won.
Including the original set of scratchcards, how many total scratchcards do you end up with?
"""
from collections import defaultdict
from itertools import repeat
import numpy as np

data_path = "input_data/input_day_4"

data = open(data_path).read().strip()
lines = data.split('\n')

total_sum = 0
numbers_matched = []

for line in lines:
    card = line.split(':')[0]
    numbers = line.split(':')[1]

    # set to use fast compare
    first = set(numbers.split('|')[0].split())
    second = set(numbers.split('|')[1].split())

    # compare the two sets and get matches and the number of matches
    number_matches = len(first & second)

    if number_matches:
        total_sum += (2**(number_matches - 1))

    numbers_matched.append(number_matches)  # part 2

print("Answer part 1:", int(total_sum))

# Part 2
# create a list of 1 to be able to add copies of matches
num_cards = [1 for i in numbers_matched]

for i, matches in enumerate(numbers_matched):
    for k in range(matches):
        num_cards[i + 1 + k] += num_cards[i]

print("Answer part 2:", sum(num_cards))
