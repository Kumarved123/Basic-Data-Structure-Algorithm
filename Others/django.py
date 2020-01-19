def is_safe(a, visited, i, j):
    n =len(visited)
    m = len(visited[0])
    if i >= 0 and j > -1 and i < n and j < m and visited[i][j] == 0and a[i][j] == 1:
        return True
    else:
        return False


def bfs(a,visited, i, j):
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1];
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1];
    visited[i][j] = 1
    for k in range(8):
        if is_safe(a,visited, i + rowNbr[k], j + colNbr[k]):
            bfs(a,visited, i + rowNbr[k], j + colNbr[k])


def findIslands(a, n, m):
    visited = [[0 for i in range(m)] for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and a[i][j] == 1:
                bfs(a, visited, i, j)

                count += 1
    print(visited)
    return count


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

row = len(graph)
col = len(graph[0])

print(findIslands(graph, row, col))