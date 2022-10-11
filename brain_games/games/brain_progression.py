from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint


def create_progressions():
    """Create list of 3 arithmetic progressions"""
    progressions = []
    index = 0

    while index < 3:

        # Create the first term in the sequence
        first_number = randint(1, 100)
        # Create the common difference between terms
        step = randint(1, 10)
        count = 0

        # Create range of numbers, then add difference (d) by formula
        progression = []
        for number in range(first_number, first_number + 10):
            num = number + step * count
            progression.append(num)
            count += 1

        progressions.append(progression)

        index += 1

    return progressions


def create_puzzles(progessions):
    """Create dictionary of question-answer pairs"""
    puzzles = {}

    for progression in progessions:
        # Choose number to hide randomly
        hidden = randint(2, 9)
        # Take answer
        answer = progression[hidden]
        # Hide element
        progression[hidden] = '..'

        question = ' '.join([str(x) for x in progression])

        puzzles.update({question: str(answer)})

    return puzzles


def brain_progression():
    """PLay game of brain progression"""

    # Greet user
    name = greeting()
    print('What number is missing in the progression?')

    # Create questions and answer
    progressions = create_progressions()
    puzzles = create_puzzles(progressions)

    # Play game
    game_engine(name, puzzles)


def main():
    brain_progression()


if __name__ == '__main__':
    main()
