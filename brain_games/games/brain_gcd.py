from brain_games.greeting import greeting
from brain_games.game_engine import game_engine
from random import randint


def create_questions():
    """Create 3 pairs of numbers"""
    questions = []

    index = 0
    while index < 3:

        number1 = randint(1, 100)
        number2 = randint(1, 100)

        questions.append(f'{number1} {number2}')

        index += 1

    return questions


def create_answers(questions):
    """Create dictionary of 3 question-answer pairs"""
    puzzles = {}

    index = 0
    while index < 3:

        # EXtract biggest and smallest numbers from a string
        num1, num2 = questions[index].split(' ')
        smallest = min(int(num1), int(num2))
        biggest = max(int(num1), int(num2))

        # Find a greatest common divider
        div_of_smallest = [x for x in range(1, smallest + 1) if smallest % x == 0]

        div_of_biggest = [x for x in div_of_smallest if biggest % x == 0]

        divider = str(max(div_of_biggest))

        # Update dictionary
        puzzles.update({questions[index] : divider})

        index += 1

    return puzzles


def brain_gcd():
    # Greet user
    name = greeting()
    print('Find the greatest common divisor of given numbers.')

    # Cteate questions and answer
    questions = create_questions()
    puzzles = create_answers(questions)

    # Play game
    game_engine(name, puzzles)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
