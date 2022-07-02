from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/pingpong")
def index():
    try:
        with open("../logs/counter.log", "r") as f:
            counter = int(f.readlines()[-1])
    except:
        counter = 0
    with open("../logs/counter.log", "w") as f:
        f.write(str(counter + 1))
    return str(counter)