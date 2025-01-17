class FileSystem:
    def __init__(self):
        self.structure = {"root": {}}  # เริ่มต้นด้วยโฟลเดอร์ root เป็นโฟลเดอร์หลัก

    def create_folder(self, folder_name, parent_folder="root"):
        """สร้างโฟลเดอร์ใหม่ในโฟลเดอร์ที่กำหนด"""
        # ตรวจสอบว่าโฟลเดอร์พ่อมีอยู่หรือไม่
        if parent_folder not in self.structure:
            print(f"โฟลเดอร์ '{parent_folder}' ไม่พบในระบบ")
            return

        # ตรวจสอบว่าโฟลเดอร์ใหม่มีอยู่แล้วหรือไม่
        if folder_name not in self.structure[parent_folder]:
            self.structure[parent_folder][folder_name] = {}
            print(f"โฟลเดอร์ '{folder_name}' ถูกสร้างใน '{parent_folder}'")
        else:
            print(f"โฟลเดอร์ '{folder_name}' มีอยู่แล้วใน '{parent_folder}'")
    
    def create_file(self, file_name, folder_name):
        """สร้างไฟล์ใหม่ในโฟลเดอร์ที่กำหนด"""
        if folder_name in self.structure and file_name not in self.structure[folder_name]:
            self.structure[folder_name][file_name] = None
            print(f"ไฟล์ '{file_name}' ถูกสร้างในโฟลเดอร์ '{folder_name}'")
        else:
            print(f"ไม่พบโฟลเดอร์ '{folder_name}' หรือไฟล์ '{file_name}' มีอยู่แล้ว")
    
    def delete(self, name, folder_name=None):
        """ลบไฟล์หรือโฟลเดอร์"""
        if folder_name:
            if name in self.structure.get(folder_name, {}):
                del self.structure[folder_name][name]
                print(f"ไฟล์/โฟลเดอร์ '{name}' ถูกลบจาก '{folder_name}'")
            else:
                print(f"ไม่พบ '{name}' ใน '{folder_name}'")
        else:
            if name in self.structure:
                del self.structure[name]
                print(f"โฟลเดอร์ '{name}' ถูกลบ")
            else:
                print(f"ไม่พบโฟลเดอร์ '{name}'")
    
    def display_structure(self, current_folder="root", indent=0):
        """แสดงโครงสร้างไฟล์และโฟลเดอร์ทั้งหมด"""
        print("  " * indent + f"[{current_folder}]")
        for folder, content in self.structure.get(current_folder, {}).items():
            if isinstance(content, dict):
                self.display_structure(folder, indent + 1)
            else:
                print("  " * (indent + 1) + f"- {folder}")
    
    def search(self, name, current_folder="root"):
        """ค้นหาไฟล์หรือโฟลเดอร์"""
        if name in self.structure.get(current_folder, {}):
            print(f"พบ '{name}' ใน '{current_folder}'")
        else:
            for folder in self.structure.get(current_folder, {}):
                if isinstance(self.structure[current_folder][folder], dict):
                    self.search(name, folder)

# การทดสอบการทำงาน
fs = FileSystem()

# สร้างโฟลเดอร์
fs.create_folder("Documents")
fs.create_folder("Projects", "Documents")
fs.create_folder("Reports", "Projects")
fs.create_folder("2025", "Reports")
fs.create_folder("January", "2025")

# สร้างไฟล์
fs.create_file("file1.txt", "Documents")
fs.create_file("project1.txt", "Projects")
fs.create_file("report1.txt", "Reports/Projects")

# แสดงโครงสร้าง
fs.display_structure()

# ลบไฟล์
fs.delete("file1.txt", "Documents")

# แสดงโครงสร้างหลังลบไฟล์
fs.display_structure()

# ค้นหาไฟล์หรือโฟลเดอร์
fs.search("Projects")
fs.search("January")
fs.search("file1.txt", "Documents")
