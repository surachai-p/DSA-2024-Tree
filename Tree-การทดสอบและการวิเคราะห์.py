class Node:
    def __init__(self, key):
        self.data = key
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
        return root  # Found or not found
    
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

# สร้าง BST
root = None
keys = [5, 3, 7, 2, 4, 8]
for key in keys:
    root = insert(root, key)

# ทดสอบการค้นหา
print("Search for 4:", "Found" if search(root, 4) else "Not Found")
print("Search for 6:", "Found" if search(root, 6) else "Not Found")

# เปรียบเทียบการ Traversal
print("\nIn-order Traversal:")
inorder(root)  # 2 3 4 5 7 8
print("\nPre-order Traversal:")
preorder(root)  # 5 3 2 4 7 8
print("\nPost-order Traversal:")
postorder(root)  # 2 4 3 8 7 5

