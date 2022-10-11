from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint


def create_puzzles():
    """Create dictionary of 3 question-answer pairs"""
    puzzles = {}

    index = 0
    while index < 3:
        # Create random number
        number = randint(1, 100)

        # Create answer
        answer = str(isprime(number))

        # Update dictionary
        puzzles.update({str(number): answer})

        # Update count
        index += 1

    return puzzles


def isprime(number):
    """Find out is number is a prime"""

    # 1 is not a prime number
    if number == 1:
        return 'no'
    # 2 is prime number
    if number == 2:
        return 'yes'

    # Try to divide the number by all numbers
    # consecutively starting from 2
    # (except 1 and number itself)
    divider = 2
    while divider < number:
        if number % divider == 0:
            return 'no'
        divider += 1
    # There is no other dividers
    return 'yes'


def brain_prime():
    """Play brain-prime game"""

    # Greet user
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    # Create questions and answers
    puzzles = create_puzzles()

    # Play game
    game_engine(name, puzzles)


def main():
    brain_prime()


if __name__ == '__main__':
    main()
