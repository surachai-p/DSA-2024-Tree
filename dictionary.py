class DictionaryNode:
    def __init__(self, word, meaning, word_type, example):
        self.word = word
        self.meaning = meaning
        self.word_type = word_type
        self.example = example
        self.left = None
        self.right = None

class DictionaryBST:
    def __init__(self):
        self.root = None

    # 1) เพิ่มคำศัพท์
    def insert(self, root, word, meaning, word_type, example):
        if root is None:
            return DictionaryNode(word, meaning, word_type, example)

        if word < root.word:
            root.left = self.insert(root.left, word, meaning, word_type, example)
        elif word > root.word:
            root.right = self.insert(root.right, word, meaning, word_type, example)

        return root

    def add_word(self, word, meaning, word_type, example):
        self.root = self.insert(self.root, word, meaning, word_type, example)

    # 2) ลบคำศัพท์
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, word):
        if root is None:
            return root

        if word < root.word:
            root.left = self.delete(root.left, word)
        elif word > root.word:
            root.right = self.delete(root.right, word)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.word = temp.word
            root.meaning = temp.meaning
            root.word_type = temp.word_type
            root.example = temp.example
            root.right = self.delete(root.right, temp.word)

        return root

    def delete_word(self, word):
        self.root = self.delete(self.root, word)

    # 3) ค้นหาคำศัพท์
    def search(self, root, word):
        if root is None or root.word == word:
            return root

        if word < root.word:
            return self.search(root.left, word)
        return self.search(root.right, word)

    def find_word(self, word):
        result = self.search(self.root, word)
        if result:
            return f"คำศัพท์: {result.word}\nความหมาย: {result.meaning}\nชนิดของคำ: {result.word_type}\nตัวอย่าง: {result.example}"
        else:
            return "ไม่พบคำศัพท์"

    # แสดงคำศัพท์ทั้งหมดในลำดับที่เรียงตามตัวอักษร
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"{root.word} ({root.word_type}): {root.meaning} | ตัวอย่าง: {root.example}")
            self.inorder(root.right)

    def display_dictionary(self):
        self.inorder(self.root)



dictionary = DictionaryBST()
dictionary.add_word("apple", "แอปเปิล", "noun", "She ate a red apple.")
dictionary.add_word("banana", "กล้วย", "noun", "He likes banana smoothies.")
dictionary.add_word("run", "วิ่ง", "verb", "He runs every morning.")
dictionary.add_word("happy", "มีความสุข", "adjective", "She felt happy today.")

print("พจนานุกรมเรียงลำดับคำศัพท์:")
dictionary.display_dictionary()

print("\nค้นหาคำศัพท์ 'banana':")
print(dictionary.find_word("banana"))

print("\nลบคำศัพท์ 'apple'")
dictionary.delete_word("apple")

print("พจนานุกรมหลังจากลบคำว่า 'apple':")
dictionary.display_dictionary()
