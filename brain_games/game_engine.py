def game_engine(name):
    """Ask question 3 times. Compare answer with user guess,
    if answer is correct, then ask again. 
    If answer is incorrect game is over
    Usage: function work with 2 other functions:
    create_question and create_answer
    """

    count = 0
    while count < 3:

        # Ask user a question
        question = create_question()
        print(f'Question: {question}')

        # Prompt user for a guess
        guess = input('Your answer: ').strip()

        # Calculate an answer
        answer = create_answer(question)

        # Copmare user guess and answer
        if answer == guess:
            print('Correct!')
        else:
            print(f"'{guess}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break

        count += 1

    # User gave 3 correct answer
    if count == 3:
        print(f'Congratulations, {name}!')

