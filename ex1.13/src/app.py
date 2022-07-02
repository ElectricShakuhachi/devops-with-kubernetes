from flask import Flask, render_template
from requests import get
from os.path import exists
from random import choice
from string import ascii_lowercase

app = Flask(__name__)

@app.route("/")
def index():
    if exists("../files/seed.txt") and exists("../files/time.log"):
        with open("../files/time.log", "r") as f:
            file_contents = f.readlines()
            if len(file_contents) > 1:
                old_time = int(file_contents[0])
                new_time = int(file_contents[-1])
            else:
                new_time = old_time = 0
        if new_time - old_time >= 86400:
            with open("../files/time.log", "w") as f:
                f.write("0\n0")
            seed = ""
            for i in range(20):
                seed += choice(ascii_lowercase)
            with open("../files/seed.txt", "w") as f:
                f.write(seed)
            print("Generated new seed due to timeout")
            print(seed)
        else:
            with open("../files/seed.txt", "r") as f:
                contents = f.readlines()
                if len(contents) > 0:
                    seed = contents[0]
                else:
                    seed = ""
                    for i in range(20):
                        seed += choice(ascii_lowercase)
                    with open("../files/seed.txt", "w") as f:
                        f.write(seed)
                    print("Generating seed because one was not found in file")
                    print(seed)
    else:
        seed = ""
        for i in range(20):
            seed += choice(ascii_lowercase)
        with open("../files/seed.txt", "w") as f:
            f.write(seed)
        print("Generating first seed")
        print(seed)
    return render_template("index.html", seed=seed)
