class Node:
    def __init__(self, student_id, name):
        self.student_id = student_id  # รหัสนักศึกษา
        self.name = name  # ชื่อ-นามสกุล
        self.left = None  # ลูกซ้าย
        self.right = None  # ลูกขวา

class StudentBST:
    def __init__(self):
        self.root = None

    # ฟังก์ชันเพิ่มข้อมูลนักศึกษา
    def insert(self, root, student_id, name):
        if root is None:
            return Node(student_id, name)
        
        if student_id < root.student_id:
            root.left = self.insert(root.left, student_id, name)
        elif student_id > root.student_id:
            root.right = self.insert(root.right, student_id, name)
        return root

    # ฟังก์ชันค้นหาข้อมูลนักศึกษาตามรหัส
    def search(self, root, student_id):
        if root is None or root.student_id == student_id:
            return root
        if student_id < root.student_id:
            return self.search(root.left, student_id)
        return self.search(root.right, student_id)

    # ฟังก์ชันลบข้อมูลนักศึกษาตามรหัส
    def delete(self, root, student_id):
        if root is None:
            return root

        if student_id < root.student_id:
            root.left = self.delete(root.left, student_id)
        elif student_id > root.student_id:
            root.right = self.delete(root.right, student_id)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.find_min(root.right)
            root.student_id, root.name = temp.student_id, temp.name
            root.right = self.delete(root.right, temp.student_id)
        return root

    # ฟังก์ชันหาค่าต่ำสุดในต้นไม้
    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    # ฟังก์ชันแสดงรายชื่อนักศึกษาเรียงตามรหัส
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"Student ID: {root.student_id}, Name: {root.name}")
            self.inorder(root.right)

    # ฟังก์ชันแสดงจำนวนนักศึกษาทั้งหมด
    def count_students(self, root):
        if root is None:
            return 0
        return 1 + self.count_students(root.left) + self.count_students(root.right)

# การทดสอบ
students = StudentBST()

# เพิ่มข้อมูลนักศึกษา
students.root = students.insert(students.root, 123, "Toon")
students.root = students.insert(students.root, 456, "Ohmes")
students.root = students.insert(students.root, 789, "Pao")
students.root = students.insert(students.root, 101, "Nami")
students.root = students.insert(students.root, 567, "Phum")

# ค้นหานักศึกษาตามรหัส
student = students.search(students.root, 456)
if student:
    print(f"\nFound student: {student.name} with ID: {student.student_id}")
else:
    print("\nStudent not found.")

# แสดงรายชื่อนักศึกษาเรียงตามรหัส
print("\nList of students sorted by ID:")
students.inorder(students.root)

# ลบข้อมูลนักศึกษาตามรหัส
students.root = students.delete(students.root, 456)
print("\nAfter deleting student with ID 456:")
students.inorder(students.root)

# แสดงจำนวนนักศึกษาทั้งหมด
print("\nTotal number of students:", students.count_students(students.root))
