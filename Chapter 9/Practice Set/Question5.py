# 5. Repeat program 4 for a list of such words to be censored.
with open("donkey.txt") as file:
    censor_words = ["donkey","monkey","zeebra"]
    lst = (file.read()).split()
    for word in lst:
        if word in censor_words:
            index =int(lst.index("donkey"))
            lst.pop(index)
            lst.insert(index,"#####")
    print(lst)

    with open("doneky.txt","w") as wrFile:
        for word in lst:
            wrFile.write(word + " ")