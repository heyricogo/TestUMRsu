import re
from flask import Flask, abort, redirect, render_template, request
from html import escape
from werkzeug.exceptions import default_exceptions, HTTPException
import sqlite3

app = Flask(__name__)

"""db.execute(CREATE TABLE users (userId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, email TEXT NOT NULL, formDate Date NOT NULL))"""

@app.route("/")
def index():
    """Handle requests for / via GET (and POST)"""
    """if MyDataBase.Users == NULL:
        CreateTable()"""
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    # User reached route via POST (as by submitting a form via POST)
    db = sqlite3.connect("MyDataBase.db")
    QueryCurs = db.cursor()
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            abort(403, "must provide username")
        # Ensure email was submitted
        elif not request.form.get("email"):
            abort(403, "must provide email")

        # Ensure formDate was submitted
        elif not request.form.get("formDate"):
            abort(403, "must provide date")

        # Ensure username is not already taken
        """username = request.form["username"]
        email = request.form["email"]
        formDate = request.form["formDate"]
"""
        """rows = QueryCurs.execute("SELECT username FROM users WHERE username = :name", (request.form.get("username"),))
        if rows == True:
            abort(403, "username already taken, please choose another")"""
        """return render_template(index.html)"""
        QueryCurs.execute("INSERT INTO Users (username, email, formDate) VALUES (:username,:email,:formDate)", (request.form.get("username"), request.form.get("email"), request.form.get("formDate")))
        db.commit()
        rows = QueryCurs.execute("SELECT * FROM users")
        for row in rows:
            print(row) 

        db.close()
        return render_template("submit.html")
"""
@app.route("/seeDB", methods=["POST"])
def seeDB():
    db = sqlite3.connect("MyDataBase.db")
    QueryCurs = db
    rows = QueryCurs.execute("SELECT * FROM users")
    db.commit()
    for row in rows:
        print(row["username"], row["email"], row["formDate"], sep=' | ') 
    db.close()
    return render_template("seeDB.html")"""

"""@app.errorhandler(HTTPException)
def errorhandler(error):"""
"""Handle errors"""
"""    return render_template("error.html", error=error), error.code


# https://github.com/pallets/flask/pull/2314
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
"""    

@app.errorhandler(HTTPException)
def errorhandler(error):
    """Handle errors"""
    return render_template("error.html", error=error)

# https://github.com/pallets/flask/pull/2314
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)