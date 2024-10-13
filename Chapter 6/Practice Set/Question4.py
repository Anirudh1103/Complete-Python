# 4. Write a program to find whether a given username contains less than 10 characters or not.
usr_name = input("Enter the user name: ")
if(len(usr_name)<10):
    print("less than 10 characters")
else:
    print("10 or more characters")

#Shortened the above program
print(len(usr_name)>10)