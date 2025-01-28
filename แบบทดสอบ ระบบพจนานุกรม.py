class Node:
    def __init__(self, word, meaning, word_type, example):
        self.word = word  # คำศัพท์ภาษาอังกฤษ
        self.meaning = meaning  # คำแปลภาษาไทย
        self.word_type = word_type  # ชนิดของคำ (noun, verb, adjective, etc.)
        self.example = example  # ตัวอย่างประโยค
        self.left = None  # โหนดลูกทางซ้าย
        self.right = None  # โหนดลูกทางขวา

class DictionaryBST:
    def __init__(self):
        self.root = None  # ต้นไม้เริ่มต้น

    def insert(self, word, meaning, word_type, example):
        self.root = self._insert(self.root, word, meaning, word_type, example)

    def _insert(self, node, word, meaning, word_type, example):
        if node is None:
            return Node(word, meaning, word_type, example)
        if word < node.word:
            node.left = self._insert(node.left, word, meaning, word_type, example)
        elif word > node.word:
            node.right = self._insert(node.right, word, meaning, word_type, example)
        return node

    def delete(self, word):
        self.root = self._delete(self.root, word)

    def _delete(self, node, word):
        if node is None:
            return node
        if word < node.word:
            node.left = self._delete(node.left, word)
        elif word > node.word:
            node.right = self._delete(node.right, word)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.word = temp.word
            node.meaning = temp.meaning
            node.word_type = temp.word_type
            node.example = temp.example
            node.right = self._delete(node.right, temp.word)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, word):
        return self._search(self.root, word)

    def _search(self, node, word):
        if node is None or node.word == word:
            return node
        if word < node.word:
            return self._search(node.left, word)
        return self._search(node.right, word)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(f"คำศัพท์: {node.word}")
            print(f"คำแปล: {node.meaning}")
            print(f"ชนิดของคำ: {node.word_type}")
            print(f"ตัวอย่างประโยค: {node.example}")
            print("-------------------------")
            self._inorder(node.right)

    def count_words(self):
        return self._count_words(self.root)

    def _count_words(self, node):
        if node is None:
            return 0
        return 1 + self._count_words(node.left) + self._count_words(node.right)

def menu():
    bst = DictionaryBST()
    while True:
        print("\n--- เมนู ---")
        print("1. เพิ่มคำศัพท์และความหมาย")
        print("2. ค้นหาคำศัพท์")
        print("3. ลบคำศัพท์")
        print("4. แสดงคำศัพท์ทั้งหมด")
        print("5. แสดงจำนวนคำศัพท์ทั้งหมด")
        print("6. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1-6): ")

        if choice == '1':
            word = input("กรุณากรอกคำศัพท์ภาษาอังกฤษ: ")
            meaning = input("กรุณากรอกคำแปลภาษาไทย: ")
            word_type = input("กรุณากรอกชนิดของคำ (noun, verb, adjective, etc.): ")
            example = input("กรุณากรอกตัวอย่างประโยค: ")
            bst.insert(word, meaning, word_type, example)
            print("คำศัพท์ถูกเพิ่มเรียบร้อยแล้ว!")
        elif choice == '2':
            word = input("กรุณากรอกคำศัพท์ที่ต้องการค้นหา: ")
            result = bst.search(word)
            if result:
                print(f"คำศัพท์: {result.word}")
                print(f"คำแปล: {result.meaning}")
                print(f"ชนิดของคำ: {result.word_type}")
                print(f"ตัวอย่างประโยค: {result.example}")
            else:
                print("ไม่พบคำศัพท์ที่ต้องการค้นหา")
        elif choice == '3':
            word = input("กรุณากรอกคำศัพท์ที่ต้องการลบ: ")
            bst.delete(word)
            print("คำศัพท์ถูกลบเรียบร้อยแล้ว!")
        elif choice == '4':
            print("\nคำศัพท์ทั้งหมด:")
            bst.inorder()
        elif choice == '5':
            print("\nจำนวนคำศัพท์ทั้งหมด:", bst.count_words())
        elif choice == '6':
            print("ขอบคุณที่ใช้โปรแกรม!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง, กรุณาลองใหม่.")

# เรียกใช้เมนูเพื่อเริ่มโปรแกรม
menu()
