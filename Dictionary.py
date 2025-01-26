class Node:
    def __init__(self, word, meaning, part_of_speech, example_sentence):
        self.word = word  # คำศัพท์ภาษาอังกฤษ
        self.meaning = meaning  # คำแปลภาษาไทย
        self.part_of_speech = part_of_speech  # ชนิดของคำ (noun, verb, adjective)
        self.example_sentence = example_sentence  # ตัวอย่างประโยค
        self.left = None
        self.right = None

class Dictionary:
    def __init__(self):
        self.root = None

    # ฟังก์ชันเพิ่มคำศัพท์และความหมาย
    def insert(self, word, meaning, part_of_speech, example_sentence):
        if self.root is None:
            self.root = Node(word, meaning, part_of_speech, example_sentence)
        else:
            self._insert(self.root, word, meaning, part_of_speech, example_sentence)

    def _insert(self, node, word, meaning, part_of_speech, example_sentence):
        if word < node.word:
            if node.left is None:
                node.left = Node(word, meaning, part_of_speech, example_sentence)
            else:
                self._insert(node.left, word, meaning, part_of_speech, example_sentence)
        elif word > node.word:
            if node.right is None:
                node.right = Node(word, meaning, part_of_speech, example_sentence)
            else:
                self._insert(node.right, word, meaning, part_of_speech, example_sentence)

    # ฟังก์ชันลบคำศัพท์
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
            else:
                min_node = self._find_min(node.right)
                node.word = min_node.word
                node.meaning = min_node.meaning
                node.part_of_speech = min_node.part_of_speech
                node.example_sentence = min_node.example_sentence
                node.right = self._delete(node.right, min_node.word)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # ฟังก์ชันค้นหาคำศัพท์
    def search(self, word):
        return self._search(self.root, word)

    def _search(self, node, word):
        if node is None:
            return None
        if word == node.word:
            return node
        elif word < node.word:
            return self._search(node.left, word)
        else:
            return self._search(node.right, word)

    # ฟังก์ชันแสดงข้อมูลทั้งหมด
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"คำศัพท์: {node.word}\nคำแปล: {node.meaning}\nชนิดของคำ: {node.part_of_speech}\nตัวอย่างประโยค: {node.example_sentence}\n")
            self._inorder(node.right)

# ฟังก์ชันให้ผู้ใช้กรอกข้อมูล
def add_word_to_dict(dictionary):
    word = input("กรุณากรอกคำศัพท์ภาษาอังกฤษ: ")
    meaning = input("กรุณากรอกคำแปลภาษาไทย: ")
    part_of_speech = input("กรุณากรอกชนิดของคำ (เช่น noun, verb, adjective): ")
    example_sentence = input("กรุณากรอกตัวอย่างประโยค: ")

    dictionary.insert(word, meaning, part_of_speech, example_sentence)
    print(f"คำศัพท์ '{word}' ถูกเพิ่มเข้าพจนานุกรมแล้ว!\n")

def search_word_in_dict(dictionary):
    word = input("กรุณากรอกคำศัพท์ที่ต้องการค้นหา: ")
    result = dictionary.search(word)
    if result:
        print(f"คำศัพท์: {result.word}\nคำแปล: {result.meaning}\nชนิดของคำ: {result.part_of_speech}\nตัวอย่างประโยค: {result.example_sentence}\n")
    else:
        print(f"ไม่พบคำศัพท์ '{word}' ในพจนานุกรม!\n")

def main():
    dictionary = Dictionary()

    while True:
        print("---- ระบบพจนานุกรม ----")
        print("1. เพิ่มคำศัพท์")
        print("2. ค้นหาคำศัพท์")
        print("3. แสดงพจนานุกรมทั้งหมด")
        print("4. ออกจากระบบ")
        
        choice = input("เลือกตัวเลือก (1-4): ")

        if choice == '1':
            add_word_to_dict(dictionary)
        elif choice == '2':
            search_word_in_dict(dictionary)
        elif choice == '3':
            print("รายการคำศัพท์ในพจนานุกรม:")
            dictionary.inorder()
        elif choice == '4':
            print("ขอบคุณที่ใช้ระบบพจนานุกรม!")
            break
        else:
            print("กรุณาเลือกตัวเลือกที่ถูกต้อง!")

if __name__ == "__main__":
    main()
