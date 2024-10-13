# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
comment = input("Enter the comment: ")
spam = ["Make a lot of money", "buy now", "subscribe this", "click this"]

if(comment in spam):
    print("Spam comment!!!")
else:
    print("Not a spam comment")