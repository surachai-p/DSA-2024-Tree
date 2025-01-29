# ใบงานการทดลอง: การสร้างและจัดการโครงสร้างข้อมูล Tree ด้วย Python

## วัตถุประสงค์
1. เพื่อให้นักศึกษาเข้าใจหลักการทำงานของโครงสร้างข้อมูลแบบ Tree
2. เพื่อให้นักศึกษาสามารถเขียนโปรแกรมสร้างและจัดการ Binary Tree ด้วยภาษา Python ได้
3. เพื่อให้นักศึกษาสามารถประยุกต์ใช้ Binary Tree ในการแก้ปัญหาต่างๆ ได้

## อุปกรณ์ที่ใช้
1. เครื่องคอมพิวเตอร์
2. Python Interpreter (เวอร์ชัน 3.6 ขึ้นไป)
3. Text Editor หรือ IDE ตามที่ถนัด

## ทฤษฎีที่เกี่ยวข้อง
Tree เป็นโครงสร้างข้อมูลแบบไม่เชิงเส้น (Non-linear) ที่ประกอบด้วย Node ต่างๆ เชื่อมต่อกันในลักษณะความสัมพันธ์แบบพ่อ-ลูก โดย:
- แต่ละ Node เก็บข้อมูลและ Reference ไปยัง Node ลูก
- Node บนสุดเรียกว่า Root Node
- Node ที่ไม่มีลูกเรียกว่า Leaf Node
- Binary Tree คือ Tree ที่แต่ละ Node มีลูกได้ไม่เกิน 2 Node (ซ้ายและขวา)

## การทดลอง

### ส่วนที่ 1: การสร้าง Binary Tree Node

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

แบบฝึกหัดที่ 1: จงสร้าง Binary Tree ต่อไปนี้
```
       5
      / \
     3   7
    / \   \
   2   4   8
```

คำตอบ:
```python
# สร้าง root node
root = Node(5)

# สร้าง left subtree
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)

# สร้าง right subtree
root.right = Node(7)
root.right.right = Node(8)
```

### ส่วนที่ 2: การท่องไป (Traversal) บน Binary Tree

จงเขียนฟังก์ชันสำหรับการท่องไปบน Binary Tree ทั้ง 3 แบบ:

1. Inorder Traversal (Left-Root-Right)
```python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)
```

2. Preorder Traversal (Root-Left-Right)
```python
def preorder(node):
    if node:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)
```

3. Postorder Traversal (Left-Right-Root)
```python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')
```

แบบฝึกหัดที่ 2: จงเขียนผลลัพธ์ที่ได้จากการ Traversal ทั้ง 3 แบบ สำหรับ Tree ที่สร้างในแบบฝึกหัดที่ 1

คำตอบ:
```
Inorder: 2 3 4 5 7 8
Preorder: 5 3 2 4 7 8
Postorder: 2 4 3 8 7 5
```

### ส่วนที่ 3: การค้นหาข้อมูลใน Binary Search Tree

Binary Search Tree (BST) เป็น Binary Tree ที่มีคุณสมบัติพิเศษคือ:
- ข้อมูลใน Node ซ้ายทั้งหมดต้องน้อยกว่าข้อมูลใน Node ปัจจุบัน
- ข้อมูลใน Node ขวาทั้งหมดต้องมากกว่าข้อมูลใน Node ปัจจุบัน

จงเขียนฟังก์ชันค้นหาข้อมูลใน BST:
```python
def search(root, key):
    # ถ้า root เป็น None หรือ ข้อมูลที่ root ตรงกับ key
    if root is None or root.data == key:
        return root
    
    # ถ้า key น้อยกว่าข้อมูลที่ root ค้นหาใน left subtree
    if root.data > key:
        return search(root.left, key)
    
    # ถ้า key มากกว่าข้อมูลที่ root ค้นหาใน right subtree
    return search(root.right, key)
```

แบบฝึกหัดที่ 3: จงเขียนฟังก์ชันเพิ่มและลบข้อมูลใน BST

คำตอบ:
```python
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

    # ค้นหา Node ที่ต้องการลบ
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # กรณีที่ 1: Node ที่ต้องการลบไม่มีลูก หรือมีลูกแค่ 1 Node
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # กรณีที่ 2: Node ที่ต้องการลบมีลูก 2 Node
        # หาค่าน้อยที่สุดใน right subtree
        temp = find_min(root.right)
        # แทนที่ข้อมูลด้วยค่าน้อยที่สุดที่พบ
        root.data = temp.data
        # ลบ Node ที่นำมาแทนที่
        root.right = delete(root.right, temp.data)
    
    return root

# ตัวอย่างการใช้งาน
root = None
keys = [5, 3, 7, 2, 4, 8]

# เพิ่มข้อมูล
for key in keys:
    root = insert(root, key)

print("ก่อนลบข้อมูล:")
inorder(root)  # 2 3 4 5 7 8

# ลบข้อมูล
root = delete(root, 3)
print("\nหลังลบข้อมูล 3:")
inorder(root)  # 2 4 5 7 8
```

## การทดสอบและการวิเคราะห์

1. จงสร้าง BST จากข้อมูลต่อไปนี้: 5, 3, 7, 2, 4, 8
2. ทดสอบการค้นหาข้อมูล 4 และ 6
3. เปรียบเทียบผลการ Traversal ทั้ง 3 แบบ

## คำถามท้ายการทดลอง

1. เพราะเหตุใด Binary Search Tree จึงมีประสิทธิภาพในการค้นหาข้อมูลมากกว่า Linear Search?
2. ในกรณีใดบ้างที่ BST จะมีประสิทธิภาพในการค้นหาเทียบเท่ากับ Linear Search?
3. จงอธิบายความแตกต่างระหว่าง Binary Tree และ Binary Search Tree
4. การ Traversal แบบใดที่จะแสดงผลข้อมูลเรียงลำดับจากน้อยไปมากเมื่อใช้กับ BST?
### ตอบ 
1. BST ค้นหาเร็วกว่า Linear Search เพราะใช้ Binary Search
2. BST อาจช้าเท่ากับ Linear Search หากต้นไม้เป็นเส้นตรง
3. Binary Tree เป็นต้นไม้ทั่วไป ส่วน BST มีการเรียงลำดับของข้อมูล
4. Inorder Traversal ใช้เพื่อแสดงข้อมูล BST เรียงจากน้อยไปมาก 

## แบบฝึกหัดเพิ่มเติม

### แบบฝึกหัดที่ 1: การสร้างและจัดการ Binary Tree
จงเขียนโปรแกรมสร้าง Binary Tree ที่มีโครงสร้างดังนี้ และเพิ่มฟังก์ชัน:
```
        10
       /  \
      5    15
     / \   / \
    3   7 12  18
```

1.1) เขียนฟังก์ชันนับจำนวน Node ทั้งหมดใน Tree
1.2) เขียนฟังก์ชันนับจำนวน Leaf Node
1.3) เขียนฟังก์ชันหาความสูงของ Tree
1.4) เขียนฟังก์ชันหาผลรวมของค่าใน Tree

### แบบฝึกหัดที่ 2: Binary Search Tree
จงเขียนโปรแกรมที่รับข้อมูลนักศึกษาประกอบด้วย รหัสนักศึกษา(key) และ ชื่อ-นามสกุล แล้วเก็บในรูปแบบ Binary Search Tree พร้อมทั้งสร้างฟังก์ชันต่อไปนี้:

2.1) เพิ่มข้อมูลนักศึกษา
2.2) ลบข้อมูลนักศึกษาตามรหัส
2.3) ค้นหาข้อมูลนักศึกษาตามรหัส
2.4) แสดงรายชื่อนักศึกษาเรียงตามรหัส
2.5) แสดงจำนวนนักศึกษาทั้งหมด

## ส่วนที่ 4: ตัวอย่างการประยุกต์ใช้งานจริง

### 1. ระบบจัดการไฟล์และโฟลเดอร์

```python
class FileSystemNode:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []  # สำหรับโฟลเดอร์ย่อยหรือไฟล์
        self.content = ""   # สำหรับไฟล์

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        prefix = "  " * level
        print(prefix + ("📄 " if self.is_file else "📁 ") + self.name)
        for child in self.children:
            child.display(level + 1)

# ตัวอย่างการใช้งาน
root = FileSystemNode("Documents")
pictures = FileSystemNode("Pictures")
vacation = FileSystemNode("Vacation")
photo1 = FileSystemNode("photo1.jpg", True)
photo2 = FileSystemNode("photo2.jpg", True)

root.add_child(pictures)
pictures.add_child(vacation)
vacation.add_child(photo1)
vacation.add_child(photo2)

root.display()
```

### 2. ระบบแสดงโครงสร้างองค์กร

```python
class Node:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.left = None
        self.right = None

def display_organization(root, level=0):
    if root is None:
        return
    
    prefix = "  " * level
    print(f"{prefix}👤 {root.name} ({root.position})")
    
    if root.left:
        display_organization(root.left, level + 1)
    if root.right:
        display_organization(root.right, level + 1)

# สร้างโครงสร้างองค์กร
def create_organization():
    # สร้าง CEO
    ceo = Node("สมชาย", "CEO")
    
    # สร้าง CTO และ CFO
    cto = Node("สมหญิง", "CTO")
    cfo = Node("สมศรี", "CFO")
    
    # สร้าง Development Manager และ System Manager
    dev_manager = Node("สมศักดิ์", "Development Manager")
    sys_manager = Node("สมชัย", "System Manager")
    
    # สร้าง Developer
    dev1 = Node("สมใจ", "Developer")
    dev2 = Node("สมปอง", "Developer")
    
    # เชื่อมความสัมพันธ์
    ceo.left = cto
    ceo.right = cfo
    
    cto.left = dev_manager
    cto.right = sys_manager
    
    dev_manager.left = dev1
    dev_manager.right = dev2
    
    return ceo

# ตัวอย่างการใช้งาน
root = create_organization()
print("โครงสร้างองค์กร:")
display_organization(root)
```

### 3. การบีบอัดข้อมูลด้วย Huffman Code

```python
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # นับความถี่ของแต่ละตัวอักษร
    frequency = Counter(text)
    
    # สร้าง priority queue
    priority_queue = []
    for char, freq in frequency.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(priority_queue, (freq, node))
    
    # สร้าง Huffman Tree
    while len(priority_queue) > 1:
        freq1, left = heapq.heappop(priority_queue)
        freq2, right = heapq.heappop(priority_queue)
        
        # สร้าง internal node
        internal = HuffmanNode(None, freq1 + freq2)
        internal.left = left
        internal.right = right
        
        heapq.heappush(priority_queue, (freq1 + freq2, internal))
    
    return priority_queue[0][1]

def get_huffman_codes(root, code="", codes=None):
    if codes is None:
        codes = {}
    
    if root is not None:
        if root.char is not None:  # ถ้าเป็น leaf node
            codes[root.char] = code
        else:  # ถ้าเป็น internal node
            get_huffman_codes(root.left, code + "0", codes)
            get_huffman_codes(root.right, code + "1", codes)
    
    return codes

def encode_text(text, codes):
    return "".join(codes[char] for char in text)

def decode_text(encoded_text, root):
    decoded_text = ""
    current = root
    
    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right
            
        if current.char is not None:  # ถ้าเจอ leaf node
            decoded_text += current.char
            current = root
    
    return decoded_text

# ตัวอย่างการใช้งาน
text = "สวัสดีครับ เรียนวิชา Data Structure"
print(f"\nข้อความต้นฉบับ: {text}")
print(f"ขนาดต้นฉบับ: {len(text.encode('utf-8'))} bytes")

# สร้าง Huffman Tree
huffman_tree = build_huffman_tree(text)

# สร้างรหัส Huffman
huffman_codes = get_huffman_codes(huffman_tree)
print("\nรหัส Huffman สำหรับแต่ละตัวอักษร:")
for char, code in huffman_codes.items():
    print(f"'{char}': {code}")

# เข้ารหัสข้อความ
encoded_text = encode_text(text, huffman_codes)
print(f"\nข้อความที่เข้ารหัสแล้ว: {encoded_text}")
print(f"ขนาดหลังเข้ารหัส: {len(encoded_text) // 8} bytes")

# ถอดรหัสข้อความ
decoded_text = decode_text(encoded_text, huffman_tree)
print(f"\nข้อความที่ถอดรหัสแล้ว: {decoded_text}")

# คำนวณอัตราการบีบอัด
compression_ratio = (1 - len(encoded_text) / (len(text.encode('utf-8')) * 8)) * 100
print(f"\nอัตราการบีบอัด: {compression_ratio:.2f}%")
```

### 4. ระบบประมวลผลนิพจน์ทางคณิตศาสตร์ (Expression Tree)

```python
class ExprNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate(root):
    if root is None:
        return 0
    
    # ถ้าเป็นตัวเลข
    if not isinstance(root.value, str):
        return root.value
    
    # ประมวลผลตามเครื่องหมาย
    left_val = evaluate(root.left)
    right_val = evaluate(root.right)
    
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val / right_val

# ตัวอย่างการใช้งาน: สร้าง Expression Tree สำหรับ (5 + 3) * 2
root = ExprNode('*')
root.left = ExprNode('+')
root.left.left = ExprNode(5)
root.left.right = ExprNode(3)
root.right = ExprNode(2)

result = evaluate(root)
print(f"ผลลัพธ์: {result}")  # ผลลัพธ์: 16
```

### 5. ระบบตัดสินใจอัตโนมัติ (Decision Tree)

```python
class DecisionNode:
    def __init__(self, question, yes_action, no_action):
        self.question = question
        self.yes = yes_action
        self.no = no_action

    def decide(self):
        answer = input(f"{self.question} (y/n): ").lower()
        if answer == 'y':
            return self.yes() if callable(self.yes) else self.yes
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
```

### แบบทดสอบ: ระบบพจนานุกรม
จงพัฒนาระบบพจนานุกรมอย่างง่ายโดยใช้ Binary Tree ที่มีความสามารถดังนี้:

1) เพิ่มคำศัพท์และความหมาย
2) ลบคำศัพท์
3) ค้นหาคำศัพท์

โดยในแต่ละคำศัพท์ประกอบด้วย:
- คำศัพท์ภาษาอังกฤษ
- คำแปลภาษาไทย
- ชนิดของคำ (noun, verb, adjective, etc.)
- ตัวอย่างประโยค

