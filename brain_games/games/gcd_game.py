"""Calc game."""

import math
import random

from brain_games.game import start_game

MAX_NUMBER = 20


def make_question():
    """Return question and answer.

    Returns:
        Tuple with question and correct answer
    """
    first_number = random.randint(0, MAX_NUMBER)
    second_number = random.randint(0, MAX_NUMBER)
    question = f'{first_number} {second_number}'
    correct_answer = math.gcd(first_number, second_number)

    return question, correct_answer


WELCOME_TEXT = 'Find the greatest common divisor of given numbers.'


def start():
    """Run game."""
    start_game(WELCOME_TEXT, make_question)
