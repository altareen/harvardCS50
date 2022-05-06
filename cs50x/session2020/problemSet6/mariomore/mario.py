###
#-------------------------------------------------------------------------------
# mario.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Nov 24, 2020
# Execution:    python3 mario.py
# Submit50:     submit50 cs50/problems/2020/x/sentimental/mario/more
#
# This program creates a pyramid of hash marks.
#
##

height = input("Height: ")
while height not in "12345678" or height == "":
    height = input("Height: ")

height = int(height)
offset = height-1
for level in range(1, height+1):
    for space in range(offset, 0, -1):
        print(" ", end="")
    for item in range(level):
        print("#", end="")
    print("  ", end="")
    for item in range(level):
        print("#", end="")
    print()
    offset -= 1

