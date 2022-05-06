###
#-------------------------------------------------------------------------------
# application.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 24, 2021
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
# Video Demo:   https://www.youtube.com/watch?v=Yaxqnq3_OKg
# Heroku URL:   https://lesson-registration.herokuapp.com
#
# This program implements a course registration system for a school.
#
##

import os

#from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#from tempfile import mkdtemp
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
#app.config["SESSION_FILE_DIR"] = mkdtemp() # Note: This line must be removed in order for the app to function properly on Heroku
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Make sure the DATABASE_URL environment variable is set
if not os.environ.get("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL not set")

# Configure CS50 Library to use PostgreSQL database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# Configure CS50 Library to use SQLite database
#db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show the student's schedule and course listings"""
    
    # Retrieve the student's personal information
    rows = db.execute("SELECT first_name, last_name, grade_level FROM students WHERE id = :id", {"id": session["user_id"]}).fetchone()

    # Retrieve the student's course registrations
    registrations = dict()
    registrations["one"] = db.execute("SELECT courses.title FROM students_courses JOIN students ON students_courses.student_id = students.id JOIN courses ON students_courses.course_id = courses.id WHERE students.id = :id AND courses.section = :csection", {"id": session["user_id"], "csection": 1}).fetchone()

    registrations["two"] = db.execute("SELECT courses.title FROM students_courses JOIN students ON students_courses.student_id = students.id JOIN courses ON students_courses.course_id = courses.id WHERE students.id = :id AND courses.section = :csection", {"id": session["user_id"], "csection": 2}).fetchone()

    registrations["three"] = db.execute("SELECT courses.title FROM students_courses JOIN students ON students_courses.student_id = students.id JOIN courses ON students_courses.course_id = courses.id WHERE students.id = :id AND courses.section = :csection", {"id": session["user_id"], "csection": 3}).fetchone()

    registrations["four"] = db.execute("SELECT courses.title FROM students_courses JOIN students ON students_courses.student_id = students.id JOIN courses ON students_courses.course_id = courses.id WHERE students.id = :id AND courses.section = :csection", {"id": session["user_id"], "csection": 4}).fetchone()

    registrations["five"] = db.execute("SELECT courses.title FROM students_courses JOIN students ON students_courses.student_id = students.id JOIN courses ON students_courses.course_id = courses.id WHERE students.id = :id AND courses.section = :csection", {"id": session["user_id"], "csection": 5}).fetchone()

    registrations["six"] = db.execute("SELECT courses.title FROM students_courses JOIN students ON students_courses.student_id = students.id JOIN courses ON students_courses.course_id = courses.id WHERE students.id = :id AND courses.section = :csection", {"id": session["user_id"], "csection": 6}).fetchone()
    
    # Remove the enclosing single tuples from the registrations dictionary
    for key, value in registrations.items():
        if value != None:
            registrations[key] = value[0]
    
    # Retrieve the course information
    mathematics = db.execute("SELECT title, instructors.first_name, instructors.last_name, enrollment, capacity, section, departments.department FROM courses JOIN instructors ON courses.instructor_id = instructors.id JOIN departments ON courses.department_id = departments.id WHERE departments.department = :department", {"department": "Mathematics"}).fetchall()

    science = db.execute("SELECT title, instructors.first_name, instructors.last_name, enrollment, capacity, section, departments.department FROM courses JOIN instructors ON courses.instructor_id = instructors.id JOIN departments ON courses.department_id = departments.id WHERE departments.department = :department", {"department": "Science"}).fetchall()
    
    humanities = db.execute("SELECT title, instructors.first_name, instructors.last_name, enrollment, capacity, section, departments.department FROM courses JOIN instructors ON courses.instructor_id = instructors.id JOIN departments ON courses.department_id = departments.id WHERE departments.department = :department", {"department": "Humanities"}).fetchall()
    
    languages = db.execute("SELECT title, instructors.first_name, instructors.last_name, enrollment, capacity, section, departments.department FROM courses JOIN instructors ON courses.instructor_id = instructors.id JOIN departments ON courses.department_id = departments.id WHERE departments.department = :department", {"department": "Languages"}).fetchall()
    
    english = db.execute("SELECT title, instructors.first_name, instructors.last_name, enrollment, capacity, section, departments.department FROM courses JOIN instructors ON courses.instructor_id = instructors.id JOIN departments ON courses.department_id = departments.id WHERE departments.department = :department", {"department": "English"}).fetchall()
    
    art = db.execute("SELECT title, instructors.first_name, instructors.last_name, enrollment, capacity, section, departments.department FROM courses JOIN instructors ON courses.instructor_id = instructors.id JOIN departments ON courses.department_id = departments.id WHERE departments.department = :department", {"department": "Art"}).fetchall()
    
    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("index.html", rows=rows, registrations=registrations, mathematics=mathematics, science=science, humanities=humanities, languages=languages, english=english, art=art)


@app.route("/choose")
@login_required
def choose():
    """Drop a course"""
    
    # Retrieve the student's course registrations from the table students_courses
    rows = db.execute("SELECT courses.id, courses.title, courses.section FROM students_courses JOIN students ON students_courses.student_id = students.id JOIN courses ON students_courses.course_id = courses.id WHERE students.id = :id", {"id": session["user_id"]}).fetchall()

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template('choose.html', rows=rows)


@app.route("/confirm", methods=["GET", "POST"])
@login_required
def confirm():
    """Select a course to drop"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get form information
        course_id = request.form.get('course_id')
        if course_id == None:
            return redirect("/choose")

        # Get student's name, the course's section number and the course's title
        rows = db.execute("SELECT students.first_name, students.last_name, courses.id, courses.section, courses.title FROM students_courses JOIN students ON students_courses.student_id = students.id JOIN courses ON students_courses.course_id = courses.id WHERE students.id = :sid AND courses.id = :cid", {"sid": session["user_id"], "cid": course_id}).fetchone()

        return render_template('confirm.html', rows=rows)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return redirect("/")


@app.route("/dropped", methods=["GET", "POST"])
@login_required
def dropped():
    """Confirm course drop"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get form information
        course_id = int(request.form.get('course_id'))

        # decrement the course's enrollment and delete it from the table students_courses
        enrollment = db.execute('SELECT enrollment FROM courses WHERE id = :id', {'id': course_id}).fetchone()[0]
        enrollment -= 1
        db.execute('UPDATE courses SET enrollment = :num WHERE id = :id', {'num': enrollment, 'id': course_id})
        db.execute("DELETE FROM students_courses WHERE student_id = :sid AND course_id = :cid", {"sid": session["user_id"], "cid": course_id})
    
        # Commit to the database
        db.commit()

        return redirect("/result")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return redirect("/")


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
        rows = db.execute("SELECT * FROM students WHERE username = :username", {"username": request.form.get("username")}).fetchall()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0].hash, request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0].id

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


@app.route("/register", methods=["GET", "POST"])
@login_required
def register():
    """Register a course"""
    
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
    
        # Get form information
        course_id = int(request.form.get('course_id'))

        # Retrieve that course's section number
        section_num = db.execute('SELECT section FROM courses WHERE id = :id', {'id': course_id}).fetchone()[0]

        # Check to see if there is another course that the student has already registered for, in the same section
        rows = db.execute("SELECT courses.id FROM students_courses JOIN students ON students_courses.student_id = students.id JOIN courses ON students_courses.course_id = courses.id WHERE students.id = :id AND courses.section = :csection", {"id": session["user_id"], "csection": section_num}).fetchall()

        # If there is another course in the same section that the student has already registered for
        # decrement its enrollment and delete it from the table students_courses
        if len(rows) > 0:
            enrollment = db.execute('SELECT enrollment FROM courses WHERE id = :id', {'id': rows[0].id}).fetchone()[0]
            enrollment -= 1
            db.execute('UPDATE courses SET enrollment = :num WHERE id = :id', {'num': enrollment, 'id': rows[0].id})
            db.execute("DELETE FROM students_courses WHERE student_id = :sid AND course_id = :cid", {"sid": session["user_id"], "cid": rows[0].id})

        # Increment the newly registered course's enrollment
        enrollment = db.execute('SELECT enrollment FROM courses WHERE id = :id', {'id': course_id}).fetchone()[0]
        enrollment += 1
        db.execute('UPDATE courses SET enrollment = :num WHERE id = :course_id', {'num': enrollment, 'course_id': course_id})

        # Place the newly registered course in the table students_courses
        db.execute("INSERT INTO students_courses (student_id, course_id) VALUES (:sid, :cid)", {"sid": session["user_id"], "cid": course_id})

        # Commit the changes to the database
        db.commit()

        return redirect("/success")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return redirect("/")


@app.route("/result")
@login_required
def result():
    """Display course drop confirmation"""

    # Get student's name
    rows = db.execute('SELECT first_name, last_name FROM students WHERE id = :id', {'id': session["user_id"]}).fetchone()

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template('result.html', rows=rows)


@app.route("/section", methods=["GET", "POST"])
@login_required
def section():
    """Register courses"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
    
        # Get section number from the form
        try:
            section_num = int(request.form.get('section_num'))
        except TypeError:
            return render_template("section.html")

        # Retrieve all courses that correspond to that section number
        courses = db.execute('SELECT courses.id, section, title, instructors.first_name, instructors.last_name FROM courses JOIN instructors ON courses.instructor_id = instructors.id WHERE courses.section = :num', {'num': section_num}).fetchall()

        return render_template('selection.html', courses=courses, sec_num=section_num)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("section.html")


@app.route("/selection", methods=["GET", "POST"])
@login_required
def selection():
    """Select a course"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
    
        # Get form information
        try:
            course_id = int(request.form.get('course_id'))
        except TypeError:
            section_num = int(request.form.get('section_num'))
            courses = db.execute('SELECT * FROM courses JOIN instructors ON courses.instructor_id = instructors.id WHERE courses.section = :num', {'num': section_num}).fetchall()
            return render_template("selection.html", courses=courses)

        courses = db.execute('SELECT c.id, title, first_name, last_name, enrollment, capacity, section, d.department, description FROM courses c JOIN instructors i ON c.instructor_id = i.id JOIN departments d ON c.department_id = d.id WHERE c.id = :id', {'id': course_id}).fetchone()

        return render_template('description.html', courses=courses)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return redirect("/")


@app.route("/success")
@login_required
def success():
    """Display course register confirmation"""

    # Get student's name
    name = db.execute('SELECT first_name, last_name FROM students WHERE id = :id', {'id': session["user_id"]}).fetchone()

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template('success.html', name=name)


#--------------------------------------
# Code snippets from CS50 Finance
#--------------------------------------


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
