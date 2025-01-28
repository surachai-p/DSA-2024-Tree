class StudentNode:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.left = None
        self.right = None

def insert_student(root, student_id, name):
    if root is None:
        return StudentNode(student_id, name)
    
    if student_id < root.student_id:
        root.left = insert_student(root.left, student_id, name)
    elif student_id > root.student_id:
        root.right = insert_student(root.right, student_id, name)
    
    return root

def search_student(root, student_id):
    if root is None or root.student_id == student_id:
        return root
    
    if student_id < root.student_id:
        return search_student(root.left, student_id)
    return search_student(root.right, student_id)

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_student(root, student_id):
    if root is None:
        return root

    if student_id < root.student_id:
        root.left = delete_student(root.left, student_id)
    elif student_id > root.student_id:
        root.right = delete_student(root.right, student_id)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        temp = find_min(root.right)
        root.student_id = temp.student_id
        root.name = temp.name
        root.right = delete_student(root.right, temp.student_id)
    
    return root

def display_students_in_order(root):
    if root is not None:
        display_students_in_order(root.left)
        print(f"ID: {root.student_id}, Name: {root.name}")
        display_students_in_order(root.right)

def count_students(root):
    if root is None:
        return 0
    return 1 + count_students(root.left) + count_students(root.right)

def menu():
    print("\n---- เมนู ----")
    print("1. เพิ่มข้อมูลนักศึกษา")
    print("2. ลบข้อมูลนักศึกษา")
    print("3. ค้นหาข้อมูลนักศึกษา")
    print("4. แสดงรายชื่อนักศึกษาเรียงตามรหัส")
    print("5. แสดงจำนวนนักศึกษาทั้งหมด")
    print("6. ออกจากโปรแกรม")

def main():
    root = None
    while True:
        menu()
        choice = input("กรุณาเลือกคำสั่ง (1-6): ")
        
        if choice == "1":
            student_id = int(input("กรุณาป้อนรหัสนักศึกษา: "))
            name = input("กรุณาป้อนชื่อ-นามสกุลนักศึกษา: ")
            root = insert_student(root, student_id, name)
            print("เพิ่มข้อมูลสำเร็จ!")

        elif choice == "2":
            student_id = int(input("กรุณาป้อนรหัสนักศึกษาที่ต้องการลบ: "))
            root = delete_student(root, student_id)
            print("ลบข้อมูลสำเร็จ!")

        elif choice == "3":
            student_id = int(input("กรุณาป้อนรหัสนักศึกษาที่ต้องการค้นหา: "))
            student = search_student(root, student_id)
            if student:
                print(f"พบ: ID: {student.student_id}, Name: {student.name}")
            else:
                print("ไม่พบข้อมูลนักศึกษา")

        elif choice == "4":
            print("\nรายชื่อนักศึกษาเรียงตามรหัส:")
            display_students_in_order(root)

        elif choice == "5":
            total_students = count_students(root)
            print(f"\nจำนวนนักศึกษาทั้งหมด: {total_students}")

        elif choice == "6":
            print("ออกจากโปรแกรม")
            break

        else:
            print("กรุณาเลือกคำสั่งที่ถูกต้อง (1-6)")

if __name__ == "__main__":
    main()