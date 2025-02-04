class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
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
        
def search(root, key):
    # ถ้า root เป็น None หรือ ข้อมูลที่ root ตรงกับ key
    if root is None or root.data == key:
        return root
    
    # ถ้า key น้อยกว่าข้อมูลที่ root ค้นหาใน left subtree
    if root.data > key:
        return search(root.left, key)
    
    # ถ้า key มากกว่าข้อมูลที่ root ค้นหาใน right subtree
    return search(root.right, key)

def insert(root, key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    
    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root

    # ค้นหา Node ที่ต้องการลบ
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # กรณีที่ 1: Node ที่ต้องการลบไม่มีลูก หรือมีลูกแค่ 1 Node
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # กรณีที่ 2: Node ที่ต้องการลบมีลูก 2 Node
        # หาค่าน้อยที่สุดใน right subtree
        temp = find_min(root.right)
        # แทนที่ข้อมูลด้วยค่าน้อยที่สุดที่พบ
        root.data = temp.data
        # ลบ Node ที่นำมาแทนที่
        root.right = delete(root.right, temp.data)
    
    return root

# ตัวอย่างการใช้งาน
root = None
keys = [5, 3, 7, 2, 4, 8]

# เพิ่มข้อมูล
for key in keys:
    root = insert(root, key)

search_result_4 = search(root, 4)
search_result_6 = search(root, 6)
print("ผลการค้นหา:")
print("ค้นหา 4:", "พบ" if search_result_4 else "ไม่พบ")
print("ค้นหา 6:", "พบ" if search_result_6 else "ไม่พบ")

print("\nTraversal เปรียบเทียบ:")
print("Inorder traversal: ", end="")
inorder(root)
print("\nPreorder traversal: ", end="")
preorder(root)
print("\nPostorder traversal: ", end="")
postorder(root)
print()