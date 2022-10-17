from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'

LOWER_LIMIT = 1
UPPER_LIMIT = 100


def generate_round():
    """Generate question-answer pair"""

    # Create question
    number1 = randint(LOWER_LIMIT, UPPER_LIMIT)
    number2 = randint(LOWER_LIMIT, UPPER_LIMIT)

    question = (f'{number1} {number2}')

    # Create answer
    answer = str(find_gcd(number1, number2))

    return question, answer


def find_gcd(number1, number2):
    """"Find greatest common divider"""

    smallest = min(number1, number2)
    biggest = max(number1, number2)

    # Find a greatest common divider
    div_of_smallest = [x for x in range(1, smallest + 1) if smallest % x == 0]

    div_of_biggest = [x for x in div_of_smallest if biggest % x == 0]

    return max(div_of_biggest)
