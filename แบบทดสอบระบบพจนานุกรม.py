class DictionaryNode:
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

    # 1) เพิ่มคำศัพท์และความหมาย
    def add_word(self, word, meaning, word_type, example):
        new_node = DictionaryNode(word, meaning, word_type, example)

        if self.root is None:
            self.root = new_node
            print(f"เพิ่มคำศัพท์ '{word}' สำเร็จ")
            return

        current = self.root
        while True:
            if word < current.word:
                if current.left is None:
                    current.left = new_node
                    print(f"เพิ่มคำศัพท์ '{word}' สำเร็จ")
                    return
                current = current.left
            elif word > current.word:
                if current.right is None:
                    current.right = new_node
                    print(f"เพิ่มคำศัพท์ '{word}' สำเร็จ")
                    return
                current = current.right
            else:
                print(f"คำศัพท์ '{word}' มีอยู่ในระบบแล้ว")
                return

    # 2) ลบคำศัพท์
    def delete_word(self, word):
        def delete_node(root, word):
            if root is None:
                return root

            if word < root.word:
                root.left = delete_node(root.left, word)
            elif word > root.word:
                root.right = delete_node(root.right, word)
            else:
                # Case: Node with one or no child
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                # Case: Node with two children
                min_larger_node = self.find_min(root.right)
                root.word = min_larger_node.word
                root.meaning = min_larger_node.meaning
                root.word_type = min_larger_node.word_type
                root.example = min_larger_node.example
                root.right = delete_node(root.right, min_larger_node.word)

            return root

        self.root = delete_node(self.root, word)
        print(f"ลบคำศัพท์ '{word}' สำเร็จ")

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # 3) ค้นหาคำศัพท์
    def search_word(self, word):
        current = self.root
        while current is not None:
            if word < current.word:
                current = current.left
            elif word > current.word:
                current = current.right
            else:
                print(f"คำศัพท์: {current.word}\nคำแปล: {current.meaning}\nชนิดของคำ: {current.word_type}\nตัวอย่าง: {current.example}")
                return
        print(f"ไม่พบคำศัพท์ '{word}' ในระบบ")

    # แสดงคำศัพท์ทั้งหมด (Inorder Traversal)
    def display_all_words(self):
        def inorder_traversal(node):
            if node is not None:
                inorder_traversal(node.left)
                print(f"คำศัพท์: {node.word}\nคำแปล: {node.meaning}\nชนิดของคำ: {node.word_type}\nตัวอย่าง: {node.example}\n")
                inorder_traversal(node.right)

        inorder_traversal(self.root)

# การใช้งาน
my_dict = Dictionary()

while True:
    print("\nระบบพจนานุกรม")
    print("1. เพิ่มคำศัพท์")
    print("2. ลบคำศัพท์")
    print("3. ค้นหาคำศัพท์")
    print("4. แสดงคำศัพท์ทั้งหมด")
    print("5. ออกจากระบบ")
    choice = input("เลือกเมนู (1-5): ")

    if choice == "1":
        word = input("ป้อนคำศัพท์ภาษาอังกฤษ: ")
        meaning = input("ป้อนคำแปลภาษาไทย: ")
        word_type = input("ป้อนชนิดของคำ (noun, verb, adjective, etc.): ")
        example = input("ป้อนตัวอย่างประโยค: ")
        my_dict.add_word(word, meaning, word_type, example)

    elif choice == "2":
        word = input("ป้อนคำศัพท์ที่ต้องการลบ: ")
        my_dict.delete_word(word)

    elif choice == "3":
        word = input("ป้อนคำศัพท์ที่ต้องการค้นหา: ")
        my_dict.search_word(word)

    elif choice == "4":
        print("\nคำศัพท์ทั้งหมดในระบบ:")
        my_dict.display_all_words()

    elif choice == "5":
        print("ออกจากระบบพจนานุกรม")
        break

    else:
        print("เลือกเมนูไม่ถูกต้อง กรุณาลองใหม่")
