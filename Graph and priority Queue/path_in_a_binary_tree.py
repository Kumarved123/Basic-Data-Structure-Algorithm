class getNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

root = getNode(1)
root.left = getNode(2)
root.right = getNode(3)
root.left.left = getNode(4)
root.left.right = getNode(5)
root.right.left = getNode(6)
root.right.right = getNode(7)
def Print(root):
    if root:
        print(root.data, end = ' ')
        Print(root.left)
        Print(root.right)
Print(root)

def path_search(root, target, stack):
    if not root:
        return False
    stack.append(root.data)
    if root.data == target:
        return True
    if path_search(root.left, target, stack) or path_search(root.right, target, stack):
        return True
    stack.pop()
    return False

def path(root, target):
    stack = [ ]
    path_search(root, target, stack)
    return stack
print(path(root, 7))
