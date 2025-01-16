class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# สร้าง Binary Tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

# 1.1 ฟังก์ชันนับจำนวน Node ทั้งหมด
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# 1.2 ฟังก์ชันนับจำนวน Leaf Node
def count_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)

# 1.3 ฟังก์ชันหาความสูงของ Tree
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# 1.4 ฟังก์ชันหาผลรวมของค่าใน Tree
def sum_tree(node):
    if node is None:
        return 0
    return node.data + sum_tree(node.left) + sum_tree(node.right)

# ทดสอบฟังก์ชัน
print("จำนวน Node ทั้งหมดใน Tree:", count_nodes(root))  # 7
print("จำนวน Leaf Node ใน Tree:", count_leaf_nodes(root))  # 4
print("ความสูงของ Tree:", tree_height(root))  # 3
print("ผลรวมของค่าใน Tree:", sum_tree(root))  # 70
