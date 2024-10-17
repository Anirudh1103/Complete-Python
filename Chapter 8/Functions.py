#Write a program to define a function which will greet the user

#Function Defination
def greet(name):
    print(f" Hello, {name}\n Have a great day!!")
    
name = input("Enter your name: ")
greet(name) #Function call

#The above code can be further shortened using below logic

greet(input("Enter your name: ")) #Function call