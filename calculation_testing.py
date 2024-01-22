import pytest
import calculation
from ErrorsCalc import FloatError, InputError
import BinaryTree as t
@pytest.mark.parametrize("expression, result",
                         [
                             (t.Tree("5 + 4 * 3"), 17.0),
                                 (t.Tree("7 / 8 + 8 % 7"), 1.875),
                                 (t.Tree("( 5 @ 7 ) $ 13"), 13),
                                 (t.Tree("2&-(5+4)"), -9),
                                 (t.Tree("( 5 ^ 2 ) #"), 7),
                                 (t.Tree("~-7! "), 5040.0),
                                 (t.Tree("17 - 20 & 10"), 7.0),
                                 (t.Tree("50 % 13 @ 40"), 23.5),
                                (t.Tree("5!# % 4 ^ 7 / 8 + ( 9 $ ~--- 12)"), 285.375),
                                (t.Tree("(165 / 96 % 5 ) @ 18 ^ 2"),8372.25)
                         ])


def tester(expression, result):
    assert calculation.calculate(expression) == result

def test_space():
    with pytest.raises(InputError) as e_info:
        calculation.calculate(t.Tree(" "))

def test_syntax():
    with pytest.raises(Exception):
        calculation.calculate(t.Tree("5*^3"))


