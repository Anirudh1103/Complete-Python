file = open("demo.txt")
line = file.readline()
while(line != ""):
    print(line)
    line = file.readline()