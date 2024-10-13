# 10. Write a program to print multiplication table of n using for loops in reversed order.
num = int(input("Enter the number whose multiplication table you want to print: "))
for i in range(10,0,-1):
    print(f"{num} * {i} = {num*i}")