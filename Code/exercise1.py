class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # 1.1 ฟังก์ชันนับจำนวน Node ทั้งหมด
    def count_nodes(self, node):
        if node is None:
            return 0
        left_count = self.count_nodes(node.left)
        right_count = self.count_nodes(node.right)
        return 1 + left_count + right_count

    # 1.2 ฟังก์ชันนับจำนวน Leaf Node
    def count_leaf_nodes(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        left_leaf = self.count_leaf_nodes(node.left)
        right_leaf = self.count_leaf_nodes(node.right)
        return left_leaf + right_leaf

    # 1.3 ฟังก์ชันหาความสูงของ Tree
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    # 1.4 ฟังก์ชันหาผลรวมของค่าใน Tree
    def sum_of_values(self, node):
        if node is None:
            return 0
        left_sum = self.sum_of_values(node.left)
        right_sum = self.sum_of_values(node.right)
        return node.value + left_sum + right_sum

# สร้าง Binary Tree
bt = BinaryTree()
values = [10, 5, 15, 3, 7, 12, 18]
for val in values:
    bt.insert(val)

# ทดสอบฟังก์ชันต่างๆ
print("จำนวน Node ทั้งหมดใน Tree:", bt.count_nodes(bt.root))
print("จำนวน Leaf Node ใน Tree:", bt.count_leaf_nodes(bt.root))
print("ความสูงของ Tree:", bt.height(bt.root))
print("ผลรวมของค่าใน Tree:", bt.sum_of_values(bt.root))
