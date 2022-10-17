from random import randint


DESCRIPTION = 'What number is missing in the progression?'

LOWER_LIMIT = 1
UPPER_LIMIT = 100
PROGRESSION_LENGTH = 10

LOWER_STEP_LIMIT = 1
UPPER_STEP_LIMIT = 10


def generate_progression():
    """Generate arithmetic progression"""

    # Create the first term in the sequence
    first_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    # Create the common difference between terms
    step = randint(LOWER_STEP_LIMIT, UPPER_STEP_LIMIT)
    count = 0

    # Create range of numbers, then add difference (d) by formula
    progression = []
    for number in range(first_number, first_number + PROGRESSION_LENGTH):
        num = number + step * count
        progression.append(num)
        count += 1

    return progression


def generate_round():
    """Generate question-answer pair"""

    progression = generate_progression()

    # Choose number to hide randomly
    hidden = randint(LOWER_LIMIT, len(progression) - 1)
    # Take answer
    answer = str(progression[hidden])
    # Hide element
    progression[hidden] = '..'

    question = ' '.join([str(x) for x in progression])

    return question, answer
