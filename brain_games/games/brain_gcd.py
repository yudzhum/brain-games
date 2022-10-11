from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint


def create_puzzles():
    """Create dictionary of 3 question-answer pairs"""
    puzzles = {}

    index = 0
    while index < 3:

        # Create question
        number1 = randint(1, 100)
        number2 = randint(1, 100)

        question = (f'{number1} {number2}')

        # Create answer
        answer = str(find_gcd(number1, number2))

        # Update dictionary
        puzzles.update({question: answer})

        index += 1

    return puzzles


def find_gcd(number1, number2):
    """"Find greatest common divider"""

    smallest = min(number1, number2)
    biggest = max(number1, number2)

    # Find a greatest common divider
    div_of_smallest = [x for x in range(1, smallest + 1) if smallest % x == 0]

    div_of_biggest = [x for x in div_of_smallest if biggest % x == 0]

    return max(div_of_biggest)


def brain_gcd():
    # Greet user
    name = greeting()
    print('Find the greatest common divisor of given numbers.')

    # Cteate questions and answer
    puzzles = create_puzzles()

    # Play game
    game_engine(name, puzzles)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
