
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


def operators_dictionary() -> dict:
    return operators_dict


def is_operator(operator: str) -> bool:
    return operator in operators_dict.keys()


def is_operand(operand: str) -> bool:
    '''
    function receives expression. if expression is operand, return True. Else, return False.
    :param operand: str
    :return: if operand, return True. Else, return False.
    '''
    return operand.isnumeric()


def precedence(operator: str) -> str:
    return operators_dict[operator][0]


def side(operator: str) -> str:
    return operators_dict[operator][1]


def operators_list(expression: str) -> list:
    operators = []
    index = 0
    for current_char in expression:
        if current_char in operators_dict.keys() or current_char in ['(', ')']:
            operators.append((current_char, index))
        index += 1
    return operators


def lowest_priority(expression: str) -> tuple:
    '''
    function receives list of operators as they appear in a mathematical expression,
    returns the operator with the lowest precedence and its index in the expression.
    :param operators: list
    :return: if the function is valid in terms of brackets, return the lowest precedence operator and its index.
    else, return 0 and -1 to indicate error
    '''
    operators = operators_list(expression)
    highest_precedence = 6
    lowest_index = 0
    lowest_operator = operators[0][0]
    open_brackets = []
    for operator, i in operators:
        if operator == '(':
            open_brackets.append(operator)
        if operator == ')':
            if not open_brackets:
                return '0', -1
            if open_brackets:
                open_brackets.pop()
        if operator not in [')', '('] and precedence(operator) <= highest_precedence and not open_brackets:
            if operator == '-':
                if i == 0 or is_operator(expression[i - 1]):
                    continue
            highest_precedence = precedence(operator)
            lowest_operator = operator
            lowest_index = i
    if open_brackets:
        return '0', -1
    return lowest_operator, lowest_index


def adjust_brackets(expression: str) -> str:
    brackets = []
    if expression[0] == '(' and expression[len(expression) - 1] == ')':
        for i in range(1, len(expression) - 1):
            if expression[i] == '(':
                brackets.append(expression[i])
            if expression[i] == ')':
                if brackets:
                    brackets.pop()
                else:
                    return expression

        return expression[1: len(brackets) - 1]
    else:
        return expression


def check_unary_minus(expression: str, index_of_minus: int) -> bool:
    '''

    :param expression:
    :param index_of_minus:
    :return: True if unary minus,else False
    '''
    return index_of_minus == 0 or is_operator(expression[index_of_minus - 1])