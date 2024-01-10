def f(S):
    if len(S) == 0:
        return [set()] # return a list with an empty set
    else:
        x = S.pop() # remove an element from S  # O(1)
        subsets = f(S)  # compute all subsets of S  
        return subsets + [subset | {x} for subset in subsets] # return all subsets of S + all subsets of S with x added (| is union)    

print(f({1, 5, 7, 4, 3}))

# Basic OP: addition in line 7 
# Worst case: O(2^n)
# C(n) = 2C(n-1) + 1 = 2(2C(n-2) + 1) + 1 = 2(2(2C(n-3) + 1) + 1) + 1 = ... = 2^nC(0) + 2^n-1 + ... + 2 + 1 = 2^n - 1
# Time complexity: O(2^n)