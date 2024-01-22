import helpersFunc as helper
from ErrorsCalc import FloatError

operators_dict = helper.operators_dictionary()


def check_validity(expression: str) -> bool:
    '''
    the function checks if the given expression only has operands , operators and brackets
    :param expression: str
    :return: if expression is valid, return True. else return False.
    '''
    for current_char in expression:
        if current_char != "." and current_char not in operators_dict.keys() and not current_char.isnumeric() and current_char not in ['(', ')']:
            print("check validity")
            return False
    return True



def check_two_opr(opr1: str, opr2: str) -> bool:
    side1 = helper.side(opr1)
    side2 = helper.side(opr2)
    if side1 == 'm' and side2 == 'm' and opr2 != '-':
        print("check two opr 1")
        return False
    if side1 == 'r' and side2 == 'l':
        print("check two opr 2")
        return False
    if side1 == 'l' and side2 == 'r':
        print("check two opr 3")
        return False
    if side1 == 'l' and side2 == 'l':
        print("check two opr 4")
        return False
    if side1 == 'm' and side2 == 'r':
        print("check two opr 5")
        return False
    if side1 == 'l' and side2 == 'm' and opr2 != '-':
        print("check two opr 6")
        return False
    return True


def check_order(expression: str) -> bool:
    if helper.is_operator(expression[0]):
        if helper.side(expression[0]) != 'l':
            if expression[0] != '-' :
                print("check order 0")
                return False
        else:
            for ch in expression[1:len(expression)]:
                if not helper.is_operand(ch) and ch != '(':
                    if ch != '-':
                        print("check order 1")
                        return False
                else:
                    break

    if helper.is_operator(expression[len(expression)-1]):
        if helper.side(expression[len(expression)-1]) != 'r':
            print("check order 2")
            return False

    for i in range(len(expression) - 2):
        first_ch = expression[i]
        second_ch = expression[i+1]
        if helper.is_operator(first_ch) and helper.is_operator(second_ch):
            if check_two_opr(first_ch, second_ch) is False:
                print("check order 3")
                return False
    return True


def operators_with_dots_list(expression: str) -> list:
    operators = []
    index = 0
    for current_char in expression:
        if current_char in operators_dict.keys() or current_char in ['(', ')'] or current_char == ".":
            operators.append((current_char, index))
        index += 1
    return operators


def check_dots(expression: str):
    operators_and_dots = operators_with_dots_list(expression)
    if expression[0] =="." or expression[len(expression)-1] == ".":
        raise FloatError
    for i in range(len(operators_and_dots) - 2):
        if operators_and_dots[i] == "." and operators_and_dots[i+1] == ".":
            raise FloatError

    for i in range(len(expression) - 3):
        if expression[i+1] == ".":
            if not expression[i].isnumeric() or not expression[i+2].isnumeric():
                raise FloatError
    return True