from flask import Flask, render_template
import os

app = Flask(__name__)

print("Server started in port " + os.environ["PORT"])
