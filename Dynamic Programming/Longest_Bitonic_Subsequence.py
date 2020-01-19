#Longest Bitonic Subsequence
'''Given an array arr[0 … n-1] containing n positive integers, a subsequence of
arr[] is called Bitonic if it is first increasing, then decreasing. Write a
function that takes an array as argument and returns the length of the longest
bitonic subsequence. A sequence, sorted in increasing order is considered Bitonic
with the decreasing part as empty. Similarly, decreasing order sequence is
considered Bitonic with the increasing part as empty.'''
def bitonic(arr):
    n = len(arr)
    inc = [1]*n
    dec = [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]> arr[j] and inc[j] +1 > inc[i]:
                inc[i] = inc[j]+1
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i]> arr[j] and dec[i] +1 > dec[j]:
                dec[i] = dec[j]+1
    res = []
    for i in range(n):
        res.append(inc[i]+dec[i])
    print(max(res)-1)
bitonic([12, 11, 40, 5, 3, 1])



