def path(A):
    m = len(A)
    n = len(A[0])
    dp = [[1 for i in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if j+1 < n:
                if A[i][j+1] == A[i][j]+1 or A[i][j+1] == A[i][j]-1:
                    dp[i][j+1] = max(dp[i][j+1] +1, dp[i][j] +1)
            if i+1 < m:
                if A[i+1][j] == A[i][j]+1 or A[i+1][j] == A[i][j]-1:
                    dp[i+1][j] = max(dp[i+1][j] +1, dp[i][j] +1)
    for i in range(m):
        for j in range(n):
            print(dp[i][j], end = ' ')
        print()

A = [[1,2,9],
     [5,3,8],
     [4,6,7]]
path(A)