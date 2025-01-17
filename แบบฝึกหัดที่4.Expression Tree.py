class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self, expression):
        self.root = self.build_tree(expression)

    def build_tree(self, expression):
        def precedence(op):
            if op in ('+', '-'): return 1
            if op in ('*', '/'): return 2
            return 0

        def apply_operator(operators, operands):
            operator = operators.pop()
            right = operands.pop()
            left = operands.pop()
            node = ExpressionNode(operator)
            node.left = left
            node.right = right
            operands.append(node)

        operators = []
        operands = []
        i = 0
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
                continue
            if expression[i].isdigit():
                num = 0
                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                operands.append(ExpressionNode(num))
                continue
            if expression[i] == '(':
                operators.append(expression[i])
            elif expression[i] == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, operands)
                operators.pop()  # Remove '('
            else:  # Operator
                while (operators and operators[-1] != '(' and
                       precedence(operators[-1]) >= precedence(expression[i])):
                    apply_operator(operators, operands)
                operators.append(expression[i])
            i += 1

        while operators:
            apply_operator(operators, operands)

        return operands[-1]

    def evaluate(self, node):
        if node.left is None and node.right is None:
            return node.value
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val

    def inorder(self, node):
        if node is not None:
            if node.left or node.right:
                print('(', end='')
            self.inorder(node.left)
            print(node.value, end='')
            self.inorder(node.right)
            if node.left or node.right:
                print(')', end='')

    def trace_evaluation(self, node):
        if node.left is None and node.right is None:
            return node.value
        left_val = self.trace_evaluation(node.left)
        right_val = self.trace_evaluation(node.right)
        result = None
        if node.value == '+':
            result = left_val + right_val
        elif node.value == '-':
            result = left_val - right_val
        elif node.value == '*':
            result = left_val * right_val
        elif node.value == '/':
            result = left_val / right_val
        print(f"{left_val} {node.value} {right_val} = {result}")
        return result

# การสร้างและประมวลผล Expression Tree
expressions = [
    "(5 + 3) * (9 - 4)",
    "2 * (7 + 3) / (8 - 6)",
    "(15 / (3 + 2)) - ((4 * 2) + 3)"
]

for i, expr in enumerate(expressions, 1):
    print(f"\n4.{i}) นิพจน์: {expr}")
    tree = ExpressionTree(expr)

    print("โครงสร้าง Tree (Inorder Traversal):", end=' ')
    tree.inorder(tree.root)
    print()

    print("ผลลัพธ์จากการคำนวณ:")
    result = tree.trace_evaluation(tree.root)
    print(f"ผลลัพธ์สุดท้าย: {result}")
