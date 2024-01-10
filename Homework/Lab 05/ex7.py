def LomutoPartition(A, l, r):
    p = A[l]
    s = l
    for i in range(l+1, r+1):
        if A[i] < p:
            s += 1
            A[i], A[s] = A[s], A[i]
    A[l], A[s] = A[s], A[l]
    return s

def quickselect(A, l, r, k):
    if l == r:
        return A[l]
    s = LomutoPartition(A, l, r)
    if k == s:
        return A[s]
    elif k < s:
        return quickselect(A, l, s-1, k)
    else:
        return quickselect(A, s+1, r, k)

# Driver code
A = [2, 8, 7, 1, 3, 5, 6, 4]
print(quickselect(A, 0, len(A)-1, 3))
print(quickselect(A, 0, len(A)-1, 5))
print(quickselect(A, 0, len(A)-1, 7))        

# Basic OP: addition in line 20
# Worst case: O(n^2)
# T(n) = T(n/2) + n
# Time complexity: O(n^2)