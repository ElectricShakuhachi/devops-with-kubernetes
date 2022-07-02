import time

while True:
    try:
        with open("../files/time.log", "r") as f:
            file_contents = f.readlines()
            old_time = int(file_contents[0])
            new_time = int(file_contents[-1]) + 30
    except:
        old_time = 0
        new_time = 0
    with open("../files/time.log", "w") as f:
        f.write(str(old_time) + "\n" + str(new_time))
    time.sleep(30)
