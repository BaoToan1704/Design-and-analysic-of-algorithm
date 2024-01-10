import time
import pylab

def binomial(n, k):
    C = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C[n][k]

if __name__ == "__main__":
    print(binomial(5, 2))
    
# Basic OP: addition in line 8
# Worst case: O(n^2)
# T(n)  = T(n-1) + O(n) = O(n^2)
# Time complexity: O(n^2)


def measure_time(func, N1, N2):
    runtime = []
    for n in range (len(N1)):
        start = time.time()
        f = func(N1[n], N2[n])
        stop = time.time()
        runtime.append(stop-start)
    return runtime

if __name__ == "__main__":
    N1 = list(range(100))
    N2 = list(range(100))
    rtime = measure_time(binomial, N1, N2)
    rtime2 = [t*1.5 for t in rtime]
    pylab.plot(N1, rtime, N2, rtime2)
    pylab.legend(['1', '2'])
    pylab.show()


