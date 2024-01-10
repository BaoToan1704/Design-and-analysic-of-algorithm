# Write a non-recursive program computing Fibonacci numbers

def fibonacci( n ):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = 0
        fib1 = 1
        fib2 = 0
        for i in range(2, n+1):
            fib = fib1 + fib2
            fib2 = fib1
            fib1 = fib
        return fib
    
if __name__ == '__main__':
    print(fibonacci(10))