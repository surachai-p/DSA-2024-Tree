class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.left = None
        self.right = None

class StudentBST:
    def __init__(self):
        self.root = None

    # 2.1 ฟังก์ชันเพิ่มข้อมูลนักศึกษา
    def insert(self, student_id, name):
        if self.root is None:
            self.root = Student(student_id, name)
        else:
            self._insert_recursive(self.root, student_id, name)

    def _insert_recursive(self, node, student_id, name):
        if student_id < node.student_id:
            if node.left is None:
                node.left = Student(student_id, name)
            else:
                self._insert_recursive(node.left, student_id, name)
        else:
            if node.right is None:
                node.right = Student(student_id, name)
            else:
                self._insert_recursive(node.right, student_id, name)

    # 2.2 ฟังก์ชันลบข้อมูลนักศึกษาตามรหัส
    def delete(self, student_id):
        self.root = self._delete_recursive(self.root, student_id)

    def _delete_recursive(self, node, student_id):
        if node is None:
            return node
        if student_id < node.student_id:
            node.left = self._delete_recursive(node.left, student_id)
        elif student_id > node.student_id:
            node.right = self._delete_recursive(node.right, student_id)
        else:
            # Node to be deleted found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Find the minimum value node in the right subtree
                min_node = self._min_value_node(node.right)
                node.student_id, node.name = min_node.student_id, min_node.name
                node.right = self._delete_recursive(node.right, min_node.student_id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # 2.3 ฟังก์ชันค้นหาข้อมูลนักศึกษาตามรหัส
    def search(self, student_id):
        return self._search_recursive(self.root, student_id)

    def _search_recursive(self, node, student_id):
        if node is None:
            return None
        if student_id == node.student_id:
            return node
        elif student_id < node.student_id:
            return self._search_recursive(node.left, student_id)
        else:
            return self._search_recursive(node.right, student_id)

    # 2.4 ฟังก์ชันแสดงรายชื่อนักศึกษาเรียงตามรหัส (Inorder Traversal)
    def display_inorder(self, node, result):
        if node:
            self.display_inorder(node.left, result)
            result.append(f"{node.student_id}: {node.name}")
            self.display_inorder(node.right, result)

    # 2.5 ฟังก์ชันแสดงจำนวนนักศึกษาทั้งหมด
    def count_students(self, node):
        if node is None:
            return 0
        return 1 + self.count_students(node.left) + self.count_students(node.right)

def main():
    bst = StudentBST()

    while True:
        print("\n*** เมนูหลัก ***")
        print("1. เพิ่มข้อมูลนักศึกษา")
        print("2. ลบข้อมูลนักศึกษาตามรหัส")
        print("3. ค้นหาข้อมูลนักศึกษาตามรหัส")
        print("4. แสดงรายชื่อนักศึกษาเรียงตามรหัส")
        print("5. แสดงจำนวนนักศึกษาทั้งหมด")
        print("6. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1-6): ")

        if choice == '1':
            student_id = int(input("กรุณาระบุรหัสนักศึกษา: "))
            name = input("กรุณาระบุชื่อ-นามสกุล: ")
            bst.insert(student_id, name)
            print("เพิ่มข้อมูลนักศึกษาเรียบร้อยแล้ว")

        elif choice == '2':
            student_id = int(input("กรุณาระบุรหัสนักศึกษาที่ต้องการลบ: "))
            bst.delete(student_id)
            print(f"ลบข้อมูลนักศึกษารหัส {student_id} เรียบร้อยแล้ว")

        elif choice == '3':
            student_id = int(input("กรุณาระบุรหัสนักศึกษาที่ต้องการค้นหา: "))
            found_student = bst.search(student_id)
            if found_student:
                print(f"พบข้อมูลนักศึกษา: {found_student.student_id}: {found_student.name}")
            else:
                print("ไม่พบข้อมูลนักศึกษาที่ค้นหา")

        elif choice == '4':
            inorder_result = []
            bst.display_inorder(bst.root, inorder_result)
            print("\nรายชื่อนักศึกษาเรียงตามรหัส:")
            for student in inorder_result:
                print(student)

        elif choice == '5':
            total_students = bst.count_students(bst.root)
            print(f"\nจำนวนนักศึกษาทั้งหมด: {total_students}")

        elif choice == '6':
            print("ขอขอบคุณที่ใช้โปรแกรม!")
            break

        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")

if __name__ == "__main__":
    main()
