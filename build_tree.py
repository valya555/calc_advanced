import BinaryTree
import helpersFunc as helper
import ErrorsCalc


def build_expression_tree(expTree: BinaryTree) -> BinaryTree:
    '''
    function receives tree with expression at its root, the function turns tree into expression tree
    :param expTree: BinaryTree
    :return: expression Binary Tree
    '''
    if helper.is_operand(repr(expTree)) or repr(expTree) == " " or helper.is_float(repr(expTree)):
        expTree.set_node(repr(expTree))
    else:
        left_exp, right_exp, operator = divide_expression(repr(expTree))
        if operator != '0':
            if helper.side(operator) == 'r':
                expTree.set_node(operator)
                expTree.set_left(left_exp)
                build_expression_tree(expTree.get_left())
            elif helper.side(operator) == 'l':
                expTree.set_node(operator)
                expTree.set_right(right_exp)
                build_expression_tree(expTree.get_right())
            else:
                expTree.set_node(operator)
                expTree.set_left(left_exp)
                expTree.set_right(right_exp)
                build_expression_tree(expTree.get_left())
                build_expression_tree(expTree.get_right())
        else:
            print("error : invalid expression.")
            raise ErrorsCalc.InputError



def divide_expression(expression: str) -> tuple:
    '''
    function receives str of mathematical expression, find the lowest precedence and slices the expression
    into two expression separated by the lowest precedence symbol
    :param expression: str
    :return:
    '''

    expression = helper.adjust_brackets(expression).replace(" ", "")
    left_exp, right_exp = " ", " "
    first_operator, index = helper.lowest_priority(expression)
    # checking for unary minus
    if first_operator == '-' and helper.check_unary_minus(expression, index):
        left_exp = 0
        right_exp = expression[1:len(expression)]
    elif helper.side(first_operator) == 'm':
        left_exp = expression[0:index]
        right_exp = expression[index + 1:len(expression)]
    elif helper.side(first_operator) == 'r':
        left_exp = expression[0:index]
        right_exp = " "
    elif helper.side(first_operator) == 'l':
        left_exp = " "
        right_exp = expression[1:len(expression)]
    return left_exp, right_exp, first_operator

