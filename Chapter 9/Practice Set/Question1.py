# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

with open("poems.txt") as poem:
    text = poem.read()
    for word in text.split():
        if word == "twinkle":
            print("The word 'twinkle' is found in the poem.")
            break
    else:
        print("The word 'twinkle' is not found in the poem.")