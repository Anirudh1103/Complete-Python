# 7. Write a program to find out the line number where python is present from ques 6.
count = 0
with open("log.txt") as f:
    data = f.readline()
    while data != "":
        if "python" in data:
            print("Python is present at line number: ", count + 1)
            break
        else:
            data = f.readline()
            count += 1