from flask import Flask, render_template, request

app = Flask(__name__)

demos = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/demo", methods=["POST"])    
def demo():
    name = request.form.get("name")
    email = request.form.get("email")
    text = request.form.get("text")
    demos.append([name, email, text])
    return render_template("success.html")

@app.route("/demo_list")
def demo_list():
    return render_template("demo.html", demos=demos)