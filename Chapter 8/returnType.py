def generateFibonacci(n) -> list:
    series = [0,1]
    for i in range(2,n):
        series.append(series[i-1] + series[i-2])
    return series

fibonacciSeries = generateFibonacci(10)
print(fibonacciSeries)

#In python you dont have to specify the return type in the function
#But its a good practice to mention it as it improves the readability of the code