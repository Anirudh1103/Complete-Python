# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

empty_dict = {}

for i in range(0,4):
    name = input(f"{i+1}) Enter your name: ")
    language = input("Enter your favorite language: ")
    empty_dict[name] = language

print(empty_dict)