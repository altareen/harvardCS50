###
#-------------------------------------------------------------------------------
# application.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Mar 14, 2020
#
# Venv setup:       python3 -m venv venv
# Venv activation:  source venv/bin/activate
#
# Check if flask is installed:  python -m flask --version
# Install requirements:         pip install -r requirements.txt
#
# Set variable: export FLASK_APP="application.py"
# Execution:    flask run
# Conclusion:   deactivate
#
# This program implements a book search engine.
#
##

import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Make sure the DATABASE_URI environment variable is set
if not os.environ.get("DATABASE_URI"):
    raise RuntimeError("DATABASE_URI not set")

# Configure application to use PostgreSQL database
engine = create_engine(os.getenv("DATABASE_URI"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/title", methods=["GET", "POST"])
def title():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Lookup the information corresponding to the book title
        title = request.form.get("title").lower()

        rows = db.execute("SELECT * FROM authors JOIN books ON authors.id=books.author_id WHERE LOWER(title) LIKE :title", {"title": '%'+title+'%'}).fetchall()
        quantity = len(rows)

        return render_template("retrieve.html", rows=rows, quantity=quantity)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("title.html")


@app.route("/author", methods=["GET", "POST"])
def author():
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Lookup the information corresponding to the book title
        author = request.form.get("author").lower()

        rows = db.execute("SELECT * FROM authors JOIN books ON authors.id=books.author_id WHERE LOWER(name) LIKE :name", {"name": '%'+author+'%'}).fetchall()
        quantity = len(rows)

        return render_template("retrieve.html", rows=rows, quantity=quantity)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("author.html")


