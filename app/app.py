"""
Atlas Application
"""

from app.menu import show_home


def run():
    """Run the Atlas application."""

    choice = show_home()

    print()
    print(f"You selected option {choice}.")