###
#-------------------------------------------------------------------------------
# application.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Dec 07, 2020
# Execution:    flask run
# Submit50:     submit50 cs50/problems/2020/x/tracks/web/finance
#
# This program implements a website via which users can buy and sell stocks.
#
##

import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime

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
    #return apology("TODO")

    # Retrieve the cash balance for the current user
    rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    balance = rows[0]["cash"]

    total = 0.0
    total += balance

    entries = db.execute("SELECT * FROM stocks WHERE user_id = :id", id=session["user_id"])

    result = []
    for content in entries:
        current = []
        current.append(content["symbol"])
        current.append(lookup(content["symbol"])["name"])
        current.append(content["shares"])
        current.append(usd(content["price"]))
        current.append(usd(content["shares"] * content["price"]))
        result.append(current)
        total += content["shares"] * content["price"]

    return render_template("index.html", cash=usd(balance), retrieval=result, networth=usd(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # return apology("TODO")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide stock symbol", 403)

        # Ensure shares were submitted
        elif not request.form.get("shares"):
            return apology("must provide quantity of shares", 403)

        # Ensure shares is an integer
        try:
            quantity = int(request.form.get("shares"))
        except ValueError:
            return apology("quantity of shares must be a numerical value", 403)

        # Ensure shares is a positive integer
        if int(request.form.get("shares")) <= 0:
            return apology("quantity of shares must be a positive integer", 403)

        stock = lookup(request.form.get("symbol"))

        # Reject any invalid symbols
        if stock == None:
            return apology("symbol does not exist")

        # Retrieve the cash balance for the current user
        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        balance = rows[0]["cash"]

        # Get the stock ticker symbol
        ticker = request.form.get("symbol")

        # Calculate the total amount of cash required for the stock purchase
        quantity = int(request.form.get("shares"))
        total = quantity * stock["price"]

        # Store the stock purchase in the database, and update the cash balance
        if balance >= total:
            result = balance - total
            db.execute("INSERT INTO stocks VALUES (?, ?, ?, ?, ?)",
                       session["user_id"], ticker, quantity, stock["price"], datetime.now().strftime('%s'))
            db.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?)",
                       session["user_id"], ticker, quantity, stock["price"], datetime.now().strftime('%s'))
            db.execute("UPDATE users SET cash = :current WHERE id = :id", current=result, id=session["user_id"])
        else:
            return apology("insufficient funds for stock purchase")

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    #return apology("TODO")

    entries = db.execute("SELECT * FROM transactions WHERE user_id = :id", id=session["user_id"])

    result = []
    for content in entries:
        current = []
        current.append(content["symbol"])
        current.append(lookup(content["symbol"])["name"])
        current.append(content["shares"])
        current.append(usd(content["price"]))
        current.append(datetime.fromtimestamp(content["transacted"]))
        result.append(current)

    return render_template("history.html", retrieval=result)


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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

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
    # return apology("TODO")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        stock = lookup(request.form.get("symbol"))

        # Reject any invalid symbols
        if stock == None:
            return apology("symbol does not exist")

        # Transfer user to the quoted page
        return render_template("quoted.html", name=stock["name"], price=usd(stock["price"]), symbol=stock["symbol"])

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # return apology("TODO")

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

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must retype password", 403)

        # Ensure that the password and confirmation match each other
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("original password and retyped password don't match", 403)

        # Ensure that the requested username is not already present in the database
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        if len(rows) == 1 and rows[0]["username"] == request.form.get("username"):
            return apology("requested username is already present in the database")

        # Insert the username and password into the database
        id_key = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                            request.form.get("username"), generate_password_hash(request.form.get("password")))

        # Ensure username and password were inserted successfully
        if id_key == None:
            return apology("unsuccessful insertion of username and password into database", 403)

        # Remember which user has logged in
        # session["user_id"] = rows[0]["id"]
        session["user_id"] = id_key

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    #return apology("TODO")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure that a stock symbol was selected
        if request.form.get("symbol") == "Symbol":
            return apology("must select a stock symbol", 403)

        # Ensure shares were submitted
        elif not request.form.get("shares"):
            return apology("must provide quantity of shares", 403)

        # Ensure shares is an integer
        try:
            quantity = int(request.form.get("shares"))
        except ValueError:
            return apology("quantity of shares must be a numerical value", 403)

        # Ensure shares is a positive integer
        if int(request.form.get("shares")) <= 0:
            return apology("quantity of shares must be a positive integer", 403)

        # Get the stock ticker symbol
        company = request.form.get("symbol")

        # Get the number of shares
        quantity = int(request.form.get("shares"))

        # Retrieve the number of shares for the current user
        rows = db.execute("SELECT shares FROM stocks WHERE user_id = :id AND symbol = :corp", id=session["user_id"], corp=company)
        holdings = rows[0]["shares"]

        # Ensure that the user has enough shares for the sale
        if holdings < quantity:
            return apology("insufficient number of shares in portfolio for sale of stock", 403)

        # Calculate the current market value of the stock holdings
        current_price = lookup(company)["price"]
        market_value = quantity * current_price

        # Subtract the number of shares from the user's portfolio
        db.execute("UPDATE stocks SET shares = :current WHERE user_id = :id AND symbol = :corp",
                    current=(holdings-quantity), id=session["user_id"], corp=company)

        # Get the user's current cash holdings
        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        balance = rows[0]["cash"]

        # Deposit the market value of the stock into the user's cash holdings
        db.execute("UPDATE users SET cash = :current WHERE id = :id", current=(balance+market_value), id=session["user_id"])

        # Record the sale of stock in the transactions table
        db.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?)",
                       session["user_id"], company, -1*quantity, current_price, datetime.now().strftime('%s'))

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        result = []
        entries = db.execute("SELECT symbol FROM stocks WHERE user_id = :id", id=session["user_id"])
        for item in entries:
            result.append(item["symbol"])

        return render_template("sell.html", retrieval=result)


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """Deposit cash"""
    #return apology("TODO")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure that a cash amount was selected
        if request.form.get("cash") == "Cash Quantity":
            return apology("must select an amount of cash to deposit", 403)

        # Get the user's current cash holdings
        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        balance = rows[0]["cash"]

        # Get the amount of cash to deposit
        funds = int(request.form.get("cash"))

        # Deposit the selected cash quantity into the user's cash holdings
        db.execute("UPDATE users SET cash = :current WHERE id = :id", current=(balance+funds), id=session["user_id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("deposit.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

