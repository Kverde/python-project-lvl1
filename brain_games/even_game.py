"""Even game."""

from random import randint

import prompt
from brain_games.cli import welcome_user

MAX_ROUNDS = 3


def is_even(number):
    """Return True if number is even.

    Args:
        number: integer number

    Returns:
        True if number is even or False if number is odd
    """
    return number % 2 == 0


def get_answer(number):
    """Return right answer.

    Args:
        number: question number.

    Returns:
        Right answer
    """
    return 'yes' if is_even(number) else 'no'


def start():
    """Run game."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    current_round = 0
    while current_round < MAX_ROUNDS:
        current_round += 1
        question = randint(100)
        correct_answer = get_answer(question)

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

        print('Correct!')
        print('Congratulations, {user_name}!')
