class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ฟังก์ชันสำหรับการสร้าง Binary Tree
def create_tree():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)
    return root

# 1.1 ฟังก์ชันนับจำนวน Node ทั้งหมดใน Tree
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# 1.2 ฟังก์ชันนับจำนวน Leaf Node (Node ที่ไม่มีลูก)
def count_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)
def find_height(node):
    if node is None:
        return 0
    left_height = find_height(node.left)
    right_height = find_height(node.right)
    return 1 + max(left_height, right_height)
def sum_of_values(node):
    if node is None:
        return 0
    return node.value + sum_of_values(node.left) + sum_of_values(node.right)
if __name__ == "__main__":
    root = create_tree()
    print("จำนวน Node ทั้งหมดใน Tree:", count_nodes(root))  # Output: 7
    print("จำนวน Leaf Node:", count_leaf_nodes(root))    # Output: 4
    print("ความสูงของ Tree:", find_height(root))           # Output: 3
    print("ผลรวมของค่าใน Tree:", sum_of_values(root))      # Output: 70
