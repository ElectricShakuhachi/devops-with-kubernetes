from time import sleep, ctime

with open("files/string.txt", "r") as file:
    random_string = file.read()

while True:
    with open("files/output.log", "w") as f:
        new_line = ctime() + ": " + random_string
        f.write(new_line)
        print(new_line)
    sleep(5)
