# 3. Attempt problem 1 using while loop.
num = int(input("Enter the number whose multiplication table you want to print: "))
i = 1

while (i<=10):
    print(f"{num} * {i} = {num*i}")
    i+=1
