def knapSack(W, wt, val, n):
    if W == 0 or n == 0:
        return 0
    if (W < wt[n-1]):
        return knapSack(W, wt, val, n-1)
    else:
        return  max(knapSack(W, wt, val, n-1), val[n-1] + knapSack(W - wt[n-1], wt, val, n-1))


def KnapSack(W, wt, val, n):
    dp = [[0 for i in range(W+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1,W+1):
            if W < wt[n-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i - W[i-1]][j-1]+ val[i-1], dp[i][j-1])

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))