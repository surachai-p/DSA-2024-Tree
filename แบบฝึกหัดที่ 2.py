class StudentNode:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.left = None
        self.right = None

class StudentBST:
    def __init__(self):
        self.root = None

    # 2.1 เพิ่มข้อมูลนักศึกษา
    def insert(self, root, student_id, name):
        if root is None:
            return StudentNode(student_id, name)

        if student_id < root.student_id:
            root.left = self.insert(root.left, student_id, name)
        elif student_id > root.student_id:
            root.right = self.insert(root.right, student_id, name)

        return root

    def add_student(self, student_id, name):
        self.root = self.insert(self.root, student_id, name)

    # 2.2 ลบข้อมูลนักศึกษา
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

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
            root.student_id = temp.student_id
            root.name = temp.name
            root.right = self.delete(root.right, temp.student_id)

        return root

    def delete_student(self, student_id):
        self.root = self.delete(self.root, student_id)

    # 2.3 ค้นหาข้อมูลนักศึกษา
    def search(self, root, student_id):
        if root is None or root.student_id == student_id:
            return root

        if student_id < root.student_id:
            return self.search(root.left, student_id)
        return self.search(root.right, student_id)

    def find_student(self, student_id):
        result = self.search(self.root, student_id)
        if result:
            return f"รหัส: {result.student_id}, ชื่อ: {result.name}"
        else:
            return "ไม่พบนักศึกษาที่ค้นหา"

    # 2.4 แสดงรายชื่อนักศึกษาเรียงตามรหัส
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"รหัส: {root.student_id}, ชื่อ: {root.name}")
            self.inorder(root.right)

    def display_students(self):
        self.inorder(self.root)

    # 2.5 แสดงจำนวนนักศึกษาทั้งหมด
    def count_students(self, node):
        if node is None:
            return 0
        return 1 + self.count_students(node.left) + self.count_students(node.right)

    def get_total_students(self):
        return self.count_students(self.root)


bst = StudentBST()
bst.add_student(102, "Alice Smith")
bst.add_student(101, "Bob Johnson")
bst.add_student(104, "Charlie Brown")
bst.add_student(103, "Daisy White")

print("รายชื่อนักศึกษาเรียงตามรหัส:")
bst.display_students()

print("\nค้นหาข้อมูลนักศึกษา (รหัส 103):")
print(bst.find_student(103))

print("\nลบข้อมูลนักศึกษา (รหัส 102)")
bst.delete_student(102)
print("รายชื่อนักศึกษาหลังจากลบ:")
bst.display_students()

print("\nจำนวนนักศึกษาทั้งหมด:", bst.get_total_students())
