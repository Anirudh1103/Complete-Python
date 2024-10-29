class Employee:
    salary = 100000
    PLanguage = "py"
    
Anirudh = Employee() #object 1
Amith = Employee() #object 2

Anirudh.name = "Anirudh"
Anirudh.id = 1
Amith.name = "Amith"
Amith.id = 2

print(Anirudh.id, Anirudh.name, Anirudh.salary)
print(Amith.id, Amith.name, Amith.salary)
