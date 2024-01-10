import time
import pylab

def knapsack(W, w, v):
    F = [[0] * (W + 1) for _ in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, W + 1):
            if j - w[i - 1] >= 0:
                F[i][j] = max(F[i - 1][j], F[i - 1][j - w[i - 1]] + v[i - 1])
            else:
                F[i][j] = F[i - 1][j]
    return F[-1][-1]

if __name__ == "__main__":
    W = 10
    w = [2, 3, 4, 5]
    v = [3, 4, 5, 6]
    print(knapsack(W, w, v))

# Basic OP: comparision in line 6
# Worst case: O(nW)
# T(n)  = T(n-1) + O(W) = O(nW)
# Time complexity: O(nW)

def measure_time(func, N):
    runtime = []
    for n in N:
        start = time.time()
        f = func(n)
        stop = time.time()
        runtime.append(stop-start)
    return runtime

