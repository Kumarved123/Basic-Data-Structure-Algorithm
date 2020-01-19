def longest(A):
    n = len(A)
    dp = [[1 for i in range(n)] for i in range(n)]
    for L in range(2, n):
        for i in range(n-L+1):
            j = i+L-1
            if L == 2:
                if A[i] == A[j]:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 1

            elif A[i] == A[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    return dp[0][-1]
