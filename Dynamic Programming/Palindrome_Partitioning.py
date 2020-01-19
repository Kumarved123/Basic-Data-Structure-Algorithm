def palindrome(string):
    n = len(string)
    dp = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for L in range(2,n+1):
        for i in range(n-L+1):
            j = i + L-1
            if L == 2 and string[i] == string[j]:
                dp[i][j] = 1
            elif string[i] == string[j]:
                dp[i][j] = dp[i+1][j-1]
    pal = [float('inf')]*n
    pal[0] = 0
    for i in range(n):
        if (dp[0][i] == 1):
            pal[i] = 0
        else:
            for j in range(0,i):
                if dp[j+1][i] == 1 and pal[i]> pal[j]+1:
                    pal[i] = pal[j]+1
    print(pal[-1])
palindrome('bananab')




