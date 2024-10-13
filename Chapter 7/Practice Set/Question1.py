#1. Write a program to print multiplication table of a given number using for loop.
num = int(input("Enter the number whose multiplication table you want to print: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
