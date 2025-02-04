# นิยามคลาส Node สำหรับเก็บข้อมูลนักศึกษาใน BST
class Node:
    def __init__(self, key, name):
        self.key = key        # รหัสนักศึกษา
        self.name = name      # ชื่อ-นามสกุล
        self.left = None      # ลูกทางซ้าย
        self.right = None     # ลูกทางขวา

# 2.1) ฟังก์ชันเพิ่มข้อมูลนักศึกษา (Insert)
def insert(root, key, name):
    if root is None:
        return Node(key, name)
    if key < root.key:
        root.left = insert(root.left, key, name)
    elif key > root.key:
        root.right = insert(root.right, key, name)
    else:
        print("รหัสนักศึกษานี้มีอยู่ในระบบแล้ว!")
    return root

# ฟังก์ชันช่วยสำหรับหาค่า node ที่มีค่าน้อยที่สุด (ใช้ในขั้นตอนการลบ)
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

# 2.2) ฟังก์ชันลบข้อมูลนักศึกษาตามรหัส (Delete)
def delete_node(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # เจอ node ที่ต้องการลบแล้ว
        # กรณี node มีลูกน้อยกว่า 1 คน
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # กรณี node มีลูกทั้งสองฝั่ง
        temp = find_min(root.right)
        root.key = temp.key
        root.name = temp.name
        root.right = delete_node(root.right, temp.key)
    return root

# 2.3) ฟังก์ชันค้นหาข้อมูลนักศึกษาตามรหัส (Search)
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

# 2.4) ฟังก์ชันแสดงรายชื่อนักศึกษาเรียงตามรหัส (Inorder Traversal)
def inorder(root):
    if root:
        inorder(root.left)
        print(f"รหัสนักศึกษา: {root.key}, ชื่อ: {root.name}")
        inorder(root.right)

# 2.5) ฟังก์ชันนับจำนวนนักศึกษาทั้งหมด (Count Nodes)
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# เมนูหลักสำหรับการทำงาน
def main():
    root = None  # เริ่มต้น BST ว่างเปล่า
    while True:
        print("\n=== เมนูจัดการข้อมูลนักศึกษา ===")
        print("1. เพิ่มข้อมูลนักศึกษา")
        print("2. ลบข้อมูลนักศึกษาตามรหัส")
        print("3. ค้นหาข้อมูลนักศึกษาตามรหัส")
        print("4. แสดงรายชื่อนักศึกษาเรียงตามรหัส")
        print("5. แสดงจำนวนนักศึกษาทั้งหมด")
        print("6. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกเมนู: ")
        
        if choice == '1':
            try:
                key = int(input("กรุณากรอกรหัสนักศึกษา: "))
                name = input("กรุณากรอกชื่อ-นามสกุล: ")
                root = insert(root, key, name)
                print("เพิ่มข้อมูลนักศึกษาเรียบร้อยแล้ว")
            except ValueError:
                print("กรุณากรอกรหัสเป็นตัวเลขเท่านั้น")
                
        elif choice == '2':
            try:
                key = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการลบ: "))
                root = delete_node(root, key)
                print("ลบข้อมูลนักศึกษาที่มีรหัส", key, "เรียบร้อยแล้ว")
            except ValueError:
                print("กรุณากรอกรหัสเป็นตัวเลขเท่านั้น")
                
        elif choice == '3':
            try:
                key = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการค้นหา: "))
                result = search(root, key)
                if result:
                    print(f"พบข้อมูล: รหัสนักศึกษา: {result.key}, ชื่อ: {result.name}")
                else:
                    print("ไม่พบข้อมูลนักศึกษาที่มีรหัสดังกล่าว")
            except ValueError:
                print("กรุณากรอกรหัสเป็นตัวเลขเท่านั้น")
                
        elif choice == '4':
            print("\n--- รายชื่อนักศึกษาเรียงตามรหัส ---")
            inorder(root)
            
        elif choice == '5':
            total = count_nodes(root)
            print("จำนวนนักศึกษาทั้งหมด:", total)
            
        elif choice == '6':
            print("ออกจากโปรแกรม")
            break
            
        else:
            print("เลือกเมนูไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")

if __name__ == '__main__':
    main()
