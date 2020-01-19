''' The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. For example,
following is a solution for 4 Queen problem.'''
N = 6
col = [i for i in range(N)]
def is_safe(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            val1 = arr[i]+i
            val2 = arr[i]-i
            if j+arr[j] == val1 or arr[j]-j == val2:
                return False
    return True

def permute(col, l, r):
    if l == r and is_safe(col):
        print(col)
    for i in range(l,r+1):
        col[i], col[l] = col[l], col[i]
        permute(col, l+1, r)
        col[i], col[l] = col[l], col[i]

permute(col, 0, N-1)
