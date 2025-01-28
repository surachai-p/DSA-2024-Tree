class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def count_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

def sum_tree(node):
    if node is None:
        return 0
    return node.data + sum_tree(node.left) + sum_tree(node.right)

print("จำนวน Node ทั้งหมดใน Tree:", count_nodes(root)) 
print("จำนวน Leaf Node ใน Tree:", count_leaf_nodes(root)) 
print("ความสูงของ Tree:", tree_height(root)) 
print("ผลรวมของค่าใน Tree:", sum_tree(root)) 