from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/translate")
def translate():
    term = request.args.get("term")
    return render_template("translate.html", term=term)

@app.route("/guide")
def guide():
    return render_template("guide.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/initdb")
def initdb():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS terms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL UNIQUE,
            definition TEXT NOT NULL,
            language TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    return "Databse intialized good"

if __name__ == "__main__":
    app.run(debug=True)