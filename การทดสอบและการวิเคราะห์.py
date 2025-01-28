class Node:
    def __init__(self, value):
        self.value = value  # ค่าของโหนด
        self.left = None    # ลูกฝั่งซ้าย
        self.right = None   # ลูกฝั่งขวา

# ฟังก์ชันเพิ่มโหนดเข้า BST
def insert(root, value):
    if root is None:  # ถ้าไม่มี root ให้สร้าง root ใหม่
        return Node(value)
    if value < root.value:  # ถ้าค่าที่เพิ่มน้อยกว่า root ให้เพิ่มในฝั่งซ้าย
        root.left = insert(root.left, value)
    else:  # ถ้าค่าที่เพิ่มมากกว่า root ให้เพิ่มในฝั่งขวา
        root.right = insert(root.right, value)
    return root

# สร้าง BST
values = [5, 3, 7, 2, 4, 8]
root = None
for value in values:
    root = insert(root, value)

# ฟังก์ชันค้นหาค่าใน BST
def search(root, key):
    if root is None:
        return False  # ไม่พบค่าในต้นไม้
    if root.value == key:
        return True  # พบค่าในต้นไม้
    if key < root.value:
        return search(root.left, key)  # ค้นหาฝั่งซ้าย
    return search(root.right, key)  # ค้นหาฝั่งขวา

# ทดสอบการค้นหา 4 และ 6
print("Search 4:", search(root, 4)) 
print("Search 6:", search(root, 6))  

# Inorder Traversal (ซ้าย -> Root -> ขวา)
def inorder(root):
    return inorder(root.left) + [root.value] + inorder(root.right) if root else []

# Preorder Traversal (Root -> ซ้าย -> ขวา)
def preorder(root):
    return [root.value] + preorder(root.left) + preorder(root.right) if root else []

# Postorder Traversal (ซ้าย -> ขวา -> Root)
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.value] if root else []

# เปรียบเทียบผลการ Traversal
print("Inorder Traversal:", inorder(root))    # คาดหวังผลลัพธ์: [2, 3, 4, 5, 7, 8]
print("Preorder Traversal:", preorder(root))  # คาดหวังผลลัพธ์: [5, 3, 2, 4, 7, 8]
print("Postorder Traversal:", postorder(root))# คาดหวังผลลัพธ์: [2, 4, 3, 8, 7, 5]
