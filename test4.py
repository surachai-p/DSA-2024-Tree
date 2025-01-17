class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self, expression):
        self.expression = expression
        self.root = None

    def build(self):
        # ใช้ stack ในการสร้างต้นไม้จากการประมวลผลแบบ infix (แบบปกติ)
        stack = []
        postfix = self.infix_to_postfix(self.expression)
        
        for char in postfix:
            if char.isdigit():
                stack.append(TreeNode(int(char)))
            elif char in "+-*/":
                node = TreeNode(char)
                node.right = stack.pop()  # ดึง operand ขวามา
                node.left = stack.pop()   # ดึง operand ซ้ายมา
                stack.append(node)  # ใส่ node นี้กลับไปที่ stack
        self.root = stack.pop()  # ค่าใน stack จะเป็น root ของต้นไม้

    def infix_to_postfix(self, expression):
        """แปลงนิพจน์จาก infix เป็น postfix"""
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operators = []
        
        for char in expression:
            if char.isdigit():
                output.append(char)
            elif char == '(':
                operators.append(char)
            elif char == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # เอา '(' ออก
            elif char in precedence:
                while (operators and operators[-1] in precedence and
                       precedence[char] <= precedence[operators[-1]]):
                    output.append(operators.pop())
                operators.append(char)
        
        while operators:
            output.append(operators.pop())
        
        return output
    
    def evaluate(self, node=None, steps=None):
        """คำนวณค่าของ Expression Tree"""
        if steps is None:
            steps = []
        if node is None:
            node = self.root
        
        if node.left is None and node.right is None:  # ถ้าเป็นตัวเลข (leaf node)
            return node.value
        
        left_value = self.evaluate(node.left, steps)
        right_value = self.evaluate(node.right, steps)
        
        # บันทึกการคำนวณ
        steps.append(f"({left_value} {node.value} {right_value})")
        
        # คำนวณค่า
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value
    
    def display(self, node=None, indent=0):
        """แสดงโครงสร้างของ Expression Tree"""
        if node is None:
            node = self.root
        
        if node.right:
            self.display(node.right, indent + 4)  # แสดงขวามากขึ้น
        print(" " * indent + str(node.value))  # แสดงค่า node พร้อมการเว้นช่องว่าง
        if node.left:
            self.display(node.left, indent + 4)  # แสดงซ้ายมากขึ้น


# นิพจน์ที่ให้มา
expressions = [
    "(5 + 3) * (9 - 4)",
    "2 * (7 + 3) / (8 - 6)",
    "(15 / (3 + 2)) - ((4 * 2) + 3)"
]

for expression in expressions:
    print(f"นิพจน์: {expression}")
    expression_tree = ExpressionTree(expression)
    expression_tree.build()
    
    # แสดงโครงสร้างต้นไม้
    print("\nแสดงโครงสร้าง Expression Tree:")
    expression_tree.display()

    # คำนวณและแสดงผล
    steps = []
    result = expression_tree.evaluate(steps=steps)

    print("\nลำดับการคำนวณ:")
    for step in steps:
        print(step)

    print(f"\nผลลัพธ์: {result}\n" + "="*50)
