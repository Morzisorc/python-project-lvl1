#!/usr/bin/env python
"""Starting project."""

from brain_games.cli import welcome_user


def greet(who):
    """Print username.

    Keyword arguments:
        who -- name
    """
    print(who)


def main():
    """Start function."""
    greet('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
