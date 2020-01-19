class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

def findPathutil(root, path, n):
    if not root:
        return False
    path.append(root.key)
    if root.key == n:
        return True
    if (root.left != None and findPathutil(root.left, path, n)) or (root.right!= None and findPathutil(root.right, path, n)):
        return True
    path.pop()
    return False


def findPath(root, n):
    path = []
    findPathutil(root,path, n)
    return path

def findLCA(root, n1, n2):
    path1= findPath(root, n1)
    path2= findPath(root, n2)
    i = 0
    lca = None
    while i< len(path1) and i<len(path2) and path1[i] == path2[i]:
        i+=1
    return (path1[i-1])





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(findPath(root, 7))

print("LCA(4, 5) = " , (findLCA(root, 4, 5, )))
print("LCA(4, 6) = ",(findLCA(root, 4, 6)))
print("LCA(3, 4) = ", (findLCA(root, 3, 4)))
print("LCA(2, 4) = " , (findLCA(root, 2, 4)))