import calculation
import BinaryTree
import helpersFunc as helper
import validity as valid
import build_tree

#operators_dict = helper.operators_dictionary()


def check_input(expression: str) -> bool:
    '''
    function checks if input received in valid:
    the function is separate from other validity checks since if the checks in this function
    are valid, there is no need to check the inheriting expressions, they are valid too.
    :param expression: str
    :return: return True if function is valid in terms of brackets, operators order and all chars are valid.
    '''
    print(valid.check_validity(expression))
    print(valid.check_order(expression))
    print(helper.lowest_priority(expression)[0])
    if valid.check_validity(expression) and valid.check_order(expression) and helper.lowest_priority(expression)[0] != '0':
        return True
    return False


def main():
    expression_input = input(" insert mathematical expression : \t")
    expression_input = expression_input.replace(" ", "")
    validity_flag = check_input(expression_input)
    if validity_flag is False:
        print("invalid input")
        return

    expression_tree = BinaryTree.Tree(expression_input)
    build_tree.build_expression_tree(expression_tree)

    if expression_tree is None:
        print("error building tree")
        return

    expression_tree.PrintTree()
    print(calculation.calculate(expression_tree))

if __name__ == "__main__":
    main()