from time import sleep, ctime

with open("string.txt", "r") as file:
    random_string = file.read()

for i in range(10):
    print(ctime() + ": " + random_string)
    sleep(5)
    
