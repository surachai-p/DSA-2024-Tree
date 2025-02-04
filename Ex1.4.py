
class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None   
        self.right = None  

def sum_tree(root):
    if root is None:
        return 0
    
    return root.value + sum_tree(root.left) + sum_tree(root.right)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)

    total = sum_tree(root)
    print("ผลรวมของค่าใน Tree คือ:", total)
