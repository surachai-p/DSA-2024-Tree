class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=" ")

# สร้าง BST และเพิ่มข้อมูล
tree = BST()
data = [5, 3, 7, 2, 4, 8]
for i in data:
    tree.insert(i)

# ค้นหาข้อมูล
print("ค้นหาข้อมูล 4:", tree.search(4))
print("ค้นหาข้อมูล 6:", tree.search(6))

# Traversal
print("\nInorder traversal:")
tree.inorder_traversal(tree.root)
print("\nPreorder traversal:")
tree.preorder_traversal(tree.root)
print("\nPostorder traversal:")
tree.postorder_traversal(tree.root)