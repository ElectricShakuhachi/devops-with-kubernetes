from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    with open("output.log", "r") as f:
        file_contents = f.readlines()
    return file_contents[-1]
