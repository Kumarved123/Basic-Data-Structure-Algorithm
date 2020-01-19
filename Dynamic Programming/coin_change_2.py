def coin_change(arr, N):
    n = len(arr)
    dp = [[float('inf') for i in range(N+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(N+1):
            if j == 0:
                dp[i][j] = 0
            if i == 0:
                dp[i][j] == float('inf')
            else:
                if j >= arr[i-1]:
                    dp[i][j] = min(dp[i][j-arr[i-1]]+1, dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
    print(dp)
coin_change([1,5,6,9],11)
# greedy Algorithm
def coin(arr, n, N, res):
    if N == 0:
        print(res)
    elif n < 0 or N < 0:
        print('Not possible', )
    elif arr[n-1] > N:
        n = n-1
        coin(arr, n, N, res)
    else:
        res.append(arr[n-1])
        coin(arr, n, N-arr[n-1], res)
arr = [9, 6, 5, 1]
arr.sort()
coin(arr, 4, 11, [])


