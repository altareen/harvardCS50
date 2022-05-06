###
#-------------------------------------------------------------------------------
# readability.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 13, 2021
# Execution:    python3 readability.py
# Check50:      check50 cs50/problems/2021/x/sentimental/readability
# Submit50:     submit50 cs50/problems/2021/x/sentimental/readability
#
# This program computes the approximate grade level needed to read some text.
#
##

import string
prose = input("Text: ")

letters = 0
words = 0
sentences = 0

for item in prose:
    if item in string.ascii_letters:
        letters += 1
    elif item == " ":
        words += 1
    elif item in ".!?":
        sentences += 1

words += 1

#print(f"{letters} letter(s)")
#print(f"{words} word(s)")
#print(f"{sentences} sentence(s)")

L = 100.0 * letters / words
S = 100.0 * sentences / words

index = 0.0588 * L - 0.296 * S - 15.8

grade = round(index)

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")

