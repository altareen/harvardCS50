###
#-------------------------------------------------------------------------------
# application.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 18, 2021
# Execution:    flask run
# Check50:      check50 cs50/problems/2021/x/finance
# Submit50:     submit50 cs50/problems/2021/x/finance
#
# This program implements a website via which users can buy and sell stocks.
#
##

import os, datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

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


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    tally = 0

    # Retrieve the user's stock holdings from their portfolio
    rows = db.execute("SELECT symbol, quantity FROM portfolio WHERE user_id = ?", session["user_id"])

    # Construct a dictionary to contain the table information
    for item in rows:
        item["name"] = lookup(item["symbol"])["name"]
        item["price"] = lookup(item["symbol"])["price"]
        item["total"] = usd(item["price"] * item["quantity"])
        tally += item["price"] * item["quantity"]
        item["price"] = usd(item["price"])

    # Get the user's cash holdings and add it to the running tally
    funds = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = funds[0]["cash"]
    tally += cash

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("index.html", rows=rows, cash=usd(cash), tally=usd(tally))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Lookup the information corresponding to the stock symbol
        stock = lookup(request.form.get("symbol"))

        # Ensure that the stock symbol exists
        if stock == None:
            return apology("stock symbol does not exist", 400)

        # Ensure that the quantity of shares is not a fractional value
        try:
            result = int(request.form.get("shares"))
        except ValueError:
            return apology("quantity of shares cannot be fractional", 400)

        # Ensure that the quantity of shares is a positive integer
        if int(request.form.get("shares")) <= 0:
            return apology("quantity of shares must be a positive integer", 400)

        # Get the user's current cash balance
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        # Ensure that the user can afford to purchase the quantity of shares
        if rows[0]["cash"] < stock["price"] * int(request.form.get("shares")):
            return apology("you cannot afford to purchase the requested quantity of shares")

        # Update cash holdings
        result = rows[0]["cash"] - stock["price"] * int(request.form.get("shares"))
        db.execute("UPDATE users SET cash = ? WHERE id = ?", result, session["user_id"])

        # Retrieve stock symbol, quantity of shares and stock price
        stock_symbol = request.form.get("symbol").upper()
        stock_quantity = int(request.form.get("shares"))
        stock_price = stock['price']

        # Check to see if the stock symbol exists in the portfolio table. If so, top it up with the new stock purchase
        rows = db.execute("SELECT quantity FROM portfolio WHERE user_id = ? AND symbol = ?", session["user_id"], stock_symbol)
        if len(rows) > 0:
            result = rows[0]["quantity"] + stock_quantity
            db.execute("UPDATE portfolio SET quantity = ? WHERE user_id = ? AND symbol = ?", result, session["user_id"], stock_symbol)
        else:
            # Insert the new stock purchase information into the portfolio table
            db.execute("INSERT INTO portfolio (user_id, symbol, quantity) VALUES (?, ?, ?)", session["user_id"], stock_symbol, stock_quantity)

        # Insert the stock purchase information into the history table
        db.execute("INSERT INTO transactions (user_id, symbol, quantity, price, occurrence) VALUES (?, ?, ?, ?, ?)", session["user_id"], stock_symbol, stock_quantity, stock_price, datetime.datetime.now())

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """Deposit funds into cash holdings"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Retrieve the requested amount of cash
        quantity = int(request.form.get("quantity"))

        # Retrieve the user's current cash holdings from the users table
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        # Add the deposited cash to the user's current cash holdingd
        quantity += rows[0]["cash"]

        # Place the updated cash amount into the users table
        db.execute("UPDATE users SET cash = ? WHERE id = ?", quantity, session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("deposit.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Retrieve the user's stock transactions
    rows = db.execute("SELECT symbol, quantity, price, occurrence FROM transactions WHERE user_id = ?", session["user_id"])

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Lookup the information corresponding to the stock symbol
        stock = lookup(request.form.get("symbol"))

        # Ensure that the stock symbol exists
        if stock == None:
            return apology("stock symbol does not exist", 400)

        # Convert the stock price to usd format
        stock["price"] = usd(stock["price"])

        # Redirect user to the quoted.html page
        return render_template("quoted.html", stock=stock)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure retyped password was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide retyped password", 400)

        # Ensure password and retyped passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("original and retyped passwords must match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username is not already in the database
        if len(rows) > 0:
            return apology("the chosen username is not available", 400)

        # Place username and hashed password into the database
        hash_code = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), hash_code)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("symbol"):
            return apology("must select a stock symbol", 400)

        # Ensure shares was submitted
        elif not request.form.get("shares"):
            return apology("quantity of shares cannot be empty", 400)

        # Ensure that shares is a positive integer
        elif int(request.form.get("shares")) <= 0:
            return apology("quantity of shares must be a positive integer", 400)

        # Ensure that the user has a sufficient quantity of shares for the sale
        rows = db.execute("SELECT quantity FROM portfolio WHERE user_id = ? AND symbol = ?", session["user_id"], request.form.get("symbol"))
        if rows[0]["quantity"] < int(request.form.get("shares")):
            return apology("insufficient quantity of shares for requested sale transaction", 400)

        # Retrieve the stock symbol, quantity of shares and stock price
        stock_symbol = request.form.get("symbol")
        stock_quantity = int(request.form.get("shares"))
        stock_price = lookup(stock_symbol)['price']

        # Calculate the reduction in the quantity of shares, and update the portfolio table
        reduced = rows[0]["quantity"] - stock_quantity
        if reduced == 0:
            db.execute("DELETE FROM portfolio WHERE user_id = ? AND symbol = ?", session["user_id"], stock_symbol)
        else:
            db.execute("UPDATE portfolio SET quantity = ? WHERE user_id = ? AND symbol = ?", reduced, session["user_id"], stock_symbol)

        # Calculate the increase in cash holdings, and update the users table
        funds = stock_quantity * stock_price
        rows = db.execute("SELECT cash from users WHERE id = ?", session["user_id"])
        funds += rows[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", funds, session["user_id"])

        # Update the transactions table
        db.execute("INSERT INTO transactions (user_id, symbol, quantity, price, occurrence) VALUES (?, ?, ?, ?, ?)", session["user_id"], stock_symbol, -1*stock_quantity, stock_price, datetime.datetime.now())

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        rows = db.execute("SELECT symbol FROM portfolio WHERE user_id = ?", session["user_id"])
        return render_template("sell.html", rows=rows)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
