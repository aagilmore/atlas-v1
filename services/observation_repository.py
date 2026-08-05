from pathlib import Path

OBSERVATIONS_DIR = Path("observations")


def get_latest_observation():
    """
    Returns the newest observation file.

    Version 1:
    Returns the first JSON file found.
    """

    files = sorted(OBSERVATIONS_DIR.glob("*.json"))

    if not files:
        raise FileNotFoundError("No observations found.")

    return files[-1]