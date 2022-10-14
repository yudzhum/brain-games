from random import randint


def generate_progression():
    """Generate arithmetic progression"""

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

    return progression


def generate_round():
    """Generate question-answer pair"""

    progression = generate_progression()

    # Choose number to hide randomly
    hidden = randint(2, 9)
    # Take answer
    answer = str(progression[hidden])
    # Hide element
    progression[hidden] = '..'

    question = ' '.join([str(x) for x in progression])

    return question, answer


def main():
    round = generate_round()
    print(f'{round}')


if __name__ == '__main__':
    main()
