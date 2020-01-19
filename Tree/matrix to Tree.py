class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findroot(matrix):
    n = len(matrix)
    zero = [0]*n
    for i in range(n):
        if matrix[i] == zero:
            return i
def Tree(matrix):
    n = len(matrix)
    root = findroot(matrix)

def dfsUtil(matrix, stack, n, root):
    if len(stack) == 0:
        return
    s = stack[-1]
    i = 0
    while i < n and matrix[s][i] !=1:
        i+=1
    if i < n:
        stack.append(i)
        matrix[s][i] = 0
        if not root.left:
            root.left = Node(i)
            dfsUtil(matrix, stack, n, root.left)
        elif not s.right:
            root.right = Node(i)
            dfsUtil(matrix, stack, n, root.right)
    else:
        dfsUtil(matrix, stack, n)

def DFS(matrix, s):
    stack = []
    root = Node(s)
    n = len(matrix)
    stack.append(s)
    dfsUtil(matrix, stack, n, root)
