class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name  # ชื่อนักศึกษา
        self.left = None  # ลูกซ้าย
        self.right = None  # ลูกขวา

class BST:
    def __init__(self):
        self.root = None

    def insert(self, student_id, name):
        """เพิ่มข้อมูลนักศึกษา"""
        new_student = Student(student_id, name)
        if self.root is None:
            self.root = new_student
        else:
            self._insert_recursive(self.root, new_student)

    def _insert_recursive(self, node, new_student):
        """ช่วยเพิ่มข้อมูลนักศึกษาใน BST"""
        if new_student.student_id < node.student_id:
            if node.left is None:
                node.left = new_student
            else:
                self._insert_recursive(node.left, new_student)
        elif new_student.student_id > node.student_id:
            if node.right is None:
                node.right = new_student
            else:
                self._insert_recursive(node.right, new_student)

    def delete(self, student_id):
        """ลบข้อมูลนักศึกษาตามรหัส"""
        self.root = self._delete_recursive(self.root, student_id)

    def _delete_recursive(self, node, student_id):
        """ช่วยลบข้อมูลนักศึกษาใน BST"""
        if node is None:
            return node
        if student_id < node.student_id:
            node.left = self._delete_recursive(node.left, student_id)
        elif student_id > node.student_id:
            node.right = self._delete_recursive(node.right, student_id)
        else:
            # ถ้าพบแล้ว
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # ถ้ามีลูกทั้งสองข้าง
            min_larger_node = self._get_min(node.right)
            node.student_id, node.name = min_larger_node.student_id, min_larger_node.name
            node.right = self._delete_recursive(node.right, min_larger_node.student_id)
        return node

    def _get_min(self, node):
        """หาต้นไม้ย่อยที่มีค่าน้อยที่สุด"""
        while node.left is not None:
            node = node.left
        return node

    def search(self, student_id):
        """ค้นหาข้อมูลนักศึกษาตามรหัส"""
        return self._search_recursive(self.root, student_id)

    def _search_recursive(self, node, student_id):
        """ช่วยค้นหานักศึกษาใน BST"""
        if node is None:
            return None
        if student_id == node.student_id:
            return node
        elif student_id < node.student_id:
            return self._search_recursive(node.left, student_id)
        else:
            return self._search_recursive(node.right, student_id)

    def inorder(self):
        """แสดงรายชื่อนักศึกษาเรียงตามรหัส"""
        students = []
        self._inorder_recursive(self.root, students)
        return students

    def _inorder_recursive(self, node, students):
        """ช่วยแสดงข้อมูลตามลำดับ Inorder"""
        if node is not None:
            self._inorder_recursive(node.left, students)
            students.append((node.student_id, node.name))
            self._inorder_recursive(node.right, students)

    def count(self):
        """แสดงจำนวนนักศึกษาทั้งหมด"""
        return self._count_recursive(self.root)

    def _count_recursive(self, node):
        """ช่วยนับจำนวนนักศึกษาใน BST"""
        if node is None:
            return 0
        return 1 + self._count_recursive(node.left) + self._count_recursive(node.right)

# ฟังก์ชันหลักที่รับข้อมูลจากผู้ใช้
def main():
    bst = BST()
    while True:
        print("\nเมนู:")
        print("1. เพิ่มข้อมูลนักศึกษา")
        print("2. ลบข้อมูลนักศึกษา")
        print("3. ค้นหาข้อมูลนักศึกษา")
        print("4. แสดงรายชื่อนักศึกษาเรียงตามรหัส")
        print("5. แสดงจำนวนนักศึกษาทั้งหมด")
        print("6. ออกจากโปรแกรม")
        choice = input("เลือกคำสั่ง: ")

        if choice == '1':
            student_id = int(input("กรุณากรอกรหัสนักศึกษา: "))
            name = input("กรุณากรอกชื่อ-นามสกุล: ")
            bst.insert(student_id, name)

        elif choice == '2':
            student_id = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการลบ: "))
            bst.delete(student_id)

        elif choice == '3':
            student_id = int(input("กรุณากรอกรหัสนักศึกษาที่ต้องการค้นหา: "))
            student = bst.search(student_id)
            if student:
                print(f"รหัสนักศึกษา: {student.student_id}, ชื่อ-นามสกุล: {student.name}")
            else:
                print("ไม่พบข้อมูลนักศึกษานี้")

        elif choice == '4':
            students = bst.inorder()
            print("รายชื่อนักศึกษาทั้งหมด (เรียงตามรหัส):")
            for student in students:
                print(f"รหัสนักศึกษา: {student[0]}, ชื่อ-นามสกุล: {student[1]}")

        elif choice == '5':
            print(f"จำนวนทั้งหมดของนักศึกษา: {bst.count()}")

        elif choice == '6':
            print("ออกจากโปรแกรม")
            break

        else:
            print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")

if __name__ == "__main__":
    main()
