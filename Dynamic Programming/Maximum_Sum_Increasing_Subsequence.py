'''Given an array of n positive integers. Write a program to find the sum of
maximum sum subsequence of the given array such that the integers in the
subsequence are sorted in increasing order. For example, if input is
{1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100),
if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10)
and if the input array is {10, 5, 4, 3}, then output should be 10'''
def max_sum(arr):
    n = len(arr)
    dp = [arr[0]]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[j] < arr[i] and dp[i] < dp[j]+arr[i]:
                dp[i] = dp[j]+arr[i]
    print(dp)
max_sum([1, 101, 2, 3, 100, 4, 5])
