from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint, choice
from operator import add, sub, mul


def create_questions():
    """Create list of math expressions"""
    questions = []

    index = 0
    while index < 3:

        operand1 = randint(0, 100)
        operand2 = randint(0, 100)

        operator = choice('+-*')

        questions.append(f'{operand1} {operator} {operand2}')

        index += 1

    return questions


def create_answers(questions):
    """Create dictionary of questions-answers pairs"""
    puzzles = {}

    index = 0
    while index < 3:
        operand1, operator, operand2 = questions[index].split(' ')

        operand1 = int(operand1)
        operand2 = int(operand2)

        operators = {
            '+': add(operand1, operand2),
            '-': sub(operand1, operand2),
            '*': mul(operand1, operand2),
        }

        answer = str(operators[operator])

        puzzles.update({questions[index]:answer})

        index += 1

    return puzzles


def brain_calc():
    # Greet user
    name = greeting()
    print('What is the result of the expression?')

    # Cteate questions and answer
    questions = create_questions()
    puzzles = create_answers(questions)

    # Play game
    game_engine(name, puzzles)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
