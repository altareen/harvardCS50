###
#-------------------------------------------------------------------------------
# credit.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 13, 2021
# Execution:    python3 credit.py
# Check50:      check50 cs50/problems/2021/x/sentimental/credit
# Submit50:     submit50 cs50/problems/2021/x/sentimental/credit
#
# This program determines whether a credit card number is valid.
#
##

#card = "4003600000000014"
#card = "378282246310005"
card = input("Number: ")

first = 0
second = 1

if len(card)%2 == 1:
    first = 1
    second = 0

total = 0
for num in range(first, len(card), 2):
    partial = 2 * int(card[num])
    if partial > 9:
        total += int(str(partial)[0]) + int(str(partial)[1])
    else:
        total += partial

for num in range(second, len(card), 2):
    total += int(card[num])

if str(total)[-1] != "0":
    print("INVALID")
elif len(card) == 15 and (card[:2] == "34" or card[:2] == "37"):
    print("AMEX")
elif len(card) == 16 and (50 < int(card[:2]) < 56):
    print("MASTERCARD")
elif (len(card) == 13 or len(card) == 16) and card[0] == "4":
    print("VISA")

