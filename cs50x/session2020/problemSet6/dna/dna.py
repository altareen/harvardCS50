###
#-------------------------------------------------------------------------------
# dna.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Nov 25, 2020
# Execution:    python3 dna.py databases/small.csv sequences/1.txt
# Submit50:     submit50 cs50/problems/2020/x/dna
#
# This program identifies a person based on their DNA sequence.
#
##

from sys import argv, exit
import csv

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

sequence = ""
profiles = {}
with open(argv[2], "r") as fhand:
    sequence = fhand.read().rstrip()

with open(argv[1], "r", newline="") as fhand:
    content = list(csv.reader(fhand))

tandems = content.pop(0)
del tandems[0]

for item in content:
    profiles[tuple([int(x) for x in item[1:]])] = item[0]

result = []
for item in tandems:
    largest = 0
    chunks = len(sequence)//len(item)
    for trial in range(1, chunks+1):
        expand = item * trial
        exists = sequence.find(expand)
        if exists != -1 and trial > largest:
            largest = trial
    result.append(largest)

person = profiles.get(tuple(result), "No match")
print(person)

