from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    with open("../files/output.log", "r") as f:
        file_contents = f.readlines()[-1]
    return file_contents