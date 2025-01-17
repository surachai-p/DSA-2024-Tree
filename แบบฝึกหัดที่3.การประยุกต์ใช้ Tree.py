class FileSystem:
    def __init__(self):
        self.structure = {}

    # 3.1 สร้างโฟลเดอร์ใหม่
    def create_folder(self, folder_path):
        parts = folder_path.split('/')
        current = self.structure
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]
        print(f"สร้างโฟลเดอร์: {folder_path}")

    # 3.2 สร้างไฟล์ใหม่ในโฟลเดอร์ที่กำหนด
    def create_file(self, folder_path, file_name):
        parts = folder_path.split('/')
        current = self.structure
        for part in parts:
            if part not in current:
                print(f"โฟลเดอร์ {folder_path} ไม่พบ")
                return
            current = current[part]
        if file_name not in current:
            current[file_name] = None
            print(f"สร้างไฟล์: {folder_path}/{file_name}")
        else:
            print(f"ไฟล์ {file_name} มีอยู่แล้วในโฟลเดอร์ {folder_path}")

    # 3.3 ลบโฟลเดอร์หรือไฟล์
    def delete(self, path):
        parts = path.split('/')
        current = self.structure
        for part in parts[:-1]:
            if part not in current:
                print(f"ไม่พบ {path}")
                return
            current = current[part]
        if parts[-1] in current:
            del current[parts[-1]]
            print(f"ลบ {path} สำเร็จ")
        else:
            print(f"ไม่พบ {path}")

    # 3.4 แสดงโครงสร้างไฟล์และโฟลเดอร์ทั้งหมด
    def display_structure(self, current=None, indent=0):
        if current is None:
            current = self.structure
        for key, value in current.items():
            print('  ' * indent + key)
            if isinstance(value, dict):
                self.display_structure(value, indent + 1)

    # 3.5 ค้นหาไฟล์หรือโฟลเดอร์
    def search(self, name, current=None, path=""):
        if current is None:
            current = self.structure
        for key, value in current.items():
            full_path = f"{path}/{key}" if path else key
            if key == name:
                print(f"พบ {name} ที่ {full_path}")
            if isinstance(value, dict):
                self.search(name, value, full_path)

# การใช้งาน
fs = FileSystem()

# สร้างโฟลเดอร์ใหม่
fs.create_folder("home")
fs.create_folder("home/user")
fs.create_folder("home/user/documents")

# สร้างไฟล์ใหม่ในโฟลเดอร์ที่กำหนด
fs.create_file("home/user", "notes.txt")
fs.create_file("home/user/documents", "report.pdf")

# ลบโฟลเดอร์หรือไฟล์
fs.delete("home/user/notes.txt")
fs.delete("home/user/music")

# แสดงโครงสร้างไฟล์และโฟลเดอร์ทั้งหมด
print("\nโครงสร้างไฟล์และโฟลเดอร์:")
fs.display_structure()

# ค้นหาไฟล์หรือโฟลเดอร์
print("\nค้นหาไฟล์หรือโฟลเดอร์:")
fs.search("documents")
fs.search("report.pdf")
