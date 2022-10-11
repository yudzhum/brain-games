from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint, choice
from operator import add, sub, mul


def create_puzzles():
    puzzles = {}

    index = 0
    while index < 3:

        operand1 = randint(0, 100)
        operand2 = randint(0, 100)

        operator = choice('+-*')

        question = (f'{operand1} {operator} {operand2}')

        answer = str(find_answer(operand1, operator, operand2))

        puzzles.update({question: answer})

        index += 1

    return puzzles


def find_answer(operand1, operator, operand2):
    operators = {
        '+': add(operand1, operand2),
        '-': sub(operand1, operand2),
        '*': mul(operand1, operand2),
    }

    return operators[operator]


def brain_calc():
    # Greet user
    name = greeting()
    print('What is the result of the expression?')

    # Cteate questions and answer
    puzzles = create_puzzles()

    # Play game
    game_engine(name, puzzles)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
