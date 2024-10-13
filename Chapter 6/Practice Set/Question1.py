#1. Write a program to find the greatest of four numbers entered by the user.
max = 0
for i in range(0,4):
    num = int(input(f"{i+1}) Enter the number: "))
    if(num>max):
        max = num

print(max)
