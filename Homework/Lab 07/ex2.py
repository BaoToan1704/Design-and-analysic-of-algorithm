import time
import pylab
import random
def CoinRow(coins):
    n = len(coins)
    if n == 0:
        return 0
    elif n == 1:
        return coins[0]
    elif n == 2:
        return max(coins[0], coins[1])
    else:
        A = [0] * n
        A[0] = coins[0]
        A[1] = max(coins[0], coins[1])
        for i in range(2, n):
            A[i] = max(A[i-1], A[i-2] + coins[i])
        return A[n-1]


if __name__ == "__main__":
    coins = [5, 22, 26, 10, 4, 8]
    print(CoinRow(coins))
    
# Basic OP: addition in line 14
# Worst case: O(n)
# T(n)  = T(n-1) + T(n-2) = O(n)
# Time complexity: O(n)

def measure_time(func, N):
    runtime = []
    for n in N:
        start = time.time()
        f = func(n)
        stop = time.time()
        runtime.append(stop-start)
    return runtime

if __name__ == "__main__":
    N = list(range(1, 100))
    rtime1 = measure_time
    rtime2 = [1.5*t for t in N]
    pylab.plot(N, rtime1, label="1")
    pylab.plot(N, rtime2, label="2")
    pylab.legend()
    pylab.show()







