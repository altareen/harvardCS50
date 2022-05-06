###
#-------------------------------------------------------------------------------
# application.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Mar 03, 2021
#
# Venv setup:       python3 -m venv venv
# Venv activation:  source venv/bin/activate
#
# Check if flask is installed:  python -m flask --version
# If flask is not installed:    pip install -r requirements.txt
#
# Set variable: export FLASK_APP="application.py"
# Execution:    flask run
# Conclusion:   deactivate
#
# This program implements a tic-tac-toe game.
#
##

from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
        session["status"] = "moves"

    return render_template("game.html", game=session["board"], turn=session["turn"], status=session["status"])


@app.route("/play/<int:row>/<int:col>")
def play(row, col):

    # Place player symbol into its position on the game board
    session["board"][row][col] = session["turn"]

    # Check for a game winning condition
    if session["board"][0] == list(session["turn"]*3) or \
    session["board"][1] == list(session["turn"]*3) or \
    session["board"][2] == list(session["turn"]*3) or \
    [session["board"][0][0], session["board"][1][0], session["board"][2][0]] == list(session["turn"]*3) or \
    [session["board"][0][1], session["board"][1][1], session["board"][2][1]] == list(session["turn"]*3) or \
    [session["board"][0][2], session["board"][1][2], session["board"][2][2]] == list(session["turn"]*3) or \
    [session["board"][0][0], session["board"][1][1], session["board"][2][2]] == list(session["turn"]*3) or \
    [session["board"][0][2], session["board"][1][1], session["board"][2][0]] == list(session["turn"]*3):
        session["status"] = "wins"
    # Check for a tied game
    elif None not in session["board"][0] and None not in session["board"][1] and None not in session["board"][2]:
        session["status"] = "ties"
    # Swap the player's turn
    else:
        if session["turn"] == "X":
            session["turn"] = "O"
        elif session["turn"] == "O":
            session["turn"] = "X"
    
    return redirect(url_for("index"))
    

@app.route("/reset")
def reset():
    del session["board"]
    return redirect(url_for("index"))

