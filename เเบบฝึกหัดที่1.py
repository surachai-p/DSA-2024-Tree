class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def count_nodes(root):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)

def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return count_leaves(root.left) + count_leaves(root.right)

def height(root):
    if root is None:
        return -1
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return 1 + max(left_height, right_height)

def sum_nodes(root):
    if root is None:
        return 0
    return root.data + sum_nodes(root.left) + sum_nodes(root.right)

# สร้าง Binary Tree ตามโจทย์
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

# เรียกใช้ฟังก์ชันต่างๆ
print("จำนวน Node ทั้งหมด:", count_nodes(root))
print("จำนวน Leaf Node:", count_leaves(root))
print("ความสูงของ Tree:", height(root))
print("ผลรวมของค่าใน Tree:", sum_nodes(root))