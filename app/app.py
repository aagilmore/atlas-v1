"""
Atlas Application
"""

from app.menu import show_home


def run():
    """Run the Atlas application."""

    while True:

        choice = show_home()

        print()

        if choice == "1":
            print("Opening Dashboard...")
            print("(Not yet implemented.)")

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