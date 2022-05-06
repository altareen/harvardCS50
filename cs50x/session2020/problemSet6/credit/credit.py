###
#-------------------------------------------------------------------------------
# credit.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Nov 24, 2020
# Execution:    python3 credit.py
# Submit50:     submit50 cs50/problems/2020/x/sentimental/credit
#
# This program determines whether a provided credit card number is valid
# according to Luhn’s algorithm.
#
##

# from cs50 import get_string

digits = input("Number: ")
# digits = get_string("Number: ")

total = 0
result = "INVALID"

if len(digits)%2 == 0:
    first, second = 0, 1
else:
    first, second = 1, 0

for i in range(first, len(digits), 2):
    product = int(digits[i]) * 2
    if product > 9:
        partial = str(product)
        total += int(partial[0]) + int(partial[1])
    else:
        total += product

for i in range(second, len(digits), 2):
    total += int(digits[i])

if int(str(total)[-1]) == 0:
    if len(digits)==15 and (digits[:2]=="34" or digits[:2]=="37"):
        result = "AMEX"
    elif len(digits)==16 and digits[0]=="5" and (digits[1] in "12345"):
        result = "MASTERCARD"
    elif (len(digits)==13 or len(digits)==16) and digits[0]=="4":
        result = "VISA"

print(result)

