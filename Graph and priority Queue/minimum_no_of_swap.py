def minSwaps(arr):
    n = len(arr)
    pos = list(enumerate(arr))
    pos = sorted(pos, key = lambda x : x[1])
    visited = [False]*n
    ans = 0
    for i in range(n):
        cycle = 0
        if visited[i] == True or pos[i][0] == i:
            continue
        j = i
        while not visited[j]:
            visited[j] = True
            j = pos[i][0]
            cycle +=1
        if cycle > 1:
            ans += cycle-1
    return ans

arr = [1, 5, 4, 3, 2]
print(minSwaps(arr))

