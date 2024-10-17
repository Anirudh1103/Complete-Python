import datetime as dt
def greet(name="Sir"):
    print(f"Hello {name}, \nHave a great day")


#The above function will take sir as value when no parameters is passed 
#It is demonstrated below.
print("Greet function is being called with parameter.\n")
greet(input("Enter your name: "))
print("\nNow Greet function is called with no parameters passed to it.\n")
greet()