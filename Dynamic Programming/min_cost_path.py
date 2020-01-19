def min_path(matrix, m, n):
    if m < 0 or n < 0:
        return float('inf')
    elif m == 0 and n == 0:
        return matrix[m][n]
    else:
        return matrix[m][n] + min(min_path(matrix, m-1, n),
                                  min_path(matrix, m, n-1),
                                  min_path(matrix, m-1, n-1))
cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
print(min_path(cost, 2, 2))
def Print(A):
    l = len(A)
    m = len(A[0])
    for i in range(l):
        for j in range(m):
            print(A[i][j], end = ' ')
        print()

def minCost(matrix, m, n):
    C = len(matrix)
    R = len(matrix[0])
    dp = [[0 for i in range(R)] for i in range(C)]
    dp[0][0] = cost[0][0]
    print(dp)
    for i in range(1,C):
        dp[0][i] = cost[0][i]+dp[0][i-1]
        dp[i][0] = cost[i][0]+dp[i-1][0]
    Print(dp)
    for i in range(1, C):
        for j in range(1, R):
            dp[i][j] =cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    Print(dp)

minCost(cost, 0, 0)

