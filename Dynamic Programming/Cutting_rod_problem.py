def Print(A):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            print(A[i][j], end = ' ')
        print()
def rodCut(P, C , N):
    l = len(P)
    dp = [[0 for i in range(N+1)] for j in range(l+1)]
    for i in range(1,l+1):
        for j in range(1,N+1):
            if j < C[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i][j-C[i-1]]+P[i-1], dp[i-1][j])
    Print(dp)
N = 5
C = [1,2,3,4]
P = [2,5,9,12]
rodCut(P, C , N)

