class DictionaryNode:
    def __init__(self, word, meaning, part_of_speech, example_sentence):
        self.word = word
        self.meaning = meaning
        self.part_of_speech = part_of_speech
        self.example_sentence = example_sentence
        self.left = None
        self.right = None

class DictionaryBST:
    def __init__(self):
        self.root = None

    # 1) ฟังก์ชันเพิ่มคำศัพท์และความหมาย
    def insert(self, word, meaning, part_of_speech, example_sentence):
        if self.root is None:
            self.root = DictionaryNode(word, meaning, part_of_speech, example_sentence)
        else:
            self._insert_recursive(self.root, word, meaning, part_of_speech, example_sentence)

    def _insert_recursive(self, node, word, meaning, part_of_speech, example_sentence):
        if word < node.word:
            if node.left is None:
                node.left = DictionaryNode(word, meaning, part_of_speech, example_sentence)
            else:
                self._insert_recursive(node.left, word, meaning, part_of_speech, example_sentence)
        else:
            if node.right is None:
                node.right = DictionaryNode(word, meaning, part_of_speech, example_sentence)
            else:
                self._insert_recursive(node.right, word, meaning, part_of_speech, example_sentence)

    # 2) ฟังก์ชันลบคำศัพท์
    def delete(self, word):
        self.root = self._delete_recursive(self.root, word)

    def _delete_recursive(self, node, word):
        if node is None:
            return node
        if word < node.word:
            node.left = self._delete_recursive(node.left, word)
        elif word > node.word:
            node.right = self._delete_recursive(node.right, word)
        else:
            # ถ้าพบคำศัพท์ที่ต้องการลบ
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # หากมีลูกทั้งสองฝั่ง ต้องหาคำศัพท์ที่มีค่าน้อยที่สุดในด้านขวา (in-order successor)
                min_node = self._min_value_node(node.right)
                node.word, node.meaning, node.part_of_speech, node.example_sentence = min_node.word, min_node.meaning, min_node.part_of_speech, min_node.example_sentence
                node.right = self._delete_recursive(node.right, min_node.word)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # 3) ฟังก์ชันค้นหาคำศัพท์
    def search(self, word):
        return self._search_recursive(self.root, word)

    def _search_recursive(self, node, word):
        if node is None:
            return None
        if word == node.word:
            return node
        elif word < node.word:
            return self._search_recursive(node.left, word)
        else:
            return self._search_recursive(node.right, word)

    # แสดงคำศัพท์ทั้งหมด (Inorder Traversal)
    def display_inorder(self, node, result):
        if node:
            self.display_inorder(node.left, result)
            result.append(f"{node.word}: {node.meaning} ({node.part_of_speech}) - {node.example_sentence}")
            self.display_inorder(node.right, result)

def main():
    dictionary = DictionaryBST()

    while True:
        print("\n*** เมนูพจนานุกรม ***")
        print("1. เพิ่มคำศัพท์และความหมาย")
        print("2. ลบคำศัพท์")
        print("3. ค้นหาคำศัพท์")
        print("4. แสดงคำศัพท์ทั้งหมด")
        print("5. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกตัวเลือก (1-5): ")

        if choice == '1':
            word = input("กรุณาระบุคำศัพท์: ")
            meaning = input("กรุณาระบุคำแปล: ")
            part_of_speech = input("กรุณาระบุชนิดของคำ (noun, verb, adjective, etc.): ")
            example_sentence = input("กรุณาระบุตัวอย่างประโยค: ")
            dictionary.insert(word, meaning, part_of_speech, example_sentence)
            print(f"เพิ่มคำศัพท์ {word} เรียบร้อยแล้ว")

        elif choice == '2':
            word = input("กรุณาระบุคำศัพท์ที่ต้องการลบ: ")
            dictionary.delete(word)
            print(f"ลบคำศัพท์ {word} เรียบร้อยแล้ว")

        elif choice == '3':
            word = input("กรุณาระบุคำศัพท์ที่ต้องการค้นหา: ")
            found_word = dictionary.search(word)
            if found_word:
                print(f"คำศัพท์: {found_word.word}")
                print(f"คำแปล: {found_word.meaning}")
                print(f"ชนิดของคำ: {found_word.part_of_speech}")
                print(f"ตัวอย่างประโยค: {found_word.example_sentence}")
            else:
                print("ไม่พบคำศัพท์ที่ค้นหา")

        elif choice == '4':
            inorder_result = []
            dictionary.display_inorder(dictionary.root, inorder_result)
            print("\nคำศัพท์ทั้งหมด:")
            for word_info in inorder_result:
                print(word_info)

        elif choice == '5':
            print("ขอขอบคุณที่ใช้โปรแกรม!")
            break

        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือกใหม่")

if __name__ == "__main__":
    main()
