class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# สร้าง Binary Tree ตามแบบฝึกหัดที่ 1
root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(7)
root.right.right = Node(8)

# ฟังก์ชันสำหรับ Inorder Traversal
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

# ฟังก์ชันสำหรับ Preorder Traversal
def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# ฟังก์ชันสำหรับ Postorder Traversal
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")

# ทดสอบการ Traversal ทั้ง 3 แบบ
print("Inorder Traversal:")
inorder_traversal(root)  # 2 3 4 5 7 8
print("\nPreorder Traversal:")
preorder_traversal(root)  # 5 3 2 4 7 8
print("\nPostorder Traversal:")
postorder_traversal(root)  # 2 4 3 8 7 5
