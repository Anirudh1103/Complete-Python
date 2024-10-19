f = open("example.txt","r")

#.readlines(): it will return the list of lines
lines = f.readlines()
print(lines,type(lines))

line1 = f.readline()
print(line1)
