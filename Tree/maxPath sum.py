class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);
print ("Max path sum is " ,findMaxSum(root));