from random import randint


def generate_round():
    """Generate question-answer pair"""

    # Create random number
    number = randint(0, 100)

    # Check if number is even and assign answer
    answer = find_answer(number)

    return number, answer


# Check if number is even and return answer
def find_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def main():
    round = generate_round()
    print(f'{round}')


if __name__ == '__main__':
    main()
