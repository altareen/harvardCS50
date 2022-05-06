###
#-------------------------------------------------------------------------------
# readability.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Nov 25, 2020
# Execution:    python3 readability.py
# Submit50:     submit50 cs50/problems/2020/x/sentimental/readability
#
# This program computes the approximate grade level needed to comprehend text.
#
##

# from cs50 import get_string
import string

passage = input("Text: ")
# passage = get_string("Text: ")

label = "Grade "
letters = 0
words = passage.count(" ") + 1
sentences = passage.count(".") + passage.count("!") + passage.count("?")

for item in passage:
    if item in string.ascii_letters:
        letters += 1

#print(f"{letters} letter(s)")
#print(f"{words} word(s)")
#print(f"{sentences} sentence(s)")

L = 100.0 * letters / words
S = 100.0 * sentences / words

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    label = "Before Grade 1"
    index = ""
elif index >= 16:
    label = "Grade 16+"
    index = ""

print(f"{label}{index}")

