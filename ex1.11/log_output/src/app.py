from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    with open("output.log", "r") as f:
        file_contents = f.readlines()
    try:
        with open("../logs/counter.log", "r") as f:
                counter = int(f.readlines()[-1])
    except:
        counter = 0
    return_string = "<p>" + file_contents[-1] + "</p><br><p>Ping / Pongs: " + str(counter) + "</p>"
    return return_string
