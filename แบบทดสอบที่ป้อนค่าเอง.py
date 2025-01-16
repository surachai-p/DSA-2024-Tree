class DictionaryNode:
    def __init__(self, word, meaning, word_type, example_sentence):
        self.word = word
        self.meaning = meaning
        self.word_type = word_type
        self.example_sentence = example_sentence
        self.left = None
        self.right = None

# ฟังก์ชันเพิ่มคำศัพท์
def insert_word(root, word, meaning, word_type, example_sentence):
    if root is None:
        return DictionaryNode(word, meaning, word_type, example_sentence)
    
    if word < root.word:
        root.left = insert_word(root.left, word, meaning, word_type, example_sentence)
    elif word > root.word:
        root.right = insert_word(root.right, word, meaning, word_type, example_sentence)
    
    return root

# ฟังก์ชันค้นหาคำศัพท์
def search_word(root, word):
    if root is None or root.word == word:
        return root
    
    if word < root.word:
        return search_word(root.left, word)
    
    return search_word(root.right, word)

# ฟังก์ชันลบคำศัพท์
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_word(root, word):
    if root is None:
        return root
    
    if word < root.word:
        root.left = delete_word(root.left, word)
    elif word > root.word:
        root.right = delete_word(root.right, word)
    else:
        # กรณีที่ Node ที่ต้องการลบไม่มีลูก หรือมีลูกแค่ 1 Node
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # กรณีที่ Node ที่ต้องการลบมีลูก 2 Node
        # หาค่าต่ำสุดใน right subtree
        temp = find_min(root.right)
        root.word = temp.word
        root.meaning = temp.meaning
        root.word_type = temp.word_type
        root.example_sentence = temp.example_sentence
        root.right = delete_word(root.right, temp.word)
    
    return root

# ฟังก์ชันแสดงคำศัพท์ทั้งหมดในรูปแบบ In-Order Traversal
def display_words_in_order(root):
    if root is not None:
        display_words_in_order(root.left)
        print(f"Word: {root.word}, Meaning: {root.meaning}, Type: {root.word_type}, Example: {root.example_sentence}")
        display_words_in_order(root.right)

# ฟังก์ชันเมนู
def menu():
    print("\n---- เมนูพจนานุกรม ----")
    print("1. เพิ่มคำศัพท์")
    print("2. ค้นหาคำศัพท์")
    print("3. ลบคำศัพท์")
    print("4. แสดงคำศัพท์ทั้งหมด")
    print("5. ออกจากโปรแกรม")

# โปรแกรมหลัก
def main():
    root = None
    while True:
        menu()
        choice = input("กรุณาเลือกคำสั่ง (1-5): ")
        
        if choice == "1":
            word = input("กรุณาป้อนคำศัพท์ภาษาอังกฤษ: ")
            meaning = input("กรุณาป้อนคำแปลภาษาไทย: ")
            word_type = input("กรุณาป้อนชนิดของคำ (noun, verb, adjective, etc.): ")
            example_sentence = input("กรุณาป้อนตัวอย่างประโยค: ")
            root = insert_word(root, word, meaning, word_type, example_sentence)
            print("เพิ่มคำศัพท์สำเร็จ!")
        
        elif choice == "2":
            word = input("กรุณาป้อนคำศัพท์ที่ต้องการค้นหา: ")
            result = search_word(root, word)
            if result:
                print(f"คำศัพท์: {result.word}\nความหมาย: {result.meaning}\nชนิดของคำ: {result.word_type}\nตัวอย่างประโยค: {result.example_sentence}")
            else:
                print("ไม่พบคำศัพท์นี้ในพจนานุกรม")

        elif choice == "3":
            word = input("กรุณาป้อนคำศัพท์ที่ต้องการลบ: ")
            root = delete_word(root, word)
            print("ลบคำศัพท์สำเร็จ!")
        
        elif choice == "4":
            print("\nคำศัพท์ทั้งหมดในพจนานุกรม:")
            display_words_in_order(root)
        
        elif choice == "5":
            print("ออกจากโปรแกรม")
            break
        
        else:
            print("กรุณาเลือกคำสั่งที่ถูกต้อง (1-5)")

# เรียกใช้งานโปรแกรมหลัก
if __name__ == "__main__":
    main()
