def matrix(arr):
    n = len(arr)
    dp = [[0 for i in range(n)] for i in range(n)]
    for L in range(1,n):
        for i in range(n-L+1):
            j = i+L-1
            dp[i][j] = float('inf')
            for k in range(i,j):
                temp = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                if temp < dp[i][j]:
                    dp[i][j] = temp
    return dp[0][-1]