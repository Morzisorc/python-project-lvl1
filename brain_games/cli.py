"""Asking username."""

import prompt


def welcome_user():
    """Asking username."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
