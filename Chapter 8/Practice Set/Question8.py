#8. Write a python function to print multiplication table of a given number.
def MultiplicationTable(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

n = int(input("Enter the number: "))
MultiplicationTable(n)