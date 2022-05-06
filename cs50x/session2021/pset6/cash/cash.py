###
#-------------------------------------------------------------------------------
# cash.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 12, 2021
# Execution:    python3 cash.py
# Check50:      check50 cs50/problems/2021/x/sentimental/cash
# Submit50:     submit50 cs50/problems/2021/x/sentimental/cash
#
# This program calculates the minimum number of coins to be dispensed.
#
##

coins = 0
total = -1.0

while total < 0.0:
    total = float(input("Change owed: "))

total *= 100

while total > 0:
    if total//25 > 0:
        total -= 25
    elif total //10 > 0:
        total -= 10
    elif total//5 > 0:
        total -= 5
    elif total//1 > 0:
        total -= 1
    coins += 1

print(coins)


