from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

LOWER_LIMIT = 1
UPPER_LIMIT = 100


def generate_round():
    """Generate question-answer pair"""

    # Create random number
    number = randint(LOWER_LIMIT, UPPER_LIMIT)

    # Create answer
    answer = ''
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'

    return number, answer


def is_prime(number):
    """Find out is number is a prime"""

    # 1 is not a prime number
    if number == 1:
        return False
    # 2 is prime number
    if number == 2:
        return True

    # Try to divide the number by all numbers
    # consecutively starting from 2
    # (except 1 and number itself)
    divider = 2
    while divider < number:
        if number % divider == 0:
            return False
        divider += 1
    # There is no other dividers
    return True
