def bfs(matrix, count,i, j):
    count[i][j] = 0
    x = [1, 1, 1, 0, 0, -1, -1, -1]
    y = [1, -1, 0, -1, 1, 1, -1, 0]
    for k in range(8):
        if matrix[i+x[k]][j+y[k]] == 1:
            count[i+x[k]][j+y[k]] = min(count[i+x[k]][j+y[k]], count[i][j])

def min_time(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = [[float('inf') for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                bfs(matrix, count, i , j)