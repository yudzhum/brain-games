from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint, choice
from operator import add, sub, mul


def create_puzzles():
    """Create dictionary of 3 question-answer pairs"""
    puzzles = {}

    index = 0
    while index < 3:

        # Create 2 random numbers and operator
        operand1 = randint(0, 100)
        operand2 = randint(0, 100)

        operator = choice('+-*')

        # Make a question
        question = (f'{operand1} {operator} {operand2}')

        # Make an answer
        answer = str(find_answer(operand1, operator, operand2))

        # Updetae dictionary
        puzzles.update({question: answer})

        index += 1

    return puzzles


def find_answer(operand1, operator, operand2):
    """Find result of math expressions and return it"""
    operators = {
        '+': add(operand1, operand2),
        '-': sub(operand1, operand2),
        '*': mul(operand1, operand2),
    }

    return operators[operator]


def brain_calc():
    """Play game of calculation"""

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
