from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'

LOWER_LIMIT = 0
UPPER_LIMIT = 100


def generate_round():
    """Generate question-answer pair"""

    # Create 2 random numbers and operator
    operand1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    operand2 = randint(LOWER_LIMIT, UPPER_LIMIT)

    operator = choice('+-*')

    # Make a question
    question = (f'{operand1} {operator} {operand2}')

    # Make an answer
    answer = str(calc(operand1, operator, operand2))

    return question, answer


def calc(operand1, operator, operand2):
    """Find result of math expressions and return it"""
    operators = {
        '+': add(operand1, operand2),
        '-': sub(operand1, operand2),
        '*': mul(operand1, operand2),
    }

    return operators[operator]
