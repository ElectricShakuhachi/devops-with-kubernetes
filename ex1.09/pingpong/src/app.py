from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/pingpong")
def index():
    with open("counter.log", "r") as f:
        counter = int(f.readlines()[-1])
    with open("counter.log", "w") as f:
        f.write(str(counter + 1))
    return str(counter)