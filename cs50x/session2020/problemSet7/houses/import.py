###
#-------------------------------------------------------------------------------
# import.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Nov 30, 2020
# Execution:    python import.py characters.csv
# Submit50:     submit50 cs50/problems/2020/x/houses
#
# This program imports student data from a CSV file into a sqlite database.
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
    print("Usage: python import.py characters.csv")
    exit(1)

with open(argv[1], "r", newline="") as fhand:
    content = csv.DictReader(fhand)
    for row in content:
        person = row["name"].split()
        # TODO: Remove the tuple brackets from the inserting data, before submitting
        if len(person) == 2:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", (person[0], None, person[1], row["house"], int(row["birth"])))
        elif len(person) == 3:
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", (person[0], person[1], person[2], row["house"], int(row["birth"])))

# TODO: Comment this before submitting
conn.commit()
conn.close()

