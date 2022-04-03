from flask import Flask, redirect, render_template, request, session
# Install flask_session using: pip3 install Flask_Session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Instrumencts for sale
ITEMS = ["piano", "guitar", "bass", "drum"]

# Serve the root page
@app.route("/")
def index():
    return render_template("index.html")

# Respond to the form from the browser
# Update our cart in session
@app.route("/update", methods=["POST"])
def update():
    for item in request.form:
        session[item] = int(request.form.get(item))
    return redirect("/cart")

# Show the cart
@app.route("/cart")
def cart():
    return render_template("cart.html", cart=session)
