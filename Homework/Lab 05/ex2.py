# Recursive Exponentiation by squaring

def exp(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp(x, n // 2) ** 2
    else:
        return x * exp(x, n // 2) ** 2
    
print(exp(2, 10))

# Basic OP: multiplication in line 10
# Worst case: O(n)
# T(n) = T(n/2) + 1
# Time complexity: O(n)