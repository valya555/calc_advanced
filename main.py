import calculation
import BinaryTree
import helpersFunc as helper
import validity as valid
import build_tree
from ErrorsCalc import InputError, FloatError
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
    if (valid.check_validity(expression) and valid.check_order(expression) and
            valid.check_dots(expression) and helper.lowest_priority(expression)[0] != '0'):
        return True
    raise InputError

def menu():
    print("+ : addition\t\t"
          "- : subtraction / negative\t\t"
          "* : multiplication\n"
          "/ : divination\t\t"
          "% : remainder / modulu\t\t"
          "^ : power \n"
          "@ : average \t\t"
          "$ : maximum \t\t"
          "& : minimum \n"
          " ~ : negative\t\t"
          " ! : factorial \t\t"
          " # : sum of digits \n")

def main():
    flag = True
    print("_____________________________________________________")
    print("\n welcome to the advanced calculator ! ~~ ")
    print("\n ____________________________________________________")
    while flag:
        try:
            menu()
            expression_input = input(" insert mathematical expression, to see menu write m : \t")
            expression_input = expression_input.replace(" ", "")
            check_input(expression_input)

            expression_tree = BinaryTree.Tree(expression_input)
            build_tree.build_expression_tree(expression_tree)

            expression_tree.PrintTree()
            print(calculation.calculate(expression_tree))

        except ZeroDivisionError as ZDError:
            print(ZDError)
            print("invalid calculation. please re-enter the expression or choose x to exit.")
        except ArithmeticError as AError:
            print(AError)
            print("invalid calculation. please re-enter the expression or choose x to exit.")
        except InputError as IError:
            print(IError)
            print("invalid expression. please re-enter the expression or choose x to exit.")
        except TypeError as ErrorT:
            print(ErrorT)
            print("invalid expression. please re-enter the expression or choose x to exit.")
        except IndexError as IError:
            if flag:
                print(IError)
                print("invalid input.")
        except FloatError as FError:
            print(FError)


if __name__ == "__main__":
    main()