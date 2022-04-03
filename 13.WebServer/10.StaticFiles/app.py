from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    file = open("data/release.csv", "r")
    reader = csv.reader(file)    
    release = list(reader)
    file.close()
    return render_template("index.html", release=release)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/demo", methods=["POST"])    
def demo():
    name = request.form.get("name").replace(",", "%2C")
    email = request.form.get("email").replace(",", "%2C")
    text = request.form.get("text").replace(",", "%2C")
    file = open("data/contact.csv", "a")
    writer = csv.writer(file)
    writer.writerow([name, email, text])
    file.close()
    return render_template("success.html")

@app.route("/demo_list")
def demo_list():
    file = open("data/contact.csv", "r")
    reader = csv.reader(file)
    demos = list(reader)
    file.close()
    for demo in demos:
        for field in range(0, len(demo)):
            print(demo[field])
            demo[field] = demo[field].replace("%2C", ",")
    return render_template("demo.html", demos=demos)