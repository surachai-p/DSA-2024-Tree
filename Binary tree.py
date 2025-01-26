class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # ฟังก์ชันนับจำนวน Node ทั้งหมดใน Tree
    def count_nodes(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    # ฟังก์ชันนับจำนวน Leaf Node (โหนดที่ไม่มีลูก)
    def count_leaf_nodes(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        else:
            return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)

    # ฟังก์ชันหาความสูงของ Tree
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1

    # ฟังก์ชันหาผลรวมของค่าใน Tree
    def sum_values(self, node):
        if node is None:
            return 0
        else:
            return node.value + self.sum_values(node.left) + self.sum_values(node.right)

# สร้าง Binary Tree ตามโครงสร้างที่ให้มา
tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(5)
tree.root.right = Node(15)
tree.root.left.left = Node(3)
tree.root.left.right = Node(7)
tree.root.right.left = Node(12)
tree.root.right.right = Node(18)

# ทดสอบฟังก์ชันต่างๆ
print("จำนวน Node ทั้งหมดใน Tree:", tree.count_nodes(tree.root))  # 7
print("จำนวน Leaf Node:", tree.count_leaf_nodes(tree.root))        # 4
print("ความสูงของ Tree:", tree.height(tree.root))                  # 3
print("ผลรวมของค่าใน Tree:", tree.sum_values(tree.root))         # 70
