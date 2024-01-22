import operations as do
import BinaryTree
import helpersFunc as helper

def calculate(expression: BinaryTree) -> float:
    if repr(expression) == " ":
        return 0
    if repr(expression).isnumeric() or helper.is_float(repr(expression)):
        data = float(expression.get_data())
        return data

    if expression.get_right():
        right_expression = round(calculate(expression.get_right()),10)
    if expression.get_left():
        left_expression = round(calculate(expression.get_left()), 10)

    operator = repr(expression)

    if operator == '-':
        return do.sub(left_expression, right_expression)
    elif operator == '+':
        return do.add(left_expression, right_expression)
    elif operator == '*':
        return do.mul(left_expression, right_expression)
    elif operator == '/':
        return do.div(left_expression, right_expression)
    elif operator == '%':
        return do.modulu(left_expression, right_expression)
    elif operator == '&':
        return do.mini(left_expression, right_expression)
    elif operator == '$':
        return do.maxi(left_expression, right_expression)
    elif operator == '~':
        return do.tilda(right_expression)
    elif operator == '!':
        return do.factorial(left_expression)
    elif operator == '#':
        return do.sum_digits(left_expression)
    elif operator == '@':
        return do.avg(left_expression, right_expression)
    elif operator == '^':
        return do.power(left_expression, right_expression)


    return repr(expression)