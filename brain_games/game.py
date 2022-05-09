"""Game framework."""


import prompt
from brain_games.cli import welcome_user

MAX_ROUNDS = 3


def start_game(welcome_text, make_question):
    """Run game.

    Args:
        welcome_text: text is printed before game
        make_question: function returns question and correct answer
    """
    print('Welcome to the Brain Games!')
    user_name = welcome_user()

    print(welcome_text)

    current_round = 0
    while current_round < MAX_ROUNDS:
        current_round += 1
        question, correct_answer = make_question()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

        print('Correct!')

    print(f'Congratulations, {user_name}!')
