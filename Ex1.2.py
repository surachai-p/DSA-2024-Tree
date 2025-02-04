class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    
    def count_leaf_nodes(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)

bt = BinaryTree()
bt.root = Node(10)
bt.root.left = Node(5)
bt.root.right = Node(15)
bt.root.left.left = Node(3)
bt.root.left.right = Node(7)
bt.root.right.left = Node(12)
bt.root.right.right = Node(18)


print("Total number of leaf nodes:", bt.count_leaf_nodes(bt.root))
