
class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None    
        self.right = None    

def tree_height(root):
   
    if root is None:
        return 0
 
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    
    return 1 + max(left_height, right_height)

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)

    height = tree_height(root)
    print("ความสูงของ Tree คือ:", height)
