# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?
class demo:
    a = 1
    
obj = demo()
obj.a = 2
print(demo.a)  # Output: 1
# The class attribute 'a' remains unchanged. The instance attribute 'a' is created
# for the object 'obj' and is different from the class attribute 'a'.

print(obj.a)