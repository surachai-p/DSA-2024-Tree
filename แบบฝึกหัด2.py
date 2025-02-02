class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ฟังก์ชันเพิ่มข้อมูลใน BST
def insert(root, key):
    if root is None:
        return Node(key)
    
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    
    return root

# ฟังก์ชันหาค่าที่น้อยที่สุดใน Subtree
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# ฟังก์ชันลบข้อมูลใน BST
def delete(root, key):
    if root is None:
        return root

    # ค้นหา Node ที่ต้องการลบ
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # กรณีที่ 1: Node ไม่มีลูก หรือมีลูกเพียงหนึ่ง
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # กรณีที่ 2: Node มีลูกสอง Node
        # หาค่าที่น้อยที่สุดใน Subtree ด้านขวา
        temp = find_min(root.right)
        # แทนค่าของ Node ที่ต้องการลบด้วยค่าที่เจอ
        root.data = temp.data
        # ลบ Node ที่นำค่ามาแทน
        root.right = delete(root.right, temp.data)
    
    return root

# ฟังก์ชันท่อง Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    root = None
    keys = [5, 3, 7, 2, 4, 8]

    # เพิ่มข้อมูลใน BST
    for key in keys:
        root = insert(root, key)

    print("ก่อนลบข้อมูล:")
    inorder(root)  # Output: 2 3 4 5 7 8

    # ลบข้อมูล
    root = delete(root, 3)
    print("\nหลังลบข้อมูล 3:")
    inorder(root)  # Output: 2 4 5 7 8