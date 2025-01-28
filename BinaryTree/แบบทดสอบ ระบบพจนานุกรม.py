class DictionaryNode:
    def __init__(self, word, meaning, word_type, example_sentence):
        self.word = word                # คำศัพท์ภาษาอังกฤษ
        self.meaning = meaning          # คำแปลภาษาไทย
        self.word_type = word_type      # ชนิดของคำ (noun, verb, etc.)
        self.example_sentence = example_sentence  # ตัวอย่างประโยค
        self.left = None                # โหนดซ้าย
        self.right = None               # โหนดขวา

# ฟังก์ชันเพิ่มคำศัพท์
def insert(root, word, meaning, word_type, example_sentence):
    if root is None:
        return DictionaryNode(word, meaning, word_type, example_sentence)
    
    if word < root.word:
        root.left = insert(root.left, word, meaning, word_type, example_sentence)
    elif word > root.word:
        root.right = insert(root.right, word, meaning, word_type, example_sentence)
    
    return root

# ฟังก์ชันค้นหาคำศัพท์
def search(root, word):
    if root is None or root.word == word:
        return root
    
    if word < root.word:
        return search(root.left, word)
    
    return search(root.right, word)

# ฟังก์ชันลบคำศัพท์
def delete(root, word):
    if root is None:
        return root
    
    if word < root.word:
        root.left = delete(root.left, word)
    elif word > root.word:
        root.right = delete(root.right, word)
    else:
        # คำศัพท์ที่ต้องการลบพบแล้ว
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # หากมีลูก 2 โหนด ให้หาค่าต่ำสุดจากโหนดขวา
        temp = find_min(root.right)
        root.word = temp.word
        root.meaning = temp.meaning
        root.word_type = temp.word_type
        root.example_sentence = temp.example_sentence
        root.right = delete(root.right, temp.word)
    
    return root

# ฟังก์ชันหาค่าต่ำสุดใน BST
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# ฟังก์ชันแสดงคำศัพท์ทั้งหมดในรูปแบบ Inorder Traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(f"คำศัพท์: {root.word}")
        print(f"คำแปล: {root.meaning}")
        print(f"ชนิดของคำ: {root.word_type}")
        print(f"ตัวอย่างประโยค: {root.example_sentence}")
        print("-" * 30)
        inorder_traversal(root.right)

# ฟังก์ชันรับข้อมูลจากผู้ใช้
def get_word_data():
    word = input("กรุณากรอกคำศัพท์ภาษาอังกฤษ: ")
    meaning = input("กรุณากรอกคำแปลภาษาไทย: ")
    word_type = input("กรุณากรอกชนิดของคำ (noun, verb, adjective, etc.): ")
    example_sentence = input("กรุณากรอกตัวอย่างประโยค: ")
    return word, meaning, word_type, example_sentence

# ฟังก์ชันหลัก
if __name__ == "__main__":
    root = None
    while True:
        print("\n--- ระบบพจนานุกรม ---")
        print("1. เพิ่มคำศัพท์")
        print("2. ค้นหาคำศัพท์")
        print("3. ลบคำศัพท์")
        print("4. แสดงคำศัพท์ทั้งหมด")
        print("5. ออกจากระบบ")
        
        choice = input("กรุณาเลือกตัวเลือก (1-5): ")
        
        if choice == '1':
            word, meaning, word_type, example_sentence = get_word_data()
            root = insert(root, word, meaning, word_type, example_sentence)
            print(f"เพิ่มคำศัพท์ '{word}' สำเร็จ!")
        
        elif choice == '2':
            search_word = input("กรุณากรอกคำศัพท์ที่ต้องการค้นหา: ")
            result = search(root, search_word)
            if result:
                print(f"คำศัพท์: {result.word}")
                print(f"คำแปล: {result.meaning}")
                print(f"ชนิดของคำ: {result.word_type}")
                print(f"ตัวอย่างประโยค: {result.example_sentence}")
            else:
                print("ไม่พบคำศัพท์นี้ในระบบ")
        
        elif choice == '3':
            delete_word = input("กรุณากรอกคำศัพท์ที่ต้องการลบ: ")
            root = delete(root, delete_word)
            print(f"ลบคำศัพท์ '{delete_word}' สำเร็จ!")
        
        elif choice == '4':
            print("\nรายการคำศัพท์ทั้งหมด (เรียงตามลำดับอักษร):")
            inorder_traversal(root)
        
        elif choice == '5':
            print("ขอบคุณที่ใช้ระบบพจนานุกรม!")
            break
        
        else:
            print("ตัวเลือกไม่ถูกต้อง! กรุณาเลือกใหม่.")
