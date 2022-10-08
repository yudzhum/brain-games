from random import randint
import prompt


def greeting():
    """Ask name and greet user"""

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def check_answer(number, answer):
    """ Take number, check if it is even,
    compare with user answer and return result 
    """

    # Check if number is even
    even = ''
    if number % 2 == 0:
        even = 'yes'
    else:
        even = 'no'

    # Validate user answer and result result
    if even == answer:
        return 'Correct!'
    else:
        return f"'{answer}' is wrong answer ;(. Correct answer was '{even}'."


def game_engine():
    """ Show user random number.
    Answer "yes" if the number is even, otherwise answer "no".
    Play three times if answers is correct ones.
    Otherwise the game is over
    """

    # Greet user
    name = greeting()

    # Ask user question 3 times
    count = 0
    while count < 3:

        #Create random number
        number = randint(0, 100)

        # Ask question
        print(f'Question: {number}')
        answer = input('Your answer: ').strip()
    
        # Validate answer
        result = check_answer(number, answer)
        print(result)
    
        # User gave wrong answer
        if result != 'Correct!':
            print(f'Let\'s try again, {name}!')
            break

        count += 1
    
    # User gave 3 correct answers
    if count == 3:
        print(f'Congratulations, {name}!')
  

# Play game
def main():
    game_engine()


if __name__ == '__main__':
    main()
