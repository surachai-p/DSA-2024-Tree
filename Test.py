class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)

# สร้าง BST
bst = BST()
data = [5, 3, 7, 2, 4, 8]
for num in data:
    bst.insert(num)

# ทดสอบการค้นหา
search_values = [4, 6]
for value in search_values:
    found = bst.search(value)
    print(f"search {value}: {'found' if found else 'not fount'}")

# ทดสอบการ Traversal
inorder_result = []
preorder_result = []
postorder_result = []

bst.inorder_traversal(bst.root, inorder_result)
bst.preorder_traversal(bst.root, preorder_result)
bst.postorder_traversal(bst.root, postorder_result)

print("Inorder Traversal:", inorder_result)
print("Preorder Traversal:", preorder_result)
print("Postorder Traversal:", postorder_result)
