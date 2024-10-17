def Factorial(n):
    if (n==1 or n==0):
        return 1
    return n * Factorial(n-1)

print(Factorial(int(input("Enter the number: "))))