def output_LCS(A, prev, i, j):
    if i == 0 or j == 0:
        return
    if prev[i][j] == 0:
        output_LCS(A, prev, i-1, j-1)
        print(A[i-1], end='')
    elif prev[i][j] == 1:
        output_LCS(A, prev, i-1, j)
    else:
        output_LCS(A, prev, i, j-1)
        
def LCS_length(A, B):
    n = len(A)
    m = len(B)
    c = [[0 for j in range(m+1)] for i in range(n+1)]
    prev = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                prev[i][j] = 0
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                prev[i][j] = 1
            else:
                c[i][j] = c[i][j-1]
                prev[i][j] = 2
    output_LCS(A, prev, n, m)
    print()
    return c[n][m]

if __name__ == '__main__':
    A = 'ABCBDAB'
    B = 'BDCABA'
    print(LCS_length(A, B))


