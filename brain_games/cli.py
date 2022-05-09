"""Methods for cli."""

import prompt


def welcome_user():
    """Ask user name and great him.

    Returns:
        Username.
    """
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')  # noqa: WPS421
    return user_name
