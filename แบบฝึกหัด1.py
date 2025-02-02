class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ฟังก์ชันสำหรับการท่อง Binary Tree
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

# สร้าง Binary Tree ตามโจทย์
#       5
#      / \
#     3   7
#    / \   \
#   2   4   8

# สร้าง root node
root = Node(5)

# สร้าง left subtree
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)

# สร้าง right subtree
root.right = Node(7)
root.right.right = Node(8)

# การทดสอบการท่อง Binary Tree
print("Inorder Traversal:")
inorder(root)  # Output: 2 3 4 5 7 8

print("\nPreorder Traversal:")
preorder(root)  # Output: 5 3 2 4 7 8

print("\nPostorder Traversal:")
postorder(root)  # Output: 2 4 3 8 7 5

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ฟังก์ชันสร้างต้นไม้
def create_tree():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)
    return root

# 1.1) ฟังก์ชันนับจำนวน Node ทั้งหมดใน Tree
def count_nodes(root):
    if root is None:
        return 0
    # รวมจำนวน Node ใน left และ right subtree และรวมตัว Root
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# 1.2) ฟังก์ชันนับจำนวน Leaf Node
def count_leaf_nodes(root):
    if root is None:
        return 0
    # ถ้า Node ไม่มีลูกซ้ายและขวา แสดงว่าเป็น Leaf Node
    if root.left is None and root.right is None:
        return 1
    # ถ้ามีลูก ให้ไปนับในลูกซ้ายและลูกขวา
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# 1.3) ฟังก์ชันหาความสูงของ Tree
def tree_height(root):
    if root is None:
        return 0
    # ความสูงคือ 1 บวกกับความสูงของ Subtree ซ้ายและขวา
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return 1 + max(left_height, right_height)

# 1.4) ฟังก์ชันหาผลรวมของค่าใน Tree
def sum_tree(root):
    if root is None:
        return 0
    # ผลรวมของข้อมูลคือข้อมูลของ root + ผลรวมของ Subtree ซ้ายและขวา
    return root.data + sum_tree(root.left) + sum_tree(root.right)

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    # สร้างต้นไม้
    root = create_tree()

    # 1.1) นับจำนวน Node ทั้งหมด
    total_nodes = count_nodes(root)
    print(f"จำนวน Node ทั้งหมดใน Tree: {total_nodes}")

    # 1.2) นับจำนวน Leaf Node
    total_leaf_nodes = count_leaf_nodes(root)
    print(f"จำนวน Leaf Node: {total_leaf_nodes}")

    # 1.3) หาความสูงของ Tree
    height = tree_height(root)
    print(f"ความสูงของ Tree: {height}")

    # 1.4) หาผลรวมของค่าใน Tree
    total_sum = sum_tree(root)
    print(f"ผลรวมของค่าใน Tree: {total_sum}")