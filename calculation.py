import operations as do
import BinaryTree

def calculate(expression: BinaryTree) -> float:
    if not expression:
        return
    if repr(expression) == " ":
        return 0
    if repr(expression).isnumeric():
        data = float(expression.get_data())
        return data

    if expression.get_right():
        right_expression = calculate(expression.get_right())
    if expression.get_left():
        left_expression = calculate(expression.get_left())

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