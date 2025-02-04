# นิยามคลาส Node สำหรับเก็บข้อมูลคำศัพท์ใน Binary Search Tree
class Node:
    def __init__(self, english, thai, word_type, example):
        self.english = english        # คำศัพท์ภาษาอังกฤษ (key)
        self.thai = thai              # คำแปลภาษาไทย
        self.word_type = word_type    # ชนิดของคำ (noun, verb, adjective, etc.)
        self.example = example        # ตัวอย่างประโยค
        self.left = None              # ลูกด้านซ้าย
        self.right = None             # ลูกด้านขวา

# 1) ฟังก์ชันเพิ่มคำศัพท์และความหมาย (Insert)
def insert(root, english, thai, word_type, example):
    if root is None:
        return Node(english, thai, word_type, example)
    if english < root.english:
        root.left = insert(root.left, english, thai, word_type, example)
    elif english > root.english:
        root.right = insert(root.right, english, thai, word_type, example)
    else:
        print("คำศัพท์นี้มีอยู่ในพจนานุกรมแล้ว!")
    return root

# ฟังก์ชันช่วยสำหรับหาค่า Node ที่มีค่าน้อยที่สุดใน subtree (ใช้ในขั้นตอนการลบ)
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

# 2) ฟังก์ชันลบคำศัพท์
def delete_node(root, english):
    if root is None:
        return root
    if english < root.english:
        root.left = delete_node(root.left, english)
    elif english > root.english:
        root.right = delete_node(root.right, english)
    else:
        # พบ Node ที่ต้องการลบแล้ว
        # กรณีที่ Node มีลูกน้อยกว่า 2 ฝั่ง
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # กรณีที่ Node มีลูกทั้งสองฝั่ง
        temp = find_min(root.right)
        # นำข้อมูลจาก Node ที่น้อยที่สุดใน subtree ขวาแทนที่
        root.english = temp.english
        root.thai = temp.thai
        root.word_type = temp.word_type
        root.example = temp.example
        # ลบ Node ที่ใช้แทนที่ออกไปใน subtree ขวา
        root.right = delete_node(root.right, temp.english)
    return root

# 3) ฟังก์ชันค้นหาคำศัพท์
def search(root, english):
    if root is None or root.english == english:
        return root
    if english < root.english:
        return search(root.left, english)
    else:
        return search(root.right, english)

# ฟังก์ชันสำหรับแสดงข้อมูลคำศัพท์ (ตัวเลือกเพิ่มเติม)
def display_entry(entry):
    if entry:
        print("-------------------------------------------------")
        print("คำศัพท์ภาษาอังกฤษ :", entry.english)
        print("คำแปลภาษาไทย     :", entry.thai)
        print("ชนิดของคำ         :", entry.word_type)
        print("ตัวอย่างประโยค    :", entry.example)
        print("-------------------------------------------------")
    else:
        print("ไม่พบคำศัพท์ที่ค้นหา")

# เมนูหลักสำหรับระบบพจนานุกรม
def main():
    root = None  # เริ่มต้น Binary Search Tree ว่าง
    while True:
        print("\n======= ระบบพจนานุกรม =======")
        print("1. เพิ่มคำศัพท์และความหมาย")
        print("2. ลบคำศัพท์")
        print("3. ค้นหาคำศัพท์")
        print("4. ออกจากโปรแกรม")
        choice = input("กรุณาเลือกเมนู: ")

        if choice == '1':
            english = input("กรุณากรอกคำศัพท์ภาษาอังกฤษ: ").strip()
            thai = input("กรุณากรอกคำแปลภาษาไทย: ").strip()
            word_type = input("กรุณากรอกชนิดของคำ (noun, verb, adjective, etc.): ").strip()
            example = input("กรุณากรอกตัวอย่างประโยค: ").strip()
            root = insert(root, english, thai, word_type, example)
            print("เพิ่มคำศัพท์เรียบร้อยแล้ว!")

        elif choice == '2':
            english = input("กรุณากรอกคำศัพท์ที่ต้องการลบ: ").strip()
            # ตรวจสอบว่าคำศัพท์มีอยู่ในระบบหรือไม่
            found = search(root, english)
            if found:
                root = delete_node(root, english)
                print("ลบคำศัพท์เรียบร้อยแล้ว!")
            else:
                print("ไม่พบคำศัพท์ที่ต้องการลบ!")

        elif choice == '3':
            english = input("กรุณากรอกคำศัพท์ที่ต้องการค้นหา: ").strip()
            result = search(root, english)
            display_entry(result)

        elif choice == '4':
            print("ออกจากโปรแกรม")
            break

        else:
            print("เลือกเมนูไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")

if __name__ == '__main__':
    main()
