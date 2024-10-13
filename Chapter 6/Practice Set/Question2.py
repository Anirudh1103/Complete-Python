# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
flag = True
marks = []
for i in range(3):
    marks.append(int(input(f"Enter the marks of Subject {i+1}: ")))
    
for i in marks:
    if i < 33:
        print("Failed")
        flag = False
avg = sum(marks)/3
while flag:
    if(avg >= 40):
        print("Passed")
    else:
        print("Failed")
    