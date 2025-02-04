class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)


def find_height(node):
    if node is None:
        return 0
    left_height = find_height(node.left)
    right_height = find_height(node.right)
    return max(left_height, right_height) + 1


def sum_tree(node):
    if node is None:
        return 0
    return node.data + sum_tree(node.left) + sum_tree(node.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

print("จำนวน Node ทั้งหมด:", count_nodes(root))
print("จำนวน Leaf Node:", count_leaf_nodes(root))
print("ความสูงของ Tree:", find_height(root))
print("ผลรวมของค่าใน Tree:", sum_tree(root))