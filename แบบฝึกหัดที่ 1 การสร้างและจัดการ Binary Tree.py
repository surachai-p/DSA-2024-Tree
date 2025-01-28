# สร้างคลาส Node สำหรับโครงสร้างต้นไม้
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ฟังก์ชันสำหรับนับจำนวน Node ทั้งหมดใน Tree
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# ฟังก์ชันสำหรับนับจำนวน Leaf Node (โหนดที่ไม่มีลูก)
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# ฟังก์ชันสำหรับหาความสูงของ Tree
def tree_height(root):
    if root is None:
        return -1  # กำหนดให้ต้นไม้ที่ไม่มีโหนดเลยมีความสูง -1
    return 1 + max(tree_height(root.left), tree_height(root.right))

# ฟังก์ชันสำหรับหาผลรวมค่าของโหนดทั้งหมดใน Tree
def sum_tree(root):
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

# สร้าง Binary Tree ตามที่กำหนด
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

# ทดสอบฟังก์ชัน
print("จำนวน Node ทั้งหมดใน Tree:", count_nodes(root))
print("จำนวน Leaf Node:", count_leaf_nodes(root))
print("ความสูงของ Tree:", tree_height(root))
print("ผลรวมของค่าทั้งหมดใน Tree:", sum_tree(root))
