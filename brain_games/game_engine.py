import prompt
import brain_games.games.brain_prime
import brain_games.games.brain_calc
import brain_games.games.brain_even
import brain_games.games.brain_gcd
import brain_games.games.brain_progression


rules = {
    'brain-even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'brain-gcd': 'Find the greatest common divisor of given numbers.',
    'brain-calc': 'What is the result of the expression?',
    'brain-progression': 'What number is missing in the progression?',
    'brain-prime': 'Answer "yes" if given number is prime. Otherwise answer "no".',
}


def game_engine(game):
    """Greet user. Print rules.
    Ask question 3 times. Compare answer with user guess,
    if answer is correct, then ask again.
    If answer is incorrect game is over.
    """

    # Greet user
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    # Print rules
    print(f'{rules[game]}')

    # What game would be playing
    if game == 'brain-prime':
        get_round = brain_games.games.brain_prime.generate_round
    elif game == 'brain-calc':
        get_round = brain_games.games.brain_calc.generate_round
    elif game == 'brain-even':
        get_round = brain_games.games.brain_even.generate_round
    elif game == 'brain-gcd':
        get_round = brain_games.games.brain_gcd.generate_round
    elif game == 'brain-progression':
        get_round = brain_games.games.brain_progression.generate_round


    index = 0
    while index < 3:

        round = get_round()
        question = round[0]
        answer = round[1]

        # Ask user a question
        print(f'Question: {question}')

        # Prompt user for a guess
        guess = input('Your answer: ').strip()

        # Copmare user guess and answer
        if answer == guess:
            print('Correct!')
            index += 1
        else:
            print(f"'{guess}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break

    # User gave 3 correct answer
    if index == 3:
        print(f'Congratulations, {name}!')


def main():
    game = 'brain-prime'
    game_engine(game)


if __name__ == '__main__':
    main()
