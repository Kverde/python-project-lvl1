"""Progression game."""

import random

from brain_games.game import start_game

MIN_LENGTH = 5
MAX_LENGTH = 10
MAX_START_NUMBER = 20


def make_sequence():
    """Make random number sequence.

    Returns:
        Sequence
    """
    lenght = random.randint(MIN_LENGTH, MAX_LENGTH)
    start_number = random.randint(0, MAX_START_NUMBER)
    step = random.randint(1, 5)
    return [str(start_number + index * step) for index in range(lenght)]


def make_question():
    """Return question and answer.

    Returns:
        Tuple with question and correct answer
    """
    seq = make_sequence()
    quesion_pos = random.randint(0, len(seq) - 1)
    correct_answer = seq[quesion_pos]

    seq[quesion_pos] = '..'
    question = ' '.join(seq)

    return question, correct_answer


WELCOME_TEXT = 'Find the greatest common divisor of given numbers.'


def start():
    """Run game."""
    start_game(WELCOME_TEXT, make_question)
