from time import sleep, ctime

with open("string.txt", "r") as file:
    random_string = file.read()

while True:
    print(ctime() + ": " + random_string)
    sleep(5)
