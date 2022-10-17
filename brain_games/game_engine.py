import prompt


START_SCORE = 0
MAX_SCORE = 3


def run_game(game):
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
    print(f'{game.DESCRIPTION}')

    score = START_SCORE
    for _ in range(START_SCORE, MAX_SCORE):

        # Get game round
        question, answer = game.generate_round()

        # Ask user a question
        print(f'Question: {question}')

        # Prompt user for a guess
        guess = input('Your answer: ').strip()

        # Copmare user guess and answer
        if answer == guess:
            print('Correct!')
            score += 1
        else:
            print(f"'{guess}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break

    # User gave 3 correct answer
    if score == MAX_SCORE:
        print(f'Congratulations, {name}!')
