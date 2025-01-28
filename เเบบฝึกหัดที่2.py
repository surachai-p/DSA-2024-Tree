class Node:
    def __init__(self, student_id, name):
        self.student_id = student_id  # เก็บรหัสนักศึกษา (Key)
        self.name = name  # เก็บชื่อ-นามสกุล (Value)
        self.left = None  # โหนดลูกทางซ้าย
        self.right = None  # โหนดลูกทางขวา

class StudentBST:
    def __init__(self):
        self.root = None  # กำหนดค่าเริ่มต้นของต้นไม้

    def insert(self, student_id, name):
        self.root = self._insert(self.root, student_id, name)

    def _insert(self, node, student_id, name):
        if node is None:
            return Node(student_id, name)
        if student_id < node.student_id:
            node.left = self._insert(node.left, student_id, name)
        elif student_id > node.student_id:
            node.right = self._insert(node.right, student_id, name)
        return node

    def delete(self, student_id):
        self.root = self._delete(self.root, student_id)

    def _delete(self, node, student_id):
        if node is None:
            return node
        if student_id < node.student_id:
            node.left = self._delete(node.left, student_id)
        elif student_id > node.student_id:
            node.right = self._delete(node.right, student_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.student_id = temp.student_id
            node.name = temp.name
            node.right = self._delete(node.right, temp.student_id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, student_id):
        return self._search(self.root, student_id)

    def _search(self, node, student_id):
        if node is None or node.student_id == student_id:
            return node
        if student_id < node.student_id:
            return self._search(node.left, student_id)
        return self._search(node.right, student_id)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(f"รหัส: {node.student_id}, ชื่อ: {node.name}")
            self._inorder(node.right)

    def count_students(self):
        return self._count_students(self.root)

    def _count_students(self, node):
        if node is None:
            return 0
        return 1 + self._count_students(node.left) + self._count_students(node.right)

def menu():
    bst = StudentBST()
    while True:
        print("\n--- เมนู ---")
        print("1. เพิ่มข้อมูลนักศึกษา")
        print("2. ค้นหาข้อมูลนักศึกษา")
        print("3. ลบข้อมูลนักศึกษา")
        print("4. แสดงรายชื่อนักศึกษาเรียงตามรหัส")
        print("5. แสดงจำนวนนักศึกษาทั้งหมด")
        print("6. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1-6): ")

        if choice == '1':
            student_id = int(input("กรุณากรอกรหัสนักศึกษา: "))
            name = input("กรุณากรอกชื่อ-นามสกุล: ")
            bst.insert(student_id, name)
            print("ข้อมูลนักศึกษาถูกเพิ่มเรียบร้อยแล้ว!")
        elif choice == '2':
            student_id = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการค้นหา: "))
            student = bst.search(student_id)
            if student:
                print(f"พบข้อมูลนักศึกษา: รหัส {student.student_id}, ชื่อ {student.name}")
            else:
                print("ไม่พบนักศึกษาที่ต้องการค้นหา")
        elif choice == '3':
            student_id = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการลบ: "))
            bst.delete(student_id)
            print("ข้อมูลนักศึกษาถูกลบเรียบร้อยแล้ว!")
        elif choice == '4':
            print("\nรายชื่อนักศึกษาเรียงตามรหัส:")
            bst.inorder()
        elif choice == '5':
            print("\nจำนวนนักศึกษาทั้งหมด:", bst.count_students())
        elif choice == '6':
            print("ขอบคุณที่ใช้โปรแกรม!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง, กรุณาลองใหม่.")

# เรียกใช้เมนูเพื่อเริ่มโปรแกรม
menu()