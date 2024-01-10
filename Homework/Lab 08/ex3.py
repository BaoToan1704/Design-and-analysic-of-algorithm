def printSolution(D):
    print("Following matrix is the shortest distances between every pair of vertices")
    for i in range(len(D)):
        for j in range(len(D)):
            print("%7d" % D[i][j], end=' ')
        print("")
    return

def Floyd(W):
    D = [[0 for i in range(len(W))] for j in range(len(W))]
    for i in range(len(W)):
        for j in range(len(W)):
            D[i][j] = W[i][j]
    for k in range(len(W)):
        for i in range(len(W)):
            for j in range(len(W)):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    printSolution(D)
    return

if __name__ == "__main__":
    W = [[0, 5, 999, 10],
         [999, 0, 3, 999],
         [999, 999, 0, 1],
         [999, 999, 999, 0]]
    Floyd(W)

