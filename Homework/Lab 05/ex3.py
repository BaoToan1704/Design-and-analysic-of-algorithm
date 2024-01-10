# Recursive Euclid’s algorithm for greatest common divisor

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(24, 16))

# Basic OP: modulo in line 7
# Worst case: O(n)
# T(n) = T(n/2) + 1
# Time complexity: O(n)