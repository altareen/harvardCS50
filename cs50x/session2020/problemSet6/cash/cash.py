###
#-------------------------------------------------------------------------------
# cash.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Nov 24, 2020
# Execution:    python3 cash.py
# Submit50:     submit50 cs50/problems/2020/x/sentimental/cash
#
# This program calculates the minimum number of coins required to give a user
# change.
#
##

# from cs50 import get_float

total = float(input("Change owed: "))
# total = get_float("Change owed: ")

while total < 0.0:
    total = float(input("Change owed: "))
    # total = get_float("Change owed: ")

total = int(total*100)
coins = 0

while total > 0:
    if total//25 > 0:
        total -= 25
    elif total//10 > 0:
        total -= 10
    elif total//5 > 0:
        total -= 5
    elif total//1 > 0:
        total -= 1
    coins += 1

print(coins) 

