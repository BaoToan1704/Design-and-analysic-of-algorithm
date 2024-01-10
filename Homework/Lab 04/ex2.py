def HoarePartition(A, l, r):
    x = A[l]
    i = l - 1
    j = r + 1
    while True:
        while True:
            j = j - 1
            if A[j] <= x:
                break
        while True:
            i = i + 1
            if A[i] >= x:
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

def quicksort(A, l, r):
    if l < r:
        s = HoarePartition(A, l, r)
        quicksort(A, l, s)
        quicksort(A, s + 1, r)

if __name__ == '__main__':
    A = [3,6,5,2,7,1,9,8,4]
    quicksort(A, 0, len(A) - 1)
    print(A)
    
# Basic OP: commparision in line 21
# Worst case: O(n^2)
# T(n) = T(n/2) + n
# Time complexity: O(n^2)
    