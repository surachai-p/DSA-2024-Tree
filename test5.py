import heapq
from collections import defaultdict


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # เพื่อให้ Node สามารถนำไปใส่ใน heapq ได้
    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self, text):
        self.text = text
        self.freq_dict = defaultdict(int)
        self.huffman_tree = None
        self.codes = {}
        self.reverse_codes = {}

    def build_frequency_dict(self):
        # สร้าง frequency dictionary สำหรับแต่ละตัวอักษร
        for char in self.text:
            self.freq_dict[char] += 1

    def build_huffman_tree(self):
        # สร้าง Huffman Tree จาก frequency dictionary
        priority_queue = [Node(char, freq) for char, freq in self.freq_dict.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            # ดึง 2 ตัวที่มีความถี่ต่ำสุดออกมา
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)

            # สร้าง node ใหม่ที่มีความถี่รวมกันของสองตัว
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            # ใส่ node ที่สร้างใหม่กลับเข้าไปใน heap
            heapq.heappush(priority_queue, merged)

        # ต้นไม้ Huffman ของเราคือ root ของ heap ที่เหลืออยู่ตัวเดียว
        self.huffman_tree = heapq.heappop(priority_queue)

    def build_codes(self, node=None, current_code=""):
        if node is None:
            node = self.huffman_tree

        # ถ้าเป็นใบ (leaf node) ให้บันทึก code ของตัวอักษร
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_codes[current_code] = node.char

        # ถ้าไม่ใช่ใบ (มีลูกซ้ายและขวา) ให้เดินต่อไป
        if node.left:
            self.build_codes(node.left, current_code + "0")
        if node.right:
            self.build_codes(node.right, current_code + "1")

    def encode(self):
        # เข้ารหัสข้อความโดยใช้ Huffman codes
        encoded_text = "".join(self.codes[char] for char in self.text)
        return encoded_text

    def calculate_compression_ratio(self, original_text, encoded_text):
        # คำนวณอัตราการบีบอัด
        original_size = len(original_text) * 8  # ขนาดเดิมในหน่วยบิต
        encoded_size = len(encoded_text)  # ขนาดที่บีบอัดในหน่วยบิต
        return (original_size - encoded_size) / original_size * 100


# รับข้อความจากผู้ใช้
text = input("กรุณากรอกข้อความภาษาไทย (ความยาวอย่างน้อย 100 ตัวอักษร): ")

# ตรวจสอบให้แน่ใจว่าข้อความยาวเกิน 100 ตัวอักษร
if len(text) < 100:
    print("ข้อความต้องมีความยาวไม่น้อยกว่า 100 ตัวอักษร")
else:
    # 1. สร้าง Huffman Coding object
    huffman = HuffmanCoding(text)

    # 2. สร้าง frequency dictionary
    huffman.build_frequency_dict()

    # 3. สร้าง Huffman Tree
    huffman.build_huffman_tree()

    # 4. สร้างรหัส Huffman
    huffman.build_codes()

    # 5. แสดงรหัส Huffman สำหรับแต่ละตัวอักษร
    print("\nรหัส Huffman สำหรับแต่ละตัวอักษร:")
    for char, code in huffman.codes.items():
        print(f"{char}: {code}")

    # 6. แสดงข้อความที่เข้ารหัสแล้ว
    encoded_text = huffman.encode()
    print("\nข้อความที่เข้ารหัสแล้ว:")
    print(encoded_text)

    # 7. คำนวณอัตราการบีบอัดข้อมูล
    compression_ratio = huffman.calculate_compression_ratio(text, encoded_text)
    print(f"\nอัตราการบีบอัดข้อมูล: {compression_ratio:.2f}%")
