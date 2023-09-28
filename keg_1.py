# Fungsi pengurangan
def subtract(a, b):
    return a - b

sub_result = subtract(8, 6)
print(sub_result)

# Fungsi perkalian
def multiply(a, b):
    return a * b

mul_result = multiply(8, 6)
print(mul_result)


# Fungsi pembagian
def divide(a, b):
    return a / b

div_result = divide(8, 6)
print(div_result)


# Tree
def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        if operator == '+':
            return tree(left_operand) + tree(right_operand)
        elif operator == '-':
            return tree(left_operand) - tree(right_operand)
        elif operator == '*':
            return tree(left_operand) * tree(right_operand)
        elif operator == '/':
            return tree(left_operand) / tree(right_operand)
    else:
        raise ValueError("Pohon ekspresi tidak valid")

# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

# Hasil dari tree
print("Hasil evaluasi pohon ekspresi: ", result)