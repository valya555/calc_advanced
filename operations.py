import math

def sub(op1, op2):
    return op1 - op2

def add(op1, op2):
    return op1 + op2

def mul(op1, op2):
    return op1 * op2

def div(op1, op2):
    if op2 == 0:
        return None
    return op1 / op2

def tilda(op1):
    return 0 - op1

def power(op1, op2):
    return math.pow(op1, op2)

def avg(op1, op2):
    return (op1 + op2) / 2

def maxi(op1, op2):
    return op1 if op1 > op2 else op2

def mini(op1, op2):
    return op1 if op1 < op2 else op2

def minus_unary(op1):
    return 0 - op1

def modulu(op1, op2):
    return op1 % op2

def factorial(op1):
    result = 1
    if op1 > 0:
        for i in range(1,int(op1) + 1):
            result *= i
        return result

def sum_digits(op1):
    op1 = str(op1)
    flag = True
    i = 0
    total = 0
    while flag:
        if i == len(op1) - 1 or op1[i] == 'e':
            flag = False
        if op1[i].isdigit():
            total += float(op1[i])
        i += 1
    return total