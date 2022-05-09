"""Prime game."""

import math
import random

from brain_games.game import start_game

MAX_NUMBER = 100


def is_prime(number):
    """Check prime number.

    Args:
        number: integer number

    Returns:
        True if number is prime
    """
    for divider in range(2, math.ceil(number / 2)):
        if number % divider == 0:
            return False
    return True


def get_answer(number):
    """Return right answer.

    Args:
        number: question number.

    Returns:
        Right answer
    """
    return 'yes' if is_prime(number) else 'no'


def make_question():
    """Return question and answer.

    Returns:
        Tuple with question and correct answer
    """
    question = random.randint(2, MAX_NUMBER)
    correct_answer = get_answer(question)

    return question, correct_answer


WELCOME_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start():
    """Run game."""
    start_game(WELCOME_TEXT, make_question)
