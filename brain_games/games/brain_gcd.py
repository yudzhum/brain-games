from random import randint


def generate_round():
    """Generate question-answer pair"""

    # Create question
    number1 = randint(1, 100)
    number2 = randint(1, 100)

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


def main():
    round = generate_round()
    print(f'{round}')


if __name__ == '__main__':
    main()
