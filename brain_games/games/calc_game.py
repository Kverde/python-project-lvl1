"""Calc game."""

import operator
import random
import types

from brain_games.game import start_game

OPEARATORS = types.MappingProxyType(
    {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
)

MAX_NUMBER = 20


def make_question():
    """Return question and answer.

    Returns:
        Tuple with question and correct answer
    """
    first_number = random.randint(0, MAX_NUMBER)
    second_number = random.randint(0, MAX_NUMBER)
    op = random.choice(("+", "-", "*"))

    question = f"{first_number} {op} {second_number}"
    correct_answer = OPEARATORS[op](first_number, second_number)

    return question, correct_answer


WELCOME_TEXT = "What is the result of the expression?"


def start():
    """Run game."""
    start_game(WELCOME_TEXT, make_question)
