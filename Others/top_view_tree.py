class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def levelorder(root):
    arr = []
    q = []
    q.append(root)
    level = 0
    while len(q)!= 0:
        n = len(q)
        while n > 0:
            temp = q.pop()
            arr.append([temp.data, level])
            if temp.left:
                q.insert(0, temp.left)
            if temp.right:
                q.insert(0, temp.right)
            n -=1
        level += 1
        print()
    return arr

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("Following are nodes in top view of Binary Tree")
print(levelorder(root))
