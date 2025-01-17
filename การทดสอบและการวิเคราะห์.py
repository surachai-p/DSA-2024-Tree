#1. จงสร้าง BST จากข้อมูลต่อไปนี้: 5, 3, 7, 2, 4, 8
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# ฟังก์ชันสำหรับการเพิ่มค่าใน BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# ฟังก์ชันสำหรับการค้นหาใน BST
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

# Inorder Traversal (Left -> Root -> Right)
def inorder(root):
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []

# Preorder Traversal (Root -> Left -> Right)
def preorder(root):
    return [root.key] + preorder(root.left) + preorder(root.right) if root else []

# Postorder Traversal (Left -> Right -> Root)
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.key] if root else []

# สร้าง BST
root = None
data = [5, 3, 7, 2, 4, 8]
for num in data:
    root = insert(root, num)

# ค้นหาข้อมูล
search_result_4 = search(root, 4)
search_result_6 = search(root, 6)

# 2.ทดสอบการค้นหาข้อมูล 4 และ 6
print("ค้นหา 4:", "พบค่า" if search_result_4 else "ไม่พบค่า")
print("ค้นหา 6:", "พบค่า" if search_result_6 else "ไม่พบค่า")

# 3.เปรียบเทียบผลการ Traversal ทั้ง 3 แบบ
print("\nTraversal ทั้ง 3 แบบ:")
print("Inorder:", inorder(root))
print("Preorder:", preorder(root))
print("Postorder:", postorder(root))
