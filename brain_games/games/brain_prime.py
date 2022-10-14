from random import randint


def generate_round():
    """Generate question-answer pair"""

    # Create random number
    number = randint(1, 100)

    # Create answer
    answer = str(get_answer(number))

    return number, answer


def get_answer(number):
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


def main():
    round = generate_round()
    print(f'{round}')


if __name__ == '__main__':
    main()
