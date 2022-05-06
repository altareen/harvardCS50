###
#-------------------------------------------------------------------------------
# application.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Mar 14, 2021
#
# Venv setup:       python3 -m venv venv
# Venv activation:  source venv/bin/activate
#
# Install sqlalchemy:   pip install -r requirements.txt
#
# Key:          export DATABASE_URL=postgres://tdpmrxyzqtyhfx:6d929e192d129a30f2fe22aec6afcf7ee2846995a004b6b5d497ffd863b31065@ec2-52-7-115-250.compute-1.amazonaws.com:5432/d79r0a8uiur6km
# Execution:    python3 importdata.py
# Conclusion:   deactivate
#
# This program populates existing database tables with data from a CSV file.
#
##

import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    f.readline()
    reader = csv.reader(f)
    unique_authors = set()
    for isbn, title, author, year in reader:
        unique_authors.add(author)
    for author in unique_authors:    
        db.execute("INSERT INTO authors (name) VALUES (:name)", {"name": author})
    db.commit()
    f.close()
    
    f = open("books.csv")
    f.readline()
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        rows = db.execute("SELECT id FROM authors WHERE name = :name", {"name": author}).fetchall()
        author_id = rows[0]["id"]
        db.execute("INSERT INTO books (year, title, isbn, author_id) VALUES (:year, :title, :isbn, :author_id)", {"year": year, "title": title, "isbn": isbn, "author_id": author_id})
    db.commit()
    f.close()

if __name__ == "__main__":
    main()


