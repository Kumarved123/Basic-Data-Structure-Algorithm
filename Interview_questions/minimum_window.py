def min_window(string):
    arr = [i for i in string]
    A= list(set(arr))
    dict = {}
    for i in A:
        dict[i] = 0
    l = len(A)
    i = 0
    count = 0
    min_len = float('inf')
    for j in range(len(arr)):
        dict[arr[j]] +=1
        if dict[arr[j]] == 1:
            count+=1
        if count == l:
            while dict[arr[i]]> 1:
                if dict[arr[i]] > 1:
                    dict[arr[i]] -=1
                i+=1
            window = j -i+1
            min_len = min(window, min_len)
    print(dict, min_len,)



string = 'aabcbcdbca'
min_window(string)