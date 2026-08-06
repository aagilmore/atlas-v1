"""
Atlas Application
"""

from app.menu import show_home
from dashboard.dashboard_generator import display_dashboard


def run():
    """Run the Atlas application."""

    while True:

        choice = show_home()

        print()

        if choice == "1":
            display_dashboard()

        elif choice == "2":
            print("Importing Observation...")
            print("(Not yet implemented.)")

        elif choice == "3":
            print("Exporting History...")
            print("(Not yet implemented.)")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid selection.")

        input("\nPress Enter to return to the Home menu...")
        print()