class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# สร้าง Binary Tree
root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(7)
root.right.right = Node(8)

# ฟังก์ชันสำหรับพิมพ์ Binary Tree ในรูปแบบโครงสร้างต้นไม้
def print_tree(node, level=0, side="Root"):
    if node is not None:
        print(" " * (4 * level) + f"{side}: {node.data}")  # แสดงข้อมูลโหนดตามระดับ
        print_tree(node.left, level + 1, "L")  # แสดงโหนดฝั่งซ้าย
        print_tree(node.right, level + 1, "R")  # แสดงโหนดฝั่งขวา

# ทดสอบการพิมพ์โครงสร้างต้นไม้
print("Binary Tree Structure:")
print_tree(root)

