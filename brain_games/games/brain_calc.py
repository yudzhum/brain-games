from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint, choice
from operator import add, sub, mul


def create_question():
    operand1 = randint(0, 100)
    operand2 = randint(0, 100)

    operator - choice('+-*')

    return (f'{operand1} {operator} {operand2}')


def create_answer(question):
    operand1, operator, operand2 = question.split(' ')

    operand1 = int(operand1)
    operand2 = int(operand2)

    operators = {
    '+': add(operand1, operand2),
    '-': sub(operand1, operand2),
    '*': mul(operand1, operand2),
    }

    return str(operators[operator])


def brain_calc():
    name = greeting()
    print('What is the result of the expression?')

    game_engine(name)


def main():
    print('rrr')
    brain_calc()


if __name__ == '__main__':
    main()