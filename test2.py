class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id  # รหัสนักศึกษา (key)
        self.name = name  # ชื่อ-นามสกุล
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 2.1 ฟังก์ชันเพิ่มข้อมูลนักศึกษา
    def add_student(self, student_id, name):
        new_student = Student(student_id, name)
        if self.root is None:
            self.root = new_student
        else:
            self._add(self.root, new_student)

    def _add(self, current_node, new_student):
        if new_student.student_id < current_node.student_id:
            if current_node.left is None:
                current_node.left = new_student
            else:
                self._add(current_node.left, new_student)
        elif new_student.student_id > current_node.student_id:
            if current_node.right is None:
                current_node.right = new_student
            else:
                self._add(current_node.right, new_student)

    # 2.2 ฟังก์ชันลบข้อมูลนักศึกษาตามรหัส
    def remove_student(self, student_id):
        self.root = self._remove(self.root, student_id)

    def _remove(self, node, student_id):
        if node is None:
            return node
        
        # ค้นหานักศึกษาที่ต้องการลบ
        if student_id < node.student_id:
            node.left = self._remove(node.left, student_id)
        elif student_id > node.student_id:
            node.right = self._remove(node.right, student_id)
        else:
            # กรณีที่พบ node ที่ต้องการลบ
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # หา node ที่มีค่าต่ำที่สุดใน subtree ขวามาแทน
            node.student_id, node.name = self._min_value_node(node.right)
            node.right = self._remove(node.right, node.student_id)
        
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.student_id, current.name

    # 2.3 ฟังก์ชันค้นหาข้อมูลนักศึกษาตามรหัส
    def find_student(self, student_id):
        return self._find(self.root, student_id)

    def _find(self, node, student_id):
        if node is None:
            return None
        if student_id == node.student_id:
            return node
        elif student_id < node.student_id:
            return self._find(node.left, student_id)
        else:
            return self._find(node.right, student_id)

    # 2.4 ฟังก์ชันแสดงรายชื่อนักศึกษาเรียงตามรหัส
    def display_students_in_order(self):
        students = []
        self._in_order_traversal(self.root, students)
        return students

    def _in_order_traversal(self, node, students):
        if node is not None:
            self._in_order_traversal(node.left, students)
            students.append((node.student_id, node.name))
            self._in_order_traversal(node.right, students)

    # 2.5 ฟังก์ชันแสดงจำนวนนักศึกษาทั้งหมด
    def count_students(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)


# ฟังก์ชันสำหรับการรับข้อมูลจากผู้ใช้และเรียกใช้งาน
def main():
    bst = BinarySearchTree()

    while True:
        print("\n*** ระบบจัดการข้อมูลนักศึกษา ***")
        print("1. เพิ่มข้อมูลนักศึกษา")
        print("2. ลบข้อมูลนักศึกษาตามรหัส")
        print("3. ค้นหาข้อมูลนักศึกษาตามรหัส")
        print("4. แสดงรายชื่อนักศึกษาเรียงตามรหัส")
        print("5. แสดงจำนวนนักศึกษาทั้งหมด")
        print("6. ออกจากโปรแกรม")

        choice = input("กรุณาเลือกตัวเลือก (1-6): ")

        if choice == "1":
            # 2.1 เพิ่มข้อมูลนักศึกษา
            student_id = int(input("กรอกรหัสนักศึกษา: "))
            name = input("กรอกชื่อ-นามสกุลของนักศึกษา: ")
            bst.add_student(student_id, name)
            print(f"เพิ่มนักศึกษา {name} (รหัส {student_id}) สำเร็จ")

        elif choice == "2":
            # 2.2 ลบข้อมูลนักศึกษาตามรหัส
            student_id = int(input("กรอกรหัสนักศึกษาที่ต้องการลบ: "))
            bst.remove_student(student_id)
            print(f"ลบข้อมูลนักศึกษาที่รหัส {student_id} สำเร็จ")

        elif choice == "3":
            # 2.3 ค้นหาข้อมูลนักศึกษาตามรหัส
            student_id = int(input("กรอกรหัสนักศึกษาที่ต้องการค้นหา: "))
            student = bst.find_student(student_id)
            if student:
                print(f"พบข้อมูลนักศึกษา: รหัส {student.student_id}, ชื่อ {student.name}")
            else:
                print("ไม่พบข้อมูลนักศึกษาที่ค้นหา")

        elif choice == "4":
            # 2.4 แสดงรายชื่อนักศึกษาเรียงตามรหัส
            students_in_order = bst.display_students_in_order()
            print("รายชื่อนักศึกษาเรียงตามรหัส:")
            for student in students_in_order:
                print(f"รหัส {student[0]}, ชื่อ {student[1]}")

        elif choice == "5":
            # 2.5 แสดงจำนวนนักศึกษาทั้งหมด
            print(f"จำนวนนักศึกษาทั้งหมด: {bst.count_students()}")

        elif choice == "6":
            # ออกจากโปรแกรม
            print("ขอบคุณที่ใช้โปรแกรม!")
            break

        else:
            print("เลือกตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่.")

if __name__ == "__main__":
    main()
