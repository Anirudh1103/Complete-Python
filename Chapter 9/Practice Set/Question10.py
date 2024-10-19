# 10. Write a program to wipe out the content of a file using python.
with open("hi-score.txt","w") as f:
    f.truncate()

#We can even use f.write("")