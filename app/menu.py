"""
Atlas Home Menu
"""


def show_home():
    """Display the Atlas home menu."""

    print("=" * 40)
    print("ATLAS")
    print("Personal Health Memory System")
    print("=" * 40)
    print()
    print("1. View Dashboard")
    print("2. Import Observation from ChatGPT")
    print("3. Export History for ChatGPT")
    print("4. Exit")
    print()

    return input("Select an option: ")