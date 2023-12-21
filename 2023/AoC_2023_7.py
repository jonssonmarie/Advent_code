"""
Day 7: Camel Cards
Part 1
In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand.
A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:
Five of a kind, Four of a kind, Full house, Three of a kind, Two pair, One pair, High card

If two hands have the same type, a second ordering rule takes effect.
    Start by comparing the first card in each hand.
If these cards are different, the hand with the stronger first card is considered stronger.
    else, then move on to considering the second card in each hand.
If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand,
    then the fourth, then the fifth.

Each hand wins an amount equal to its bid multiplied by its rank
first step is to put the hands in order of strength

you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with
its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?

# part 2
J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.
To balance this, J cards are now the weakest individual cards, weaker even than 2.
A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example,
QJJQ2 is now considered four of a kind.

J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.
Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?

updated after solution was found. Looked at others to learn to write shorter code after solution.
"""

from collections import Counter
data_path = "input_data/input_day_7"
data = open(data_path).read().split('\n')

hands = []


def cards_weight(hand, part2=False):
    # replace T, J, Q, K, A with other symbols
    # ord take one char and give chars value, char convert from ascii to sign
    hand = hand.replace('T', chr(ord('9') + 1))
    if part2:
        hand = hand.replace('J', chr(ord('2') - 1))     # J = '1'
    else:
        hand = hand.replace('J', chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    count = Counter(hand)

    if part2:
        # extend card with the highest count with + 1 per J
        target = list(count.keys())[0]  # get the highest count for a value in the hand

        for item in count:
            # if no J
            if item != '1':
                if count[item] > count[target] or target == '1':
                    target = item
        # if J in hand and the highest count is not J
        if '1' in count and target != '1':
            count[target] += count['1']     # increase value for card eg. 2 Q become 3 Q
            del count['1']                  # delete J

    # calculate type
    if list(count.values()) == [5]:                     # five of a kind
        return 10, hand
    elif sorted(count.values()) == [1, 4]:              # four of a kind
        return 9, hand
    elif sorted(count.values()) == [2, 3]:              # full house (one pair, three of a kind)
        return 8, hand
    elif sorted(count.values()) == [1, 1, 3]:           # three
        return 7, hand
    elif sorted(count.values()) == [1, 2, 2]:           # two pair
        return 6, hand
    elif sorted(count.values()) == [1, 1, 1, 2]:        # one pair
        return 5, hand
    elif sorted(count.values()) == [1, 1, 1, 1, 1]:     # high card
        return 4, hand


# split data into sublists of cards and bid
for line in data:
    card, bid = line.split()
    hands.append((card, bid))


hand_sorted = sorted(hands, key=lambda cardbid: cards_weight(cardbid[0]))
hand_sorted2 = sorted(hands, key=lambda cardbid: cards_weight(cardbid[0], True))


def calculate_answer(sorted_hand):
    # calculate winnings, winnings = bid1 * rank1 + bid2 * rank2 + .. + bid1000 * rank1000
    answer = 0
    for i, (h, b) in enumerate(sorted_hand):
        answer += (i + 1) * int(b)
    return answer


print("Solution part 1:", calculate_answer(hand_sorted))
print("Solution part 2:", calculate_answer(hand_sorted2))
