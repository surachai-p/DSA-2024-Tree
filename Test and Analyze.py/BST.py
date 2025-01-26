class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None:
            return None
        if node.value == key:
            return node
        elif key < node.value:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)


# สร้าง BST และเพิ่มค่าต่าง ๆ
bst = BST()
values = [5, 3, 7, 2, 4, 8]

for value in values:
    bst.insert(value)

# ทดสอบการค้นหาข้อมูล 4 และ 6
search_values = [4, 6]
for value in search_values:
    result = bst.search(value)
    if result:
        print(f"พบข้อมูล {value} ใน BST")
    else:
        print(f"ไม่พบข้อมูล {value} ใน BST")

# แสดงผลการ Traversal ทั้ง 3 แบบ
print("\nInorder Traversal:")
bst.inorder(bst.root)

print("\nPreorder Traversal:")
bst.preorder(bst.root)

print("\nPostorder Traversal:")
bst.postorder(bst.root)
