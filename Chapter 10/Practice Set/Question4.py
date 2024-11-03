# 4. Add a static method in problem 2, to greet the user with hello.
class calculator:
    
    @staticmethod
    def greet():
        print("Hello, welcome to calculator class")
    def square(self,num):
        return num ** 2
    def cube(self,num):
        return num ** 3
    def squareRoot(self,num):
        return num ** 0.5


calci = calculator()
calci.greet()
print(calci.square(5))  # Output: 25
print(calci.cube(5))    # Output: 125
print(calci.squareRoot(16)) # OP : 2