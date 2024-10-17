#2. Write a python program using function to convert Celsius to Fahrenheit.
def CtoF(degree):
    return (degree * (9/5) + 32)

print(CtoF(int(input("Enter the degree: "))))