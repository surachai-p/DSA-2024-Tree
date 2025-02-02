class DictionaryEntry:
    def __init__(self, word, meaning, part_of_speech, example):
        self.word = word  # คำศัพท์ภาษาอังกฤษ
        self.meaning = meaning  # คำแปลภาษาไทย
        self.part_of_speech = part_of_speech  # ชนิดของคำ (noun, verb, adjective, etc.)
        self.example = example  # ตัวอย่างประโยค

class Node:
    def __init__(self, entry):
        self.entry = entry  # ข้อมูลของคำศัพท์
        self.left = None  # ลูกซ้าย
        self.right = None  # ลูกขวา

# ฟังก์ชันเพิ่มคำศัพท์
def insert(root, entry):
    if root is None:
        return Node(entry)
    
    if entry.word < root.entry.word:
        root.left = insert(root.left, entry)
    elif entry.word > root.entry.word:
        root.right = insert(root.right, entry)
    
    return root

# ฟังก์ชันลบคำศัพท์
def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, word):
    if root is None:
        return root

    # ค้นหาคำศัพท์ที่จะลบ
    if word < root.entry.word:
        root.left = delete(root.left, word)
    elif word > root.entry.word:
        root.right = delete(root.right, word)
    else:
        # กรณีที่ Node ที่ต้องการลบมีลูก 0 หรือ 1
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # กรณีที่ Node ที่ต้องการลบมีลูก 2 ตัว
        temp = find_min(root.right)
        root.entry = temp.entry  # แทนที่ข้อมูล
        root.right = delete(root.right, temp.entry.word)

    return root

# ฟังก์ชันค้นหาคำศัพท์
def search(root, word):
    if root is None or root.entry.word == word:
        return root

    if word < root.entry.word:
        return search(root.left, word)

    return search(root.right, word)

# ฟังก์ชันแสดงข้อมูลคำศัพท์ทั้งหมด (Inorder Traversal)
def inorder(root):
    if root:
        inorder(root.left)
        print(f"คำศัพท์: {root.entry.word}")
        print(f"คำแปล: {root.entry.meaning}")
        print(f"ชนิดของคำ: {root.entry.part_of_speech}")
        print(f"ตัวอย่างประโยค: {root.entry.example}\n")
        inorder(root.right)

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    root = None

    # เพิ่มคำศัพท์
    entry1 = DictionaryEntry("apple", "แอปเปิ้ล", "noun", "I ate an apple.")
    entry2 = DictionaryEntry("run", "วิ่ง", "verb", "She runs every morning.")
    entry3 = DictionaryEntry("beautiful", "สวยงาม", "adjective", "The view is beautiful.")
    entry4 = DictionaryEntry("book", "หนังสือ", "noun", "He is reading a book.")

    root = insert(root, entry1)
    root = insert(root, entry2)
    root = insert(root, entry3)
    root = insert(root, entry4)

    # แสดงข้อมูลคำศัพท์ทั้งหมด
    print("ข้อมูลคำศัพท์ทั้งหมด:")
    inorder(root)

    # ค้นหาคำศัพท์
    search_word = "run"
    found_entry = search(root, search_word)
    if found_entry:
        print(f"คำศัพท์ที่ค้นหา: {found_entry.entry.word}")
        print(f"คำแปล: {found_entry.entry.meaning}")
        print(f"ชนิดของคำ: {found_entry.entry.part_of_speech}")
        print(f"ตัวอย่างประโยค: {found_entry.entry.example}")
    else:
        print(f"ไม่พบคำศัพท์ '{search_word}' ในพจนานุกรม")

    # ลบคำศัพท์
    word_to_delete = "apple"
    root = delete(root, word_to_delete)

    # แสดงข้อมูลคำศัพท์หลังการลบ
    print("\nหลังการลบคำศัพท์ 'apple':")
    inorder(root)