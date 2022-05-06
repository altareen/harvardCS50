###
#-------------------------------------------------------------------------------
# roster.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Nov 30, 2020
# Execution:    python roster.py Gryffindor
# Submit50:     submit50 cs50/problems/2020/x/houses
#
# This program produces a class roster from a sqlite database.
#
##

from sys import argv, exit
import csv

# TODO: Uncomment this before submitting
# from cs50 import SQL
# db = SQL("sqlite:///students.db")

# TODO: Comment this before submitting
import sqlite3
conn = sqlite3.connect("students.db")
db = conn.cursor()

if len(argv) != 2:
    print("Usage: python roster.py Gryffindor")
    exit(1)

# TODO: Before submitting, remove the tuple brackets
person = db.execute("SELECT first, middle, last, house, birth FROM students WHERE house = ? ORDER BY last", (argv[1], ))

# TODO: Before submitting, note that row is a dictionary in the CS50 IDE
for row in person:
    if row[1] != None:
        print(f"{row[0]} {row[1]} {row[2]}, born {row[4]}")
    else:
        print(f"{row[0]} {row[2]}, born {row[4]}")

# TODO: Comment this before submitting
conn.commit()
conn.close()

