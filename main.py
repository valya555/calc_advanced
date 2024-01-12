

operands_dict = {
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


def check_validity(equation: str) -> bool:
    '''
    the function checks if the given expression only has operands , operators and brackets
    :param equation: str
    :return: if expression is valid, return True. else return False.
    '''
    for current_char in equation:
        if current_char not in operands_dict.keys() and not current_char.isnumeric() and current_char not in ['(', ')']:
            return False
    return True


def get_all_operands(equ: str) -> list:
    operands_list = []
    for current_char in equ:
        if current_char in operands_dict.keys() or current_char in ['(', ')']:
            operands_list.append(current_char)
    return operands_list

def get_lowest_priority(operands: list) -> str:
    max = 6
    opr = operands[0]
    open_brackets = []
    for operand in operands:
        if operand == '(':
            open_brackets.append(operand)
        if operand == ')':
            if not open_brackets:
                return '0'
            if open_brackets:
                open_brackets.pop()
        if operand not in [')', '('] and operands_dict[operand][0] < max and not open_brackets:
            max = operands_dict[operand][0]
            opr = operand
    return opr



def calculate(equation: str):
    equ1 = ""
    equ2 = ""
    operands = get_all_operands(equation)
    first_opr = get_lowest_priority(operands)
    print(first_opr)
    if first_opr == '0':
        print("invalid expression : invalid brackets")
        return False


def main():
    expression = input("please insert mathematical expression")
    calculate(expression)

if __name__ == "__main__":
    main()

