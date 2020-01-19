#Count number of binary strings without consecutive 1’s
def count(N):
    dp = [0 for i in range(N)]
    dp[0] = 2
    dp[1] = 3
    for i in range(2,N):
        dp[i] = dp[i-1] + dp[i-2]
    print(2**N - dp[-1])
count(5)


