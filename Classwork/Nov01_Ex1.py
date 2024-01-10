# Knapsack problem with W capacity and list of items, each with a weight(w) and a value(v). Choose items that not weight over capacity W, but also making the best value of all items pick.
# Input: W, n, w1, w2, ..., wn and v1, v2, ..., vn
# Output:  List of items that fit in the knapsack and value-wise picked

def knapsack(W, n, w, v):
    # Create a table to store results of subproblems
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                K[i][j] = 0
            elif w[i-1] <= j:
                K[i][j] = max(v[i-1] + K[i-1][j-w[i-1]],  K[i-1][j])
            else:
                K[i][j] = K[i-1][j]

    return K[n][W]

# Driver program to test above function
W = 50
n = 3
w = [10, 20, 30]
v = [60, 100, 120]
print (knapsack(W, n, w, v))


