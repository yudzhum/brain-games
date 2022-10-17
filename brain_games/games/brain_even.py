from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

LOWER_LIMIT = 0
UPPER_LIMIT = 100


def generate_round():
    """Generate question-answer pair"""

    # Create random number
    number = randint(LOWER_LIMIT, UPPER_LIMIT)

    # Check if number is even and assign answer
    answer = 'yes' if number % 2 == 0 else 'no'

    return number, answer
