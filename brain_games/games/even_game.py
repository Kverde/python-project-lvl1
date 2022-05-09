"""Even game."""

from random import randint

from brain_games.game import start_game


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


def make_question():
    """Return question and answer.

    Returns:
        Tuple with question and correct answer
    """
    question = randint(0, 100)
    return question, get_answer(question)


WELCOME_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def start():
    """Run game."""
    start_game(WELCOME_TEXT, make_question)
