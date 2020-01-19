class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def binarySearch(self, arr, l, r, x):
        while l <= r:
            mid = l + (r - l)//2;
            if arr[mid] == x:
                return( mid)
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return -1
    def search(self, A, B):
        n = len(A)
        m= min(A)
        i = A.index(m)
        l = i
        if l ==0:
            ans = self.binarySearch(A, 0, n-1, B)
            return ans
        else:
            A = A+A
            r = i+n-1
            ans = self.binarySearch(A, l, r, B)
            return ans

A = [ 1, 7, 67, 133, 178 ]
B =1
s = Solution()
print(s.search(A, B))

