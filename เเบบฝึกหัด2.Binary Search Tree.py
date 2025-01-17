class StudentNode:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.left = None
        self.right = None

class StudentBST:
    def __init__(self):
        self.root = None

    # 2.1 เพิ่มข้อมูลนักศึกษา
    def add_student(self, key, name):
        def insert(node, key, name):
            if node is None:
                return StudentNode(key, name)
            if key < node.key:
                node.left = insert(node.left, key, name)
            elif key > node.key:
                node.right = insert(node.right, key, name)
            return node

        self.root = insert(self.root, key, name)

    # 2.2 ลบข้อมูลนักศึกษาตามรหัส
    def delete_student(self, key):
        def delete(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = delete(node.left, key)
            elif key > node.key:
                node.right = delete(node.right, key)
            else:
                # Node to be deleted found
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                # Node with two children
                min_larger_node = self.get_min(node.right)
                node.key, node.name = min_larger_node.key, min_larger_node.name
                node.right = delete(node.right, min_larger_node.key)
            return node

        self.root = delete(self.root, key)

    # ฟังก์ชันหา Node ที่มีค่าน้อยที่สุด
    def get_min(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

    # 2.3 ค้นหาข้อมูลนักศึกษาตามรหัส
    def search_student(self, key):
        def search(node, key):
            if node is None or node.key == key:
                return node
            if key < node.key:
                return search(node.left, key)
            return search(node.right, key)

        return search(self.root, key)

    # 2.4 แสดงรายชื่อนักศึกษาเรียงตามรหัส
    def display_students(self):
        def inorder(node):
            if node:
                inorder(node.left)
                print(f"รหัส: {node.key}, ชื่อ: {node.name}")
                inorder(node.right)

        inorder(self.root)

    # 2.5 แสดงจำนวนนักศึกษาทั้งหมด
    def count_students(self):
        def count(node):
            if node is None:
                return 0
            return 1 + count(node.left) + count(node.right)

        return count(self.root)

# การใช้งาน
bst = StudentBST()

# เพิ่มข้อมูลนักศึกษา
bst.add_student(66030281, "Wipatsasicha")
bst.add_student(66030284, "Sronsawan")
bst.add_student(66030213, "Kannika")
bst.add_student(66030243, "Thanyatep")

# ลบข้อมูลนักศึกษา
bst.delete_student(1002)

# ค้นหาข้อมูลนักศึกษา
student = bst.search_student(1001)
if student:
    print(f"พบข้อมูล: รหัส {student.key}, ชื่อ {student.name}")
else:
    print("ไม่พบนักศึกษา")

# แสดงรายชื่อนักศึกษาเรียงตามรหัส
print("\nรายชื่อนักศึกษาเรียงตามรหัส:")
bst.display_students()

# แสดงจำนวนนักศึกษาทั้งหมด
print("\nจำนวนนักศึกษาทั้งหมด:", bst.count_students())
