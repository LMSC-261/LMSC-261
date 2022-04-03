from flask import Flask, render_template, request, json, g
import sqlite3

DATABASE = "data/ThisGo.db"

app = Flask(__name__)

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DATABASE)
  db.row_factory = sqlite3.Row
  return db

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()

@app.route("/")
def index():
    cursor = get_db().cursor()
    release = cursor.execute(f"SELECT * FROM release")
    return render_template("index.html", release=release)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/demo", methods=["POST"])    
def demo():
    name = request.form.get("name")
    email = request.form.get("email")
    text = request.form.get("text")
    db = get_db()
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO contact (name, email, text) VALUES('{name}', '{email}', '{text}')")
    db.commit()
    return render_template("success.html")

@app.route("/demo_list")    
def demo_list():
    cursor = get_db().cursor()
    demos = cursor.execute(f"SELECT * FROM contact")
    return render_template("demo.html", demos=demos)

@app.route("/artists")
def artists():
    cursor = get_db().cursor()
    cursor.execute(f"SELECT * FROM artists")
    rows = cursor.fetchall()
    artists = []
    for row in rows:
        artists.append(row['name'])
    return render_template("artists.html", artists=json.dumps(artists))