# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.
class calculator:
    def __init__(self):
        print("Welcome to calculator class")
    
    def square(self,num):
        return num ** 2
    def cube(self,num):
        return num ** 3
    def squareRoot(self,num):
        return num ** 0.5


calci = calculator()
print(calci.square(5))  # Output: 25
print(calci.cube(5))    # Output: 125
print(calci.squareRoot(16)) # OP : 2