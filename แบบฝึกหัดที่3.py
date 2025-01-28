class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    
    return root

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

def main():
    root = None

    while True:
        print("\nตัวเลือก:")
        print("1. เพิ่มข้อมูล")
        print("2. ลบข้อมูล")
        print("3. แสดงข้อมูล (Inorder, Preorder, Postorder Traversal)")
        print("4. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1-4): ")

        if choice == "1":
            key = int(input("ป้อนค่าที่ต้องการเพิ่ม: "))
            root = insert(root, key)
            print(f"เพิ่มข้อมูล {key} สำเร็จ!")
        
        elif choice == "2":
            key = int(input("ป้อนค่าที่ต้องการลบ: "))
            root = delete(root, key)
            print(f"ลบข้อมูล {key} สำเร็จ!")
        
        elif choice == "3":
            print("Inorder Traversal:")
            inorder(root)
            print("\nPreorder Traversal:")
            preorder(root)
            print("\nPostorder Traversal:")
            postorder(root)
            print()
        
        elif choice == "4":
            print("ออกจากโปรแกรม")
            break
        
        else:
            print("กรุณาเลือกตัวเลือกที่ถูกต้อง (1-4)")

if __name__ == "__main__":
    main()