import heapq
from collections import Counter, defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self, text):
        self.text = text
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    # 5.2 สร้าง Huffman Tree
    def build_huffman_tree(self):
        frequency = Counter(self.text)
        for char, freq in frequency.items():
            node = HuffmanNode(char, freq)
            heapq.heappush(self.heap, node)

        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

        return heapq.heappop(self.heap)

    def build_codes_helper(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.build_codes_helper(root.left, current_code + "0")
        self.build_codes_helper(root.right, current_code + "1")

    def build_codes(self):
        root = self.build_huffman_tree()
        self.build_codes_helper(root, "")

    # 5.3 แสดงรหัส Huffman สำหรับแต่ละตัวอักษร
    def get_huffman_codes(self):
        self.build_codes()
        return self.codes

    # 5.4 แสดงข้อความที่เข้ารหัสแล้ว
    def encode_text(self):
        encoded_text = ""
        for char in self.text:
            encoded_text += self.codes[char]
        return encoded_text

    # แปลงข้อความเข้ารหัสกลับเป็นข้อความเดิม
    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""

        return decoded_text

    # 5.5 แสดงอัตราการบีบอัดข้อมูล
    def calculate_compression_ratio(self, encoded_text):
        original_size = len(self.text) * 8  # ขนาดเดิมในบิต (1 ตัวอักษร = 8 บิต)
        compressed_size = len(encoded_text)  # ขนาดหลังบีบอัดในบิต
        return (original_size - compressed_size) / original_size * 100

# การใช้งาน
text = input("กรุณาป้อนข้อความภาษาไทยที่มีความยาวอย่างน้อย 100 ตัวอักษร: ")
while len(text) < 100:
    text = input("ข้อความสั้นเกินไป กรุณาป้อนข้อความที่มีความยาวอย่างน้อย 100 ตัวอักษร: ")

huffman = HuffmanCoding(text)

# สร้าง Huffman Tree และแสดงรหัส
codes = huffman.get_huffman_codes()
print("\nรหัส Huffman สำหรับแต่ละตัวอักษร:")
for char, code in codes.items():
    print(f"'{char}': {code}")

# เข้ารหัสข้อความ
encoded_text = huffman.encode_text()
print("\nข้อความที่เข้ารหัสแล้ว:")
print(encoded_text)

# แสดงอัตราการบีบอัด
compression_ratio = huffman.calculate_compression_ratio(encoded_text)
print(f"\nอัตราการบีบอัดข้อมูล: {compression_ratio:.2f}%")
