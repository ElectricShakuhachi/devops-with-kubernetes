from random import choice
from string import printable

random_string = ""
for i in range(choice(range(50))):
    random_string += choice(printable)

with open("files/string.txt", "w") as file:
    file.write(random_string)
