class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# ฟังก์ชันสำหรับการสร้าง Binary Tree
def create_binary_tree():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)
    return root

# 1.1 ฟังก์ชันนับจำนวน Node ทั้งหมดใน Tree
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# 1.2 ฟังก์ชันนับจำนวน Leaf Node
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# 1.3 ฟังก์ชันหาความสูงของ Tree
def tree_height(root):
    if root is None:
        return 0
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return 1 + max(left_height, right_height)

# 1.4 ฟังก์ชันหาผลรวมของค่าใน Tree
def sum_tree(root):
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)

# สร้าง Binary Tree
root = create_binary_tree()

# เรียกใช้งานฟังก์ชันต่าง ๆ
print("จำนวน Node ทั้งหมดใน Tree:", count_nodes(root))
print("จำนวน Leaf Node ใน Tree:", count_leaf_nodes(root))
print("ความสูงของ Tree:", tree_height(root))
print("ผลรวมของค่าทั้งหมดใน Tree:", sum_tree(root))
