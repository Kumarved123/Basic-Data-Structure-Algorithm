def permutations(arr, l, s):
    if s == l:
        print(''.join(arr))
    for i in range(s, l):
        arr[i], arr[s] = arr[s], arr[i]
        permutations(arr, l, s+1)
        arr[i], arr[s] = arr[s], arr[i]
a =['A', 'B', 'C']
permutations(a, len(a), 0)





