def updateMatrix(mat):
    m,n = len(mat), len(mat[0])
    matOutput= [[]]
    def checkdistance(mat, i, j, dist=0):
        if (j+2<n and mat[i][j+1]== 0):
            return dist+1
        elif (i+2<m and mat[i+1][j]==0): 
            return dist+1
        elif j+2<n:
            return updateMatrix(mat, i, j+1, dist=dist+1)
        elif i+2<m:
            return updateMatrix(mat, i+1, j, dist=dist+1)

    for i in range(0,m-1):
        for j in range(0,n-1):
            matOutput[i][j] = checkdistance(mat, i, j, 0)
    return matOutput

mat = [[0,0,0],[0,1,0],[0,0,0]]
# print(len(mat))
print(updateMatrix(mat))