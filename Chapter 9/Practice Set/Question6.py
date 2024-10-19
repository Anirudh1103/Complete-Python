# 6. Write a program to mine a log file and find out whether it contains ‘python’.
with open("log.txt") as f:
    data = f.read()
    if 'Python' in data or  'python' in data:
        print("The log file contains 'Python'")
    else:
        print("The log file does not contain 'Python'")