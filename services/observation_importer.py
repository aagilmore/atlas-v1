"""
Observation Importer
"""

import shutil

from services.observation_inbox import get_pending_observations


def import_observation():
    """
    Import an observation from the Inbox into the Observation Repository.
    """

    observations = get_pending_observations()

    if not observations:
        print("No observations found in the Inbox.")
        return

    print("Pending Observations\n")

    for index, observation in enumerate(observations, start=1):
        print(f"{index}. {observation.name}")

    print()

    selection = input("Select observation to import: ")

    try:
        observation = observations[int(selection) - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    destination = f"observations/{observation.name}"

    shutil.copy2(observation, destination)

    print()
    print(f"Imported {observation.name}")