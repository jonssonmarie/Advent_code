"""
the start of a packet is indicated by a sequence of four characters that are all different.
your subroutine needs to identify the first position where the four most recently received characters were all different.
needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.
For example, suppose you receive the following datastream buffer:
mjqjpqmgbljsphdztnvjfqwrcgsmlb

The first time a marker could occur is after the fourth character is received,
making the most recent four characters mjqj.
Because j is repeated, this isn't a marker.  - find distinct set of letters

part two : 14 distinct characters
"""
# part one  first time a marker could occur is after the 4 character is received
with open("input_data/input_day6", 'r') as f:
    datastream = f.readline().strip()

for i in range(len(datastream)):
    if len(set(datastream[i:i + 4])) == 4:
        print(i + 4)
        break

# part two first time a marker could occur is after the 14 character is received
for i in range(len(datastream)):
    if len(set(datastream[i:i + 14])) == 14:
        print(i + 14)
        break
