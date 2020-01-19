ans = []
def comb(arr, start, l, res, ans):
    print(res)
    for i in range(start,l):
        res.append(arr[i])
        comb(arr, i+1, l, res,ans)
        res.pop()
    return
comb([1,2,3], 0, 3, [], ans)
print(ans)


