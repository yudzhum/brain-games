def game_engine(name, puzzles):
    """Ask question 3 times. Compare answer with user guess,
    if answer is correct, then ask again.
    If answer is incorrect game is over
    Function take for input 2 arguments.
    Name of user and dictionary of questions and answers
    """

    for question, answer in puzzles.items():

        # Ask user a question
        print(f'Question: {question}')

        # Prompt user for a guess
        guess = input('Your answer: ').strip()

        # Copmare user guess and answer
        if answer == guess:
            print('Correct!')
        else:
            print(f"'{guess}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break

        # User gave 3 correct answer
        print(f'Congratulations, {name}!')
