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
    if is_op(repr(expTree)):
        expTree.set_node(int(repr(expTree)))
    else:
        left, right, operator = slice_equ(repr(expTree))
        if operator != '0':
            expTree.set_node(operator)
            expTree.set_left(BinaryTree.Tree(left))
            expTree.set_right(BinaryTree.Tree(right))
            build_expression_tree(expTree.get_left())
            build_expression_tree(expTree.get_right())
        else:
            print("error : invalid expression.")
            return


def is_opr(expression: str) -> bool:
    return expression in operators_dict.keys()


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
    equ1 = ""
    equ2 = ""
    index = 0
    operands = get_all_operands(equation)
    if operands:
        first_opr, index = get_lowest_priority(operands)
        if first_opr == '0':
            print("invalid expression : invalid brackets")
            return 0, 0, '0'
        else:
            equ1 = equation[0:index]
            equ2 = equation[index+1:len(equation)]
            print("equ1 : ", equ1, "\n", "equ2 : ", equ2)
        return equ1, equ2, first_opr


def adjust_brackets(equ: str):
    while equ[0] == '(' and equ[len(equ) - 1] == ')':
        equ = equ[1:len(equ)-1]
        print(" new equ : ", equ)
    return equ


def main():
    expression = input("please insert mathematical expression")
    ExpT = BinaryTree.Tree(expression)
    build_expression_tree(ExpT)
    print("exp tree \n\n\n")
    ExpT.PrintTree()


if __name__ == "__main__":
    main()

