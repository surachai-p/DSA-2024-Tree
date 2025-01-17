class DictionaryEntry:
    def __init__(self, word, meaning, word_type, example_sentence):
        self.word = word  # คำศัพท์
        self.meaning = meaning  # คำแปล
        self.word_type = word_type  # ชนิดของคำ (เช่น noun, verb, adjective)
        self.example_sentence = example_sentence  # ตัวอย่างประโยค
        self.left = None  # ลูกซ้าย
        self.right = None  # ลูกขวา

class Dictionary:
    def __init__(self):
        self.root = None

    def insert(self, word, meaning, word_type, example_sentence):
        """เพิ่มคำศัพท์และความหมายลงในพจนานุกรม"""
        new_entry = DictionaryEntry(word, meaning, word_type, example_sentence)
        if self.root is None:
            self.root = new_entry
        else:
            self._insert_recursive(self.root, new_entry)

    def _insert_recursive(self, node, new_entry):
        """ช่วยเพิ่มคำศัพท์ใน BST"""
        if new_entry.word < node.word:
            if node.left is None:
                node.left = new_entry
            else:
                self._insert_recursive(node.left, new_entry)
        elif new_entry.word > node.word:
            if node.right is None:
                node.right = new_entry
            else:
                self._insert_recursive(node.right, new_entry)

    def delete(self, word):
        """ลบคำศัพท์จากพจนานุกรม"""
        self.root = self._delete_recursive(self.root, word)

    def _delete_recursive(self, node, word):
        """ช่วยลบคำศัพท์ใน BST"""
        if node is None:
            return node
        if word < node.word:
            node.left = self._delete_recursive(node.left, word)
        elif word > node.word:
            node.right = self._delete_recursive(node.right, word)
        else:
            # ถ้าพบคำศัพท์แล้ว
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # ถ้ามีลูกทั้งสองข้าง
            min_larger_node = self._get_min(node.right)
            node.word, node.meaning, node.word_type, node.example_sentence = min_larger_node.word, min_larger_node.meaning, min_larger_node.word_type, min_larger_node.example_sentence
            node.right = self._delete_recursive(node.right, min_larger_node.word)
        return node

    def _get_min(self, node):
        """หาคำศัพท์ที่มีค่าน้อยที่สุดใน BST"""
        while node.left is not None:
            node = node.left
        return node

    def search(self, word):
        """ค้นหาคำศัพท์ในพจนานุกรม"""
        return self._search_recursive(self.root, word)

    def _search_recursive(self, node, word):
        """ช่วยค้นหาคำศัพท์ใน BST"""
        if node is None:
            return None
        if word == node.word:
            return node
        elif word < node.word:
            return self._search_recursive(node.left, word)
        else:
            return self._search_recursive(node.right, word)

    def inorder(self):
        """แสดงคำศัพท์ทั้งหมดเรียงตามตัวอักษร"""
        words = []
        self._inorder_recursive(self.root, words)
        return words

    def _inorder_recursive(self, node, words):
        """ช่วยแสดงคำศัพท์ในลำดับ Inorder"""
        if node is not None:
            self._inorder_recursive(node.left, words)
            words.append((node.word, node.meaning, node.word_type, node.example_sentence))
            self._inorder_recursive(node.right, words)

# ฟังก์ชันหลักที่รับข้อมูลจากผู้ใช้
def main():
    dictionary = Dictionary()
    while True:
        print("\nเมนู:")
        print("1. เพิ่มคำศัพท์และความหมาย")
        print("2. ลบคำศัพท์")
        print("3. ค้นหาคำศัพท์")
        print("4. แสดงคำศัพท์ทั้งหมดเรียงตามตัวอักษร")
        print("5. ออกจากโปรแกรม")
        choice = input("เลือกคำสั่ง: ")

        if choice == '1':
            word = input("กรุณากรอกคำศัพท์: ")
            meaning = input("กรุณากรอกคำแปล: ")
            word_type = input("กรุณากรอกชนิดของคำ (noun, verb, adjective, etc.): ")
            example_sentence = input("กรุณากรอกตัวอย่างประโยค: ")
            dictionary.insert(word, meaning, word_type, example_sentence)

        elif choice == '2':
            word = input("กรุณากรอกคำศัพท์ที่ต้องการลบ: ")
            dictionary.delete(word)

        elif choice == '3':
            word = input("กรุณากรอกคำศัพท์ที่ต้องการค้นหา: ")
            entry = dictionary.search(word)
            if entry:
                print(f"คำศัพท์: {entry.word}")
                print(f"คำแปล: {entry.meaning}")
                print(f"ชนิดของคำ: {entry.word_type}")
                print(f"ตัวอย่างประโยค: {entry.example_sentence}")
            else:
                print("ไม่พบคำศัพท์นี้ในพจนานุกรม")

        elif choice == '4':
            words = dictionary.inorder()
            print("คำศัพท์ทั้งหมด (เรียงตามตัวอักษร):")
            for word in words:
                print(f"คำศัพท์: {word[0]}, คำแปล: {word[1]}, ชนิดของคำ: {word[2]}, ตัวอย่างประโยค: {word[3]}")

        elif choice == '5':
            print("ออกจากโปรแกรม")
            break

        else:
            print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")

if __name__ == "__main__":
    main()
