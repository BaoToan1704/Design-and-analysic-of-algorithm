def knapsack(W, V, K):
    n = len(W)
    max_value = 0
    for i in range(2 ** n):
        weight = 0
        value = 0
        for j in range(n):
            if (i >> j) & 1:
                weight += W[j]
                value += V[j]
        if weight <= K:
            max_value = max(max_value, value)
    return max_value

if __name__ == "__main__":
    W = [10, 20, 30]
    V = [60, 100, 120]
    K = 50
    print(knapsack(W, V, K))
    

# Basic OP: addition on line 9
# Worst case: other cases
# T(n) = 2^n
# Time complexity: O(n^2)