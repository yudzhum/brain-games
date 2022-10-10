from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint


def create_questions():
    """Create list of 3 random numbers"""
    questions = []

    index = 0
    while index < 3:

        # Create random number in range 0 to 100
        number = randint(0, 100)
        questions.append(number)

        index += 1

    return questions


def create_answers(questions):
    """Create dictionary of 3 question-answer pairs"""
    puzzles = {}

    index = 0
    while index < 3:

        # Check if number is even and assign answer
        answer = ''
        if questions[index] % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'

        puzzles.update({questions[index]: answer})

        index += 1

    return puzzles


def brain_even():
    # Greet user
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # Cteate questions and answer
    questions = create_questions()
    puzzles = create_answers(questions)

    # Play game
    game_engine(name, puzzles)


def main():
    brain_even()


if __name__ == '__main__':
    main()
