import time
import pylab

def ChangeMaking(C, n):
    F = [0] * (n + 1)
    for i in range(1, n + 1):
        F[i] = min([F[i - c] for c in C if i - c >= 0]) + 1
    return F[n]

if __name__ == "__main__":
    C = [1, 3, 4]
    n = 6
    print(ChangeMaking(C, n))

# Basic OP: comparision in line 4
# Worst case: O(n^2)
# T(n)  = T(n-1) + O(n) = O(n^2)
# Time complexity: O(n^2)


