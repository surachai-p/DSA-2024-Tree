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

    def insert(self, word, meaning, word_type, example):
        self.root = self._insert(self.root, word, meaning, word_type, example)
    
    def _insert(self, node, word, meaning, word_type, example):
        if node is None:
            return DictionaryNode(word, meaning, word_type, example)
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
            node.word, node.meaning, node.word_type, node.example = temp.word, temp.meaning, temp.word_type, temp.example
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

# ทดสอบโปรแกรม
dictionary = DictionaryBST()
dictionary.insert("apple", "แอปเปิ้ล", "noun", "I eat an apple every day.")
dictionary.insert("run", "วิ่ง", "verb", "She can run very fast.")

dict_entry = dictionary.search("apple")
if dict_entry:
    print(f"คำศัพท์: {dict_entry.word}, ความหมาย: {dict_entry.meaning}, ชนิดคำ: {dict_entry.word_type}, ตัวอย่าง: {dict_entry.example}")

dictionary.delete("run")
