class StudentNode:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.left = None
        self.right = None

class StudentBST:
    def __init__(self):
        self.root = None

    def insert(self, student_id, name):
        self.root = self._insert(self.root, student_id, name)
    
    def _insert(self, node, student_id, name):
        if node is None:
            return StudentNode(student_id, name)
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
            node.student_id, node.name = temp.student_id, temp.name
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

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.student_id, node.name))
            self._inorder(node.right, result)

    def count_students(self):
        return self._count_nodes(self.root)
    
    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

# ทดสอบโปรแกรม
bst = StudentBST()
bst.insert(1001, "Alice Brown")
bst.insert(1005, "Charlie Davis")
bst.insert(1003, "Bob Smith")

print("รายชื่อนักศึกษาเรียงตามรหัส:", bst.inorder_traversal())
print("จำนวนนักศึกษาทั้งหมด:", bst.count_students())

bst.delete(1003)
print("รายชื่อนักศึกษาหลังจากลบ:", bst.inorder_traversal())
