class Node:
    def __init__(self, word, meaning, word_type, example):
        self.word = word
        self.meaning = meaning
        self.word_type = word_type
        self.example = example
        self.left = None
        self.right = None

class Dictionary:
    def __init__(self):
        self.root = None

    def insert(self, root, word, meaning, word_type, example):
        if root is None:
            return Node(word, meaning, word_type, example)
        if word < root.word:
            root.left = self.insert(root.left, word, meaning, word_type, example)
        elif word > root.word:
            root.right = self.insert(root.right, word, meaning, word_type, example)
        return root

    def search(self, root, word):
        if root is None or root.word == word:
            return root
        if word < root.word:
            return self.search(root.left, word)
        return self.search(root.right, word)

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
            root.word, root.meaning, root.word_type, root.example = temp.word, temp.meaning, temp.word_type, temp.example
            root.right = self.delete(root.right, temp.word)
        return root

    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"Word: {root.word}, Meaning: {root.meaning}, Type: {root.word_type}, Example: {root.example}")
            self.inorder(root.right)

# สร้างตัวอย่างคำศัพท์ 5 คำ
dictionary = Dictionary()
dictionary.root = dictionary.insert(dictionary.root, "apple", "แอปเปิ้ล", "noun", "I eat an apple every morning.")
dictionary.root = dictionary.insert(dictionary.root, "run", "วิ่ง", "verb", "She runs every day to stay fit.")
dictionary.root = dictionary.insert(dictionary.root, "beautiful", "สวยงาม", "adjective", "The view from the mountain is beautiful.")
dictionary.root = dictionary.insert(dictionary.root, "cat", "แมว", "noun", "The cat sleeps on the sofa.")
dictionary.root = dictionary.insert(dictionary.root, "quickly", "อย่างรวดเร็ว", "adverb", "He ran quickly to catch the bus.")

# ทดสอบค้นหาคำศัพท์
search_word = "run"
found = dictionary.search(dictionary.root, search_word)
if found:
    print(f"Found word: {found.word}, Meaning: {found.meaning}, Type: {found.word_type}, Example: {found.example}")
else:
    print(f"Word '{search_word}' not found.")

# แสดงรายชื่อคำศัพท์ทั้งหมด
print("\nDictionary content:")
dictionary.inorder(dictionary.root)

# ทดสอบการลบคำศัพท์
dictionary.root = dictionary.delete(dictionary.root, "cat")
print("\nAfter deleting 'cat':")
dictionary.inorder(dictionary.root)
