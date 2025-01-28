class Node:
    def __init__(self, key, name):
        self.key = key  # รหัสนักศึกษา
        self.name = name  # ชื่อ-นามสกุล
        self.left = None
        self.right = None

# 2.1 เพิ่มข้อมูลนักศึกษา
def insert(root, key, name):
    if root is None:
        return Node(key, name)
    if key < root.key:
        root.left = insert(root.left, key, name)
    elif key > root.key:
        root.right = insert(root.right, key, name)
    return root

# 2.2 ลบข้อมูลนักศึกษาตามรหัส
def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.name = temp.name
        root.right = delete(root.right, temp.key)
    return root

# 2.3 ค้นหาข้อมูลนักศึกษาตามรหัส
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

# 2.4 แสดงรายชื่อนักศึกษาเรียงตามรหัส
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(f"รหัส: {root.key}, ชื่อ: {root.name}")
        inorder_traversal(root.right)

# 2.5 แสดงจำนวนนักศึกษาทั้งหมด
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# โปรแกรมหลัก
root = None

# เพิ่มข้อมูลนักศึกษา
root = insert(root,158 , "อิ๋ง")
root = insert(root, 178, "อัง")
root = insert(root, 188, "เนย")
root = insert(root, 196, "เอย")

print("รายชื่อนักศึกษาเรียงตามรหัส:")
inorder_traversal(root)

# ค้นหานักศึกษาตามรหัส
search_key = 178
result = search(root, search_key)
if result:
    print(f"\nค้นหาพบ: รหัส {result.key}, ชื่อ {result.name}")
else:
    print(f"\nไม่พบข้อมูลนักศึกษาที่มีรหัส {search_key}")

# ลบนักศึกษาตามรหัส
delete_key = 196
root = delete(root, delete_key)
print(f"\nหลังลบข้อมูลนักศึกษาที่มีรหัส {delete_key}:")
inorder_traversal(root)

# แสดงจำนวนนักศึกษาทั้งหมด
print(f"\nจำนวนนักศึกษาทั้งหมด: {count_nodes(root)}")
