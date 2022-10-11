def game_engine(name, puzzles):
    """Ask question 3 times. Compare answer with user guess,
    if answer is correct, then ask again.
    If answer is incorrect game is over
    Function take for input 2 arguments.
    Name of user and dictionary of questions and answers
    """
    count = 0
    for question, res in puzzles.items():

        # Ask user a question
        print(f'Question: {question}')

        # Prompt user for a guess
        guess = input('Your answer: ').strip()

        # Copmare user guess and answer
        if res == guess:
            print('Correct!')
            count += 1
        else:
            print(f"'{guess}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f'Let\'s try again, {name}!')
            break

    # User gave 3 correct answer
    if count == 3:
        print(f'Congratulations, {name}!')
