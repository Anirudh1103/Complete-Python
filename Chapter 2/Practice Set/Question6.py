#Write a python program to calculate the square and square root of a number entered by the user.
num = int(input("Enter the number: "))
square = num * num

square_root = num ** 0.5
# We can use math module 
import math
square_root = math.sqrt(num)
print("Square = ",square)
print("Sqrt = ",square_root)
