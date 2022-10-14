from random import randint, choice
from operator import add, sub, mul


def generate_round():
    """Generate question-answer pair"""

    # Create 2 random numbers and operator
    operand1 = randint(0, 100)
    operand2 = randint(0, 100)

    operator = choice('+-*')

    # Make a question
    question = (f'{operand1} {operator} {operand2}')

    # Make an answer
    answer = str(find_answer(operand1, operator, operand2))

    return question, answer


def find_answer(operand1, operator, operand2):
    """Find result of math expressions and return it"""
    operators = {
        '+': add(operand1, operand2),
        '-': sub(operand1, operand2),
        '*': mul(operand1, operand2),
    }

    return operators[operator]


def main():
    round = generate_round()
    print(f'{round}')


if __name__ == '__main__':
    main()
