# Combination 
def combination(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combination(n-1, k-1) + combination(n-1, k)
    
if __name__ == "__main__":
    print(combination(6, 2))
    
# Basic OP: multiplication on line 5
# Worst case: other cases
# Count: T(n) = n
# Time complexity: O(n)