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
