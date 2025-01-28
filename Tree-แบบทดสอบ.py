class Word:
    def __init__(self, word, meaning, part_of_speech, example):
        self.word = word
        self.meaning = meaning
        self.part_of_speech = part_of_speech
        self.example = example


class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, word):
        if root is None:
            return Node(word)

        if word.word < root.word.word:
            root.left = self.insert(root.left, word)
        elif word.word > root.word.word:
            root.right = self.insert(root.right, word)

        return root

    def search(self, root, word):
        if root is None or root.word.word == word:
            return root

        if word < root.word.word:
            return self.search(root.left, word)
        return self.search(root.right, word)

    def delete(self, root, word):
        if root is None:
            return root

        if word < root.word.word:
            root.left = self.delete(root.left, word)
        elif word > root.word.word:
            root.right = self.delete(root.right, word)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.word = temp.word
            root.right = self.delete(root.right, temp.word.word)

        return root

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"Word: {root.word.word}, Meaning: {root.word.meaning}, Part of Speech: {root.word.part_of_speech}, Example: {root.word.example}")
            self.inorder(root.right)

    def get_root(self):
        return self.root


def get_word_input():
    word = input("กรอกคำศัพท์ (ภาษาอังกฤษ): ")
    meaning = input("กรอกคำแปล (ภาษาไทย): ")
    part_of_speech = input("กรอกชนิดของคำ (noun, verb, adjective, etc.): ")
    example = input("กรอกตัวอย่างประโยค: ")
    return Word(word, meaning, part_of_speech, example)


def main():
    bst = BinarySearchTree()

    while True:
        print("\n--- ระบบพจนานุกรม ---")
        print("1. เพิ่มคำศัพท์")
        print("2. ลบคำศัพท์")
        print("3. ค้นหาคำศัพท์")
        print("4. แสดงคำศัพท์ทั้งหมด")
        print("5. ออกจากระบบ")
        choice = input("กรุณาเลือกตัวเลือก (1-5): ")

        if choice == '1':
            # เพิ่มคำศัพท์
            word = get_word_input()
            bst.root = bst.insert(bst.root, word)
            print("คำศัพท์ได้ถูกเพิ่มแล้ว!")

        elif choice == '2':
            # ลบคำศัพท์
            word_to_delete = input("กรุณากรอกคำศัพท์ที่ต้องการลบ: ")
            bst.root = bst.delete(bst.root, word_to_delete)
            print(f"คำศัพท์ '{word_to_delete}' ได้ถูกลบออกจากพจนานุกรม!")

        elif choice == '3':
            # ค้นหาคำศัพท์
            word_to_search = input("กรุณากรอกคำศัพท์ที่ต้องการค้นหา: ")
            result = bst.search(bst.root, word_to_search)
            if result:
                print(f"พบคำศัพท์ '{word_to_search}':")
                print(f"คำแปล: {result.word.meaning}")
                print(f"ชนิดของคำ: {result.word.part_of_speech}")
                print(f"ตัวอย่างประโยค: {result.word.example}")
            else:
                print(f"ไม่พบคำศัพท์ '{word_to_search}'")

        elif choice == '4':
            # แสดงคำศัพท์ทั้งหมด
            print("\nคำศัพท์ทั้งหมดในพจนานุกรม:")
            bst.inorder(bst.root)

        elif choice == '5':
            # ออกจากระบบ
            print("ออกจากระบบ...")
            break

        else:
            print("ตัวเลือกไม่ถูกต้อง, กรุณาลองใหม่อีกครั้ง")

if __name__ == "__main__":
    main()
