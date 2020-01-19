str1 = 'saturday'
str2 = 'sunday'
m = len(str1)
n = len(str2)
def edit(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m - 1] == str2[n - 1]:
        return edit(str1, str2, m - 1, n - 1)
    return 1 + min(edit(str1, str2, m, n - 1),  # Insert
                   edit(str1, str2, m - 1, n),  # Remove
                   edit(str1, str2, m - 1, n - 1)  # Replace
                   )
print(edit(str1, str2, m, n))

def editDistance(str1, str2, m, n):
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i ==0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[m][n]

print(editDistance(str1, str2, m, n))

