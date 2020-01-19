class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.ans = []

    def sub(self, A, arr, index, ans):
        ans.append(arr)
        for i in range(index, len(A)):
            arr.append(A[i])
            self.sub(A, arr, i + 1, ans)
            arr.pop()
        return


    def subsets(self, A):
        ans = []
        self.sub(A, [], 0, ans)
        return ans
c= Solution()
arr = [1,2,3]
print(c.subsets(arr))


'_____________________________________________________________________'


def subsetsUtil(A, subset, index, res):
    res.append(subset)
    for i in range(index, len(A)):
        # include the A[i] in subset.
        subset.append(A[i])

        # move onto the next element.
        subsetsUtil(A, subset, i + 1,res)

        # exclude the A[i] from subset and
        # triggers backtracking.
        subset.pop(-1)
    return


# below function returns the subsets of vector A.
def subsets(A):
    subset = []
    index = 0
    res = []
    subsetsUtil(A, subset, index, res)
    print(res)


# Driver Code

# find the subsets of below vector.
array = [1, 2, 3]

# res will store all subsets.
# O(2 ^ (number of elements inside array))
# because at every step we have two choices
# either include or ignore.
subsets(array)