# design and analyze an algorithm to count the number of elements which are smaller than surrounding their neighbors.
def countSmallerThanNeighbors(mat):
    count = 0
    for i in range(1, len(mat)-1):
        for j in range(1, len(mat[i])-1):
            if mat[i][j] < mat[i-1][j] and mat[i][j] < mat[i+1][j] and mat[i][j] < mat[i][j-1] and mat[i][j] < mat[i][j+1]:
                count += 1
    return count


if __name__ == "__main__":
    mat = [[7,1,3,6,9,85,37,3],
        [64,17,45,37,5,83,25,3],
        [4,62,4,6,27,58,83,2],
        [5,6,6,42,46,83,1,31],
        [35,61,3,41,2,5,31,3]]
    print(countSmallerThanNeighbors(mat))    