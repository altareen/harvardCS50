###
#-------------------------------------------------------------------------------
# dna.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 13, 2021
# Execution:    python3 dna.py databases/large.csv sequences/5.txt
# Check50:      check50 cs50/problems/2021/x/dna
# Submit50:     submit50 cs50/problems/2021/x/dna
#
# This program identifies a person based on their specific DNA sequence.
#
##

import csv
import sys

def main():
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py DATABASE SEQUENCE")

    signatures = dict()
    with open(sys.argv[1], "r") as fhand:
        content = list(csv.reader(fhand))

    STR = content[0][1:]
    counts = content[1:]

    for item in counts:
        signatures[tuple([int(x) for x in item[1:]])] = item[0]

    with open(sys.argv[2], "r") as fhand:
        dna = fhand.read()

    repeats = [0] * len(STR)
    
    for i in range(len(STR)):
        for j in range(len(dna) // len(STR[i])):
            if STR[i]*j in dna:
                repeats[i] = j

    repeats = tuple(repeats)
    result = signatures.get(repeats, "No match")
    print(result)    

if __name__ == "__main__":
    main()

