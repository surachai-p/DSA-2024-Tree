# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def inorder(node):
#     if node:
#         inorder(node.left)
#         print(node.data, end=' ')
#         inorder(node.right)
        
# def preorder(node):
#     if node:
#         print(node.data, end=' ')
#         preorder(node.left)
#         preorder(node.right)
        
# def postorder(node):
#     if node:
#         postorder(node.left)
#         postorder(node.right)
#         print(node.data, end=' ')
        
# def search(root, key):
#     # ถ้า root เป็น None หรือ ข้อมูลที่ root ตรงกับ key
#     if root is None or root.data == key:
#         return root
    
#     # ถ้า key น้อยกว่าข้อมูลที่ root ค้นหาใน left subtree
#     if root.data > key:
#         return search(root.left, key)
    
#     # ถ้า key มากกว่าข้อมูลที่ root ค้นหาใน right subtree
#     return search(root.right, key)

# def insert(root, key):
#     if root is None:
#         return Node(key)
    
#     if key < root.data:
#         root.left = insert(root.left, key)
#     elif key > root.data:
#         root.right = insert(root.right, key)
    
#     return root

# def find_min(node):
#     current = node
#     while current.left is not None:
#         current = current.left
#     return current

# def delete(root, key):
#     if root is None:
#         return root

#     # ค้นหา Node ที่ต้องการลบ
#     if key < root.data:
#         root.left = delete(root.left, key)
#     elif key > root.data:
#         root.right = delete(root.right, key)
#     else:
#         # กรณีที่ 1: Node ที่ต้องการลบไม่มีลูก หรือมีลูกแค่ 1 Node
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
        
#         # กรณีที่ 2: Node ที่ต้องการลบมีลูก 2 Node
#         # หาค่าน้อยที่สุดใน right subtree
#         temp = find_min(root.right)
#         # แทนที่ข้อมูลด้วยค่าน้อยที่สุดที่พบ
#         root.data = temp.data
#         # ลบ Node ที่นำมาแทนที่
#         root.right = delete(root.right, temp.data)
    
#     return root

# # ตัวอย่างการใช้งาน
# root = None
# keys = [5, 3, 7, 2, 4, 8]

# # เพิ่มข้อมูล
# for key in keys:
#     root = insert(root, key)

# search_result_4 = search(root, 4)
# search_result_6 = search(root, 6)

# print("ก่อนลบข้อมูล:")
# inorder(root)  # 2 3 4 5 7 8

# # ลบข้อมูล
# root = delete(root, 3)
# print("\nหลังลบข้อมูล 3:")
# inorder(root)  # 2 4 5 7 8

# print("ผลการค้นหา:")
# print("ค้นหา 4:", "พบ" if search_result_4 else "ไม่พบ")
# print("ค้นหา 6:", "พบ" if search_result_6 else "ไม่พบ")

# print("\nTraversal เปรียบเทียบ:")
# print("Inorder traversal: ", end="")
# inorder(root)
# print("\nPreorder traversal: ", end="")
# preorder(root)
# print("\nPostorder traversal: ", end="")
# postorder(root)
# print()

# class FileSystemNode:
#     def __init__(self, name, is_file=False):
#         self.name = name
#         self.is_file = is_file
#         self.children = []  # สำหรับโฟลเดอร์ย่อยหรือไฟล์
#         self.content = ""   # สำหรับไฟล์

#     def add_child(self, child):
#         self.children.append(child)

#     def display(self, level=0):
#         prefix = "  " * level
#         print(prefix + ("📄 " if self.is_file else "📁 ") + self.name)
#         for child in self.children:
#             child.display(level + 1)

# # ตัวอย่างการใช้งาน
# root = FileSystemNode("Documents")
# pictures = FileSystemNode("Pictures")
# vacation = FileSystemNode("Vacation")
# photo1 = FileSystemNode("photo1.jpg", True)
# photo2 = FileSystemNode("photo2.jpg", True)

# root.add_child(pictures)
# pictures.add_child(vacation)
# vacation.add_child(photo1)
# vacation.add_child(photo2)

# root.display()


# class Node:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         self.left = None
#         self.right = None

# def display_organization(root, level=0):
#     if root is None:
#         return
    
#     prefix = "  " * level
#     print(f"{prefix}👤 {root.name} ({root.position})")
    
#     if root.left:
#         display_organization(root.left, level + 1)
#     if root.right:
#         display_organization(root.right, level + 1)

# # สร้างโครงสร้างองค์กร
# def create_organization():
#     # สร้าง CEO
#     ceo = Node("สมชาย", "CEO")
    
#     # สร้าง CTO และ CFO
#     cto = Node("สมหญิง", "CTO")
#     cfo = Node("สมศรี", "CFO")
    
#     # สร้าง Development Manager และ System Manager
#     dev_manager = Node("สมศักดิ์", "Development Manager")
#     sys_manager = Node("สมชัย", "System Manager")
    
#     # สร้าง Developer
#     dev1 = Node("สมใจ", "Developer")
#     dev2 = Node("สมปอง", "Developer")
    
#     # เชื่อมความสัมพันธ์
#     ceo.left = cto
#     ceo.right = cfo
    
#     cto.left = dev_manager
#     cto.right = sys_manager
    
#     dev_manager.left = dev1
#     dev_manager.right = dev2
    
#     return ceo

# # ตัวอย่างการใช้งาน
# root = create_organization()
# print("โครงสร้างองค์กร:")
# display_organization(root)


# import heapq
# from collections import Counter

# class HuffmanNode:
#     def __init__(self, char, freq):
#         self.char = char
#         self.freq = freq
#         self.left = None
#         self.right = None
    
#     def __lt__(self, other):
#         return self.freq < other.freq

# def build_huffman_tree(text):
#     # นับความถี่ของแต่ละตัวอักษร
#     frequency = Counter(text)
    
#     # สร้าง priority queue
#     priority_queue = []
#     for char, freq in frequency.items():
#         node = HuffmanNode(char, freq)
#         heapq.heappush(priority_queue, (freq, node))
    
#     # สร้าง Huffman Tree
#     while len(priority_queue) > 1:
#         freq1, left = heapq.heappop(priority_queue)
#         freq2, right = heapq.heappop(priority_queue)
        
#         # สร้าง internal node
#         internal = HuffmanNode(None, freq1 + freq2)
#         internal.left = left
#         internal.right = right
        
#         heapq.heappush(priority_queue, (freq1 + freq2, internal))
    
#     return priority_queue[0][1]

# def get_huffman_codes(root, code="", codes=None):
#     if codes is None:
#         codes = {}
    
#     if root is not None:
#         if root.char is not None:  # ถ้าเป็น leaf node
#             codes[root.char] = code
#         else:  # ถ้าเป็น internal node
#             get_huffman_codes(root.left, code + "0", codes)
#             get_huffman_codes(root.right, code + "1", codes)
    
#     return codes

# def encode_text(text, codes):
#     return "".join(codes[char] for char in text)

# def decode_text(encoded_text, root):
#     decoded_text = ""
#     current = root
    
#     for bit in encoded_text:
#         if bit == "0":
#             current = current.left
#         else:
#             current = current.right
            
#         if current.char is not None:  # ถ้าเจอ leaf node
#             decoded_text += current.char
#             current = root
    
#     return decoded_text

# # ตัวอย่างการใช้งาน
# text = "สวัสดีครับ เรียนวิชา Data Structure"
# print(f"\nข้อความต้นฉบับ: {text}")
# print(f"ขนาดต้นฉบับ: {len(text.encode('utf-8'))} bytes")

# # สร้าง Huffman Tree
# huffman_tree = build_huffman_tree(text)

# # สร้างรหัส Huffman
# huffman_codes = get_huffman_codes(huffman_tree)
# print("\nรหัส Huffman สำหรับแต่ละตัวอักษร:")
# for char, code in huffman_codes.items():
#     print(f"'{char}': {code}")

# # เข้ารหัสข้อความ
# encoded_text = encode_text(text, huffman_codes)
# print(f"\nข้อความที่เข้ารหัสแล้ว: {encoded_text}")
# print(f"ขนาดหลังเข้ารหัส: {len(encoded_text) // 8} bytes")

# # ถอดรหัสข้อความ
# decoded_text = decode_text(encoded_text, huffman_tree)
# print(f"\nข้อความที่ถอดรหัสแล้ว: {decoded_text}")

# # คำนวณอัตราการบีบอัด
# compression_ratio = (1 - len(encoded_text) / (len(text.encode('utf-8')) * 8)) * 100
# print(f"\nอัตราการบีบอัด: {compression_ratio:.2f}%")

# class ExprNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def evaluate(root):
#     if root is None:
#         return 0
    
#     # ถ้าเป็นตัวเลข
#     if not isinstance(root.value, str):
#         return root.value
    
#     # ประมวลผลตามเครื่องหมาย
#     left_val = evaluate(root.left)
#     right_val = evaluate(root.right)
    
#     if root.value == '+':
#         return left_val + right_val
#     elif root.value == '-':
#         return left_val - right_val
#     elif root.value == '*':
#         return left_val * right_val
#     elif root.value == '/':
#         return left_val / right_val

# # ตัวอย่างการใช้งาน: สร้าง Expression Tree สำหรับ (5 + 3) * 2
# root = ExprNode('*')
# root.left = ExprNode('+')
# root.left.left = ExprNode(5)
# root.left.right = ExprNode(3)
# root.right = ExprNode(2)

# result = evaluate(root)
# print(f"ผลลัพธ์: {result}")  # ผลลัพธ์: 16


class DecisionNode:
    def __init__(self, question, yes_action, no_action):
        self.question = question
        self.yes = yes_action
        self.no = no_action

    def decide(self):
        answer = input(f"{self.question} (y/n): ").lower()
        if answer == 'y':
            # Recursively call decide() if yes is a DecisionNode
            if isinstance(self.yes, DecisionNode):
                return self.yes.decide()
            else:
                return self.yes() if callable(self.yes) else self.yes
        else:
            # Recursively call decide() if no is a DecisionNode
            if isinstance(self.no, DecisionNode):
                return self.no.decide()
            else:
                return self.no() if callable(self.no) else self.no

# ตัวอย่างการใช้งาน: ระบบแนะนำการแต่งกาย
def create_clothing_advisor():
    casual = "สวมเสื้อยืดกับกางเกงยีนส์"
    formal = "สวมสูททางการ"
    smart_casual = "สวมเสื้อโปโลกับกางเกงสแล็ค"
    
    going_to_work = DecisionNode(
        "คุณกำลังจะไปทำงานหรือไม่?",
        DecisionNode(
            "เป็นการประชุมสำคัญหรือไม่?",
            formal,
            smart_casual
        ),
        casual
    )
    
    return going_to_work

advisor = create_clothing_advisor()
recommendation = advisor.decide()
print(f"คำแนะนำการแต่งกาย: {recommendation}")