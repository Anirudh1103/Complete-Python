#4. Write a recursive function to calculate the sum of first n natural numbers.
def SumOfNaturalNumbers(n):
    if(n==0):
        return n
    return n + SumOfNaturalNumbers(n-1)

print(SumOfNaturalNumbers(int(input("Enter the number: "))))