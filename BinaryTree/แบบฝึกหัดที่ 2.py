class StudentNode:
    def __init__(self, student_id, name):
        self.student_id = student_id  # รหัสนักศึกษา (key)
        self.name = name             # ชื่อ-นามสกุล
        self.left = None             # โหนดซ้าย
        self.right = None            # โหนดขวา
def insert(root, student_id, name):
    if root is None:
        return StudentNode(student_id, name)
    if student_id < root.student_id:
        root.left = insert(root.left, student_id, name)
    elif student_id > root.student_id:
        root.right = insert(root.right, student_id, name)
    return root
def delete(root, student_id):
    if root is None:
        return root
    if student_id < root.student_id:
        root.left = delete(root.left, student_id)
    elif student_id > root.student_id:
        root.right = delete(root.right, student_id)
    else:
        # โหนดที่ต้องการลบถูกพบแล้ว
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # โหนดที่มีลูกทั้งสองฝั่ง
        temp = find_min(root.right)
        root.student_id = temp.student_id
        root.name = temp.name
        root.right = delete(root.right, temp.student_id)
    return root
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
def search(root, student_id):
    if root is None or root.student_id == student_id:
        return root
    if student_id < root.student_id:
        return search(root.left, student_id)
    return search(root.right, student_id)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(f"รหัส: {root.student_id}, ชื่อ: {root.name}")
        inorder_traversal(root.right)
def count_students(root):
    if root is None:
        return 0
    return 1 + count_students(root.left) + count_students(root.right)
if __name__ == "__main__":
    root = None
    students = [
        (196, "Suwannarat Padkham"),
        (178, "Siriwan Putarasu"),
        (204, "Arkurapum Misa"),
        (158, "Rapeepun Thongchai"),
        (253, "Adil Binsaaud"),
    ]
    for student_id, name in students:
        root = insert(root, student_id, name)
    print("รายชื่อนักศึกษาเรียงตามรหัส:")
    inorder_traversal(root)
    print("\nค้นหานักศึกษาที่มีรหัส 196:")
    student = search(root, 196)
    if student:
        print(f"พบรหัส: {student.student_id}, ชื่อ: {student.name}")
    else:
        print("ไม่พบนักศึกษา")
    print("\nลบนักศึกษาที่มีรหัส 178")
    root = delete(root, 178)
    print("รายชื่อนักศึกษาเรียงตามรหัสหลังลบ:")
    inorder_traversal(root)
    print("\nจำนวนนักศึกษาทั้งหมด:", count_students(root))
