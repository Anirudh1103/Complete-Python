# Write a program to input eight numbers from the user and display all the unique
# numbers (once)

numbers = set()
for i in range(0,8):
    temp = int(input(f"Enter the {i+1} number you want to add: "))
    numbers.add(temp)
    
print("Elements you entered are: ", numbers)
print("Repeated elements will not be printed")
