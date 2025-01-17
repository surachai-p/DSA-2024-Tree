class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)
    
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
    
    def inorder(self, node):
        """Traversal แบบ In-order (Left, Root, Right)"""
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)
    
    def preorder(self, node):
        """Traversal แบบ Pre-order (Root, Left, Right)"""
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        """Traversal แบบ Post-order (Left, Right, Root)"""
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

# สร้าง BST และเพิ่มข้อมูล
bst = BinarySearchTree()
data = [5, 3, 7, 2, 4, 8]
for value in data:
    bst.insert(value)

# ทดสอบการค้นหา
search_result_4 = bst.search(4)  # ค้นหาค่า 4
search_result_6 = bst.search(6)  # ค้นหาค่า 6

# ผลการค้นหาข้อมูล
print("ค้นหาค่า 4:", "พบ" if search_result_4 else "ไม่พบ")
print("ค้นหาค่า 6:", "พบ" if search_result_6 else "ไม่พบ")

# เปรียบเทียบการ Traversal ทั้ง 3 แบบ
print("\nIn-order Traversal:")
bst.inorder(bst.root)

print("\nPre-order Traversal:")
bst.preorder(bst.root)

print("\nPost-order Traversal:")
bst.postorder(bst.root)
