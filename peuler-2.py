"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def p2():
    fib = [1]
    fib2 =[]
    start = 0
    sum = 0
    # get the fibonacci < 4000000 first
    while fib[-1] <= 4000000:
        fib.append(fib[start] + fib[start-1])
        start+=1
    # get even fibonaccis < 4000000
    for num in fib:
        fib2 = [num for num in fib if num %2 ==0 and num <= 4000000]
    # sum even fibonaccis < 4000000
    for num2 in fib2: 
        sum += num2
    return sum


p2()