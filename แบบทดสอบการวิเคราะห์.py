class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

# สร้าง BST
keys = [5, 3, 7, 2, 4, 8]
root = None
for key in keys:
    root = insert(root, key)

# ทดสอบการค้นหา
print("ทดสอบการค้นหา:")
key_to_search = [4, 6]
for key in key_to_search:
    result = search(root, key)
    if result:
        print(f"ข้อมูล {key} พบใน BST")
    else:
        print(f"ข้อมูล {key} ไม่พบใน BST")

# เปรียบเทียบผลการ Traversal
print("\nTraversal Results:")
print("Inorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
