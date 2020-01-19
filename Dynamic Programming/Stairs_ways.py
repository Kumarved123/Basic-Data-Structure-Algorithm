def countWays(s,m):
    dp = [0 for i in range(s+1)]
    dp[1] = 1
    dp[0] = 1
    for i in range(2, s):
        j = 1
        while j <= m and j <= i:
            dp[i] = dp[i] + dp[i - j]
            j = j + 1
    return dp[s - 1]



s,m = 4,2
print("Nmber of ways =",countWays(s,m))