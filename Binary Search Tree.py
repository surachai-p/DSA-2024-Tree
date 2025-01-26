class Node:
    def __init__(self, key, name):
        self.key = key  # รหัสนักศึกษา
        self.name = name  # ชื่อ-นามสกุล
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ฟังก์ชันเพิ่มข้อมูลนักศึกษา
    def insert(self, key, name):
        if self.root is None:
            self.root = Node(key, name)
        else:
            self._insert(self.root, key, name)

    def _insert(self, node, key, name):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, name)
            else:
                self._insert(node.left, key, name)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, name)
            else:
                self._insert(node.right, key, name)
        # ถ้ารหัสซ้ำไม่ทำอะไร

    # ฟังก์ชันลบข้อมูลนักศึกษาตามรหัส
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # โหนดที่ต้องการลบ
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # โหนดที่มีลูกทั้งสอง
                min_node = self._find_min(node.right)
                node.key = min_node.key
                node.name = min_node.name
                node.right = self._delete(node.right, min_node.key)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # ฟังก์ชันค้นหาข้อมูลนักศึกษาตามรหัส
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # ฟังก์ชันแสดงรายชื่อนักศึกษาเรียงตามรหัส
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"รหัส: {node.key}, ชื่อ-นามสกุล: {node.name}")
            self._inorder(node.right)

    # ฟังก์ชันแสดงจำนวนนักศึกษาทั้งหมด
    def count_students(self):
        return self._count_students(self.root)

    def _count_students(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._count_students(node.left) + self._count_students(node.right)

# ทดสอบโปรแกรม
bst = BinarySearchTree()

# เพิ่มข้อมูลนักศึกษา
bst.insert(66030236, "ณัฏฐณิชชา")
bst.insert(66030238, "ณัฐนันท์")
bst.insert(66030243, "ธัญเทพ")
bst.insert(66030077, "ธีรพัฒน์")

# แสดงรายชื่อนักศึกษาเรียงตามรหัส
print("รายชื่อนักศึกษาเรียงตามรหัส:")
bst.inorder()

# ค้นหานักศึกษาตามรหัส
student = bst.search(1002)
if student:
    print("\nค้นพบข้อมูลนักศึกษาตามรหัส 66030238:", student.name)
else:
    print("\nไม่พบข้อมูลนักศึกษาตามรหัส 66030255")

# ลบข้อมูลนักศึกษาตามรหัส
bst.delete(66030077)
print("\nหลังจากลบข้อมูลรหัส 66030077:")

# แสดงรายชื่อนักศึกษาเรียงตามรหัสหลังลบ
bst.inorder()

# แสดงจำนวนนักศึกษาทั้งหมด
print("\nจำนวนรวมของนักศึกษาทั้งหมด:", bst.count_students())
