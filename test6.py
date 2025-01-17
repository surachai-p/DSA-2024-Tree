class DictionaryNode:
    def __init__(self, word, meaning, part_of_speech, example_sentence):
        self.word = word  # คำศัพท์ภาษาอังกฤษ
        self.meaning = meaning  # ความหมายภาษาไทย
        self.part_of_speech = part_of_speech  # ชนิดของคำ (noun, verb, adjective, etc.)
        self.example_sentence = example_sentence  # ตัวอย่างประโยค
        self.left = None  # ลูกซ้าย
        self.right = None  # ลูกขวา


class Dictionary:
    def __init__(self):
        self.root = None  # รากของต้นไม้

    def insert(self, word, meaning, part_of_speech, example_sentence):
        """เพิ่มคำศัพท์และความหมายลงในต้นไม้"""
        new_node = DictionaryNode(word, meaning, part_of_speech, example_sentence)
        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, node, new_node):
        """ฟังก์ชันช่วยเหลือในการแทรกคำศัพท์ใหม่"""
        if new_node.word < node.word:
            if node.left is None:
                node.left = new_node
            else:
                self._insert(node.left, new_node)
        elif new_node.word > node.word:
            if node.right is None:
                node.right = new_node
            else:
                self._insert(node.right, new_node)

    def delete(self, word):
        """ลบคำศัพท์จากต้นไม้"""
        self.root = self._delete(self.root, word)

    def _delete(self, node, word):
        """ฟังก์ชันช่วยเหลือในการลบคำศัพท์"""
        if node is None:
            return node
        
        if word < node.word:
            node.left = self._delete(node.left, word)
        elif word > node.word:
            node.right = self._delete(node.right, word)
        else:
            # กรณีที่พบคำศัพท์ที่ต้องการลบ
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # กรณีที่มีลูกสองตัว
                min_larger_node = self._min_value_node(node.right)
                node.word = min_larger_node.word
                node.meaning = min_larger_node.meaning
                node.part_of_speech = min_larger_node.part_of_speech
                node.example_sentence = min_larger_node.example_sentence
                node.right = self._delete(node.right, min_larger_node.word)
        return node

    def _min_value_node(self, node):
        """หาค่าที่น้อยที่สุดในต้นไม้"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, word):
        """ค้นหาคำศัพท์ในต้นไม้"""
        return self._search(self.root, word)

    def _search(self, node, word):
        """ฟังก์ชันช่วยเหลือในการค้นหาคำศัพท์"""
        if node is None or node.word == word:
            return node
        if word < node.word:
            return self._search(node.left, word)
        return self._search(node.right, word)

    def display(self):
        """แสดงคำศัพท์ทั้งหมดในต้นไม้"""
        self._display(self.root)

    def _display(self, node):
        """ฟังก์ชันช่วยเหลือในการแสดงคำศัพท์"""
        if node:
            self._display(node.left)
            print(f"คำศัพท์: {node.word}")
            print(f"ความหมาย: {node.meaning}")
            print(f"ชนิดของคำ: {node.part_of_speech}")
            print(f"ตัวอย่างประโยค: {node.example_sentence}")
            print("-" * 50)
            self._display(node.right)


# ฟังก์ชันให้ผู้ใช้กรอกข้อมูลคำศัพท์
def add_word_to_dictionary(dictionary):
    print("\nกรุณากรอกข้อมูลคำศัพท์ใหม่:")
    word = input("คำศัพท์ (ภาษาอังกฤษ): ")
    meaning = input("ความหมาย (ภาษาไทย): ")
    part_of_speech = input("ชนิดของคำ (noun, verb, adjective, etc.): ")
    example_sentence = input("ตัวอย่างประโยค: ")

    # เพิ่มคำศัพท์ใหม่เข้าไปในพจนานุกรม
    dictionary.insert(word, meaning, part_of_speech, example_sentence)
    print(f"เพิ่มคำศัพท์ '{word}' ลงในพจนานุกรมแล้ว!")


# ตัวอย่างการใช้งาน
dictionary = Dictionary()

# ให้ผู้ใช้สามารถเพิ่มคำศัพท์เองได้
while True:
    add_word_to_dictionary(dictionary)

    continue_adding = input("\nต้องการเพิ่มคำศัพท์อีกหรือไม่? (y/n): ")
    if continue_adding.lower() != 'y':
        break

# 2) ค้นหาคำศัพท์
word_to_search = input("\nกรุณากรอกคำศัพท์ที่ต้องการค้นหา: ")
found_word = dictionary.search(word_to_search)
if found_word:
    print(f"พบคำศัพท์: {found_word.word}")
    print(f"ความหมาย: {found_word.meaning}")
    print(f"ชนิดของคำ: {found_word.part_of_speech}")
    print(f"ตัวอย่างประโยค: {found_word.example_sentence}")
else:
    print(f"ไม่พบคำศัพท์: {word_to_search}")

# 3) ลบคำศัพท์
word_to_delete = input("\nกรุณากรอกคำศัพท์ที่ต้องการลบ: ")
dictionary.delete(word_to_delete)

# แสดงผลคำศัพท์ทั้งหมดในต้นไม้หลังจากลบ
print("\nคำศัพท์ในพจนานุกรมหลังจากลบคำ:")
dictionary.display()
    