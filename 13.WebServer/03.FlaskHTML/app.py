from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

# See https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
# for the documentation on render_template object.