#!/usr/bin/env python3

from brain_games.cli import welcome_user

def greet(message):
    print(f'{message}')


def main():
    greet('Welcome to the Brain Games!')
    welcome_user()


if __name__=='__main__':
    main()
