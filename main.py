import math

import BinaryTree

operators_dict = {
    "+": [1, 'm'],
    "-": [1, 'm'],
    "*": [2, 'm'],
    "/": [2, 'm'],
    "^": [3, 'm'],
    "@": [5, 'm'],
    "$": [5, 'm'],
    "&": [5, 'm'],
    "%": [4, 'm'],
    "~": [6, 'l'],
    "!": [6, 'r'],
    "#": [6, 'r'],
}


def check_validity(expression: str) -> bool:
    '''
    the function checks if the given expression only has operands , operators and brackets
    :param expression: str
    :return: if expression is valid, return True. else return False.
    '''
    for current_char in expression:
        if current_char not in operators_dict.keys() and not current_char.isnumeric() and current_char not in ['(', ')']:
            return False
    return True


def get_all_operands(equ: str) -> list:
    operands_list = []
    index = 0
    for current_char in equ:
        if current_char in operators_dict.keys() or current_char in ['(', ')']:
            operands_list.append((current_char, index))
        index += 1
    return operands_list


def get_lowest_priority(operators: list) -> tuple:
    '''
    function receives list of operands as they appear in a math expression,
    returns the lowest precedence operators and its index in the expression.
    :param operators: list
    :return: if the function is valid in terms of brackets, return the lowest precedence operator and its index.
    else, return 0 and -1 to indicate error
    '''
    max_pre = 6
    index = 0
    opr = operators[0][0]
    open_brackets = []
    for operand, i in operators:
        if operand == '(':
            open_brackets.append(operand)
        if operand == ')':
            if not open_brackets:
                return '0', -1
            if open_brackets:
                open_brackets.pop()
        if operand not in [')', '('] and operators_dict[operand][0] <= max_pre and not open_brackets:
            if operand == '-':
                if i == 0 or operators[operators.index((operand, i)) - 1][1] == i - 1:
                    continue
            max_pre = operators_dict[operand][0]
            opr = operand
            index = i
    if open_brackets:
        return '0', -1
    return opr, index


def is_op(exp: str) -> bool:
    '''
    function receives expression. if expression is operand, return True. Else, return False.
    :param exp: str
    :return: if operand, return True. Else, return False.
    '''
    return exp.isnumeric()


def build_expression_tree(expTree: BinaryTree) -> BinaryTree:
    '''
    function receives tree with expression at its root, the function turns tree into expression tree
    :param expTree: BinaryTree
    :return: expression Binary Tree
    '''
    if is_op(repr(expTree)) or check_neg_num(repr(expTree)):
        expTree.set_node(check_minus(repr(expTree)))
    else:
        left_exp, right_exp, operator = slice_equ(repr(expTree))
        if operator != '0':
            if get_dict_val(operator)[1] == 'r':
                expTree.set_node(operator)
                expTree.set_left(BinaryTree.Tree(left_exp))
                build_expression_tree(expTree.get_left())
            elif get_dict_val(operator)[1] == 'l' or left_exp =='U':
                expTree.set_node(operator)
                expTree.set_right(BinaryTree.Tree(right_exp))
                build_expression_tree(expTree.get_right())
            else:
                expTree.set_node(operator)
                expTree.set_left(BinaryTree.Tree(left_exp))
                expTree.set_right(BinaryTree.Tree(right_exp))
                build_expression_tree(expTree.get_left())
                build_expression_tree(expTree.get_right())
        else:
            print("error : invalid expression.")
            return


def is_unary(operator: str):
    return get_dict_val(operator)[1] != 'm'


def is_opr(expression: str) -> bool:
    return expression in operators_dict.keys()


def check_two_opr(opr1: str, opr2: str) -> bool:
    dir1 = get_dict_val(opr1)[1]
    dir2 = get_dict_val(opr2)[1]
    if dir1 == 'm' and dir2 == 'm' and opr2 != '-':
        return False
    if dir1 == 'r' and dir2 == 'l':
        return False
    if dir1 == 'l' and dir2 == 'r':
        return False
    if dir1 == 'l' and dir2 == 'l':
        return False
    if dir1 == 'm' and dir2 == 'r':
        return False
    if dir1 == 'l' and dir2 == 'm' and opr2 != '-':
        return False
    return True


def check_order(expression: str) -> bool:
    if is_opr(expression[0]):
        if expression[0] not in ['-', '~']:
            return False
        else:
            for ch in expression[1:len(expression)]:
                if not is_op(ch) and ch != '(':
                    if ch != '-':
                        return False
                else:
                    break

    if is_opr(expression[len(expression)-1]):
        if expression[len(expression)-1] not in ['!', '#']:
            return False

    for i in range(1, len(expression)-2):
        first_ch = expression[i]
        second_ch = expression[i+1]

        if is_opr(first_ch) and is_opr(second_ch):
            if check_two_opr(first_ch, second_ch) is False:
                return False


def get_dict_val(operator: str) -> tuple or None:
    if operator in operators_dict.keys():
        return operators_dict[operator]
    else:
        return


def slice_equ(equation: str) -> tuple:
    '''
    function receives str of mathematical expression, find the lowest precedence and slices the expression
    into two expression separated by the lowest precedence symbol
    :param equation: str
    :return: tuple with the two new expression and the operator in between
    '''
    equation = adjust_brackets(equation.replace(" ", ""))
    if check_validity(equation) is False:
        print("invalid characters in expression .")
        return 0, 0, '0'
    if check_order(equation) is False:
        print("invalid operators order.")
        return 0, 0, '0'
    equ1 = ""
    equ2 = ""
    index = 0
    operands = get_all_operands(equation)
    if operands:
        first_opr, index = get_lowest_priority(operands)
        if first_opr == '0':
            print("invalid expression : invalid brackets")
            return 0, 0, '0'
        elif first_opr == '-' and is_opr(equation[index-1]):
            equ2 = equation[1:len(equation)]
            equ1 = "U"
        elif get_dict_val(first_opr)[1] == 'm':
            equ1 = equation[0:index]
            equ2 = equation[index+1:len(equation)]
            print("equ1 : ", equ1, "\n", "equ2 : ", equ2)
        elif get_dict_val(first_opr)[1] == 'r':
            equ1 = equation[0:index]
            equ2 = "U"
        elif get_dict_val(first_opr)[1] == 'l':
            equ2 = equation[1:len(equation)]
            equ1 = "U"
        return equ1, equ2, first_opr


def adjust_brackets(equ: str):
    flag = True
    try:
        while equ[0] == '(' and equ[len(equ) - 1] == ')' and flag:
            equ = equ[1:len(equ)-1]
            print(" new equ : ", equ)
    except IndexError:
        return equ

    return equ


def check_minus(exp: str) -> int:
    count = 0
    for i in range(len(exp)):
        if exp[i] == '-':
            count += 1
    number = int(exp[count: len(exp)])
    if count % 2 == 1:
        return 0 - number
    return number


def check_neg_num(exp: str) -> bool:
    if exp[0] == '-' and exp[1] != '(':
        flag = True
        i = 0
        while flag:
            if exp[i] != '-' or i == len(exp) - 1:
                print(i)
                print("len " + str(len(exp)))
                flag = False
            i += 1
        if i != len(exp):
            return False
        elif not is_op(exp[i-1:len(exp)]):
            return False
        else:
            return True
    return False


def sub(op1, op2):
    return op1 - op2

def add(op1, op2):
    return op1 + op2

def mul(op1, op2):
    return op1 * op2

def div(op1, op2):
    if op2 == 0:
        return None
    return op1 / op2

def tilda(op1):
    return 0 - op1

def pow(op1, op2):
    return math.pow(op1, op2)

def avg(op1, op2):
    return (op1 + op2) / 2

def maxi(op1, op2):
    return op1 if op1 > op2 else op2

def mini(op1, op2):
    return op1 if op1 < op2 else op2

def minus_unary(op1):
    return 0 - op1

def modulu(op1, op2):
    return op1 % op2

def factorial(op1):
    result = 1
    if op1 > 0:
        for i in range(1,op1 + 1):
            result *= i
        return result

def sum_digits(op1):
    total = 0
    while op1 != 0:
        total += op1 % 10
        op1 /= 10
    return total


def calculate(expression: BinaryTree) -> float:

    if not expression:
        return 0

    if not expression.get_left() and not expression.get_right():
        return expression.get_data()

    right_expression = calculate(expression.get_right())
    left_expression = calculate(expression.get_left())

    operator = expression.get_data()
    if operator == '-' and not expression.get_left():
        return minus_unary(right_expression)
    elif operator == '-' and expression.get_left():
        return sub(left_expression, right_expression)
    elif operator == '+':
        return add(left_expression, right_expression)
    elif operator == '*':
        return mul(left_expression, right_expression)
    elif operator == '/':
        return div(left_expression, right_expression)
    elif operator == '%':
        return modulu(left_expression, right_expression)
    elif operator == '&':
        return mini(left_expression, right_expression)
    elif operator == '$':
        return maxi(left_expression, right_expression)
    elif operator == '~':
        return tilda(right_expression)
    elif operator == '!':
        return factorial(left_expression)
    elif operator == '#':
        return sum_digits(left_expression)
    elif operator == '@':
        return avg(left_expression, right_expression)
    elif operator == '^':
        return pow(left_expression, right_expression)


def main():
    expression = input("please insert mathematical expression")
    ExpT = BinaryTree.Tree(expression)
    build_expression_tree(ExpT)
    print(calculate(ExpT))
    print("exp tree \n\n\n")
    ExpT.PrintTree()


if __name__ == "__main__":
    main()

