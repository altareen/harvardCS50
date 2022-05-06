###
#-------------------------------------------------------------------------------
# application.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 18, 2021
# Execution:    flask run
# Submit50:     submit50 cs50/labs/2021/x/birthdays
#
# This program implements a website via which users can track their birthdays.
#
##

import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))

        # Insert the birthday into the database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        # Return to the homepage
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        results = db.execute("SELECT name, month, day FROM birthdays")

        # Render the homepage
        return render_template("index.html", results=results)



