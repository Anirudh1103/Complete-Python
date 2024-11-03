# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        
p = Programmer("Anirudh",400000,123456)
print(f"{p.company} : {p.name} {p.salary} {p.pincode}")