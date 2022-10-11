from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint


def create_puzzles():
    """Create dictionary of 3 question-answer pairs"""
    puzzles = {}

    index = 0
    while index < 3:

        # Create random number
        number = randint(0, 100)

        # Check if number is even and assign answer
        answer = find_answer(number)

        # Update dictionary
        puzzles.update({number: answer})

        index += 1

    return puzzles


# Check if number is even and return answer
def find_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def brain_even():
    # Greet user
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # Cteate questions and answer
    puzzles = create_puzzles()

    # Play game
    game_engine(name, puzzles)


def main():
    brain_even()


if __name__ == '__main__':
    main()
