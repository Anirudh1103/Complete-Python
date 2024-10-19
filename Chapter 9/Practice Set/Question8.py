# 8. Write a program to make a copy of a text file “pems.txt”
with open("poems.txt") as f:
    content = f.read()
with open("poems_copy.txt","w") as f:
    f.write(content)