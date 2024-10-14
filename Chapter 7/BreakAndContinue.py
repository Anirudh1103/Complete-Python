#Break
i = 0
while i<5:
    if(i == 3):
        break
    print(i)
    i+=1
#Printing only even numbers using continue:
for i in range(1,20):
    if(i%2==0):
        print(i)
    else:
        continue