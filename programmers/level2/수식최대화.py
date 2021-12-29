from itertools import permutations
import re

def solution(expression):
    operands = []
    numbers = []
    answers = []

    expression = re.split(r'(\D)',expression)

    for ex in expression:
        operands.append(ex) if ex in ['+', '-', '*'] else numbers.append(ex)

    for operand in list(permutations(set(operands))): 
        operands_copy = operands[:]
        numbers_copy = numbers[:]

        for op in operand:
            while op in operands_copy:
                a = numbers_copy.pop(operands_copy.index(op))
                b = numbers_copy.pop(operands_copy.index(op))

                numbers_copy.insert(operands_copy.index(op), str(eval(a+op+b)))
                operands_copy.pop(operands_copy.index(op))
        
        answers.append(abs(int(numbers_copy[0])))
     
    return max(answers)