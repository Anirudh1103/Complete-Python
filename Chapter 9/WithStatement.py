with open("demo.txt") as file:
    line = file.readline()
    while(line != ""):
        print(line)
        line = file.readline()
        
    