def multiply(A, B, n):
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(multiply(A, B, 3))
    
# Basic OP: addition on line 7
# Worst case: other cases
# Count: T(n) = n*k
# Time complexity: O(n*k)