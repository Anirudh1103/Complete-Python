#4. Write a program to find whether a given number is prime or not.

num = int(input("Enter the number: "))
for i in range(2,num):
    if num % i == 0:
        print(num,"is not a prime number")
        break
    else:
        print(num,"is a prime number")