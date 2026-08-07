from pathlib import Path

OBSERVATIONS_DIR = Path("sample_data/weekly")


def get_latest_observation():
    """
    Returns the newest observation file.

    Version 1:
    Returns the first JSON file found.
    """

    files = sorted(OBSERVATIONS_DIR.glob("*.json"))

    if not files:
        raise FileNotFoundError("No observations found.")

    for file in files:
        if file.name == "atlas_observation_v1.json":
         print(f"Loading observation: {file}")
        return file

    print(f"Loading observation: {files[-1]}")
    return files[-1]