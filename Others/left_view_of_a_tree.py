def leftViewUtil(root, level, max_level):
    if root is None:
        return
    if (max_level[0] < level):
        print("% d\t" % (root.data))
        max_level[0] = level
    leftViewUtil(root.left, level + 1, max_level)
    leftViewUtil(root.right, level + 1, max_level)
def leftView(root):
    max_level = [0]
    leftViewUtil(root, 1, max_level)