from services.confidence_engine import calculate_confidence

import json
from pathlib import Path


def load_observation():
    file_path = Path("sample_data/weekly/weekly_observation_sample.json")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def print_summary(data, confidence):

    print("=" * 50)
    print("ATLAS WEEKLY OBSERVATION")
    print("=" * 50)

    print(f"Week: {data['week']}")
    print()

    print("Scale")
    print(f"  Today's Weight: {data['scale']['today_weight']} lbs")
    print(f"  Average Weight: {data['scale']['average_weight']} lbs")
    print()

    print("Recovery")
    print(f"  Avg Calorie Burn: {data['recovery']['average_daily_calorie_burn']}")
    print()

    print("Activity")
    print(f"  Strength Sessions: {data['activity']['strength_sessions']}")
    print(f"  Weekly Strength Volume: {data['activity']['weekly_strength_volume']}")
    print(f"  Avg Volume/Session: {data['activity']['average_strength_volume_per_session']}")
    print()

    print("Nutrition")
    print(f"  Calories: {data['nutrition']['average_daily_calories']}")
    print(f"  Protein: {data['nutrition']['average_daily_protein']} g")
    print()

    print("Assessment")
    print(f"  Status: {data['assessment']['overall_status']}")
    print(f"  Confidence: {confidence['confidence']}")
    print()

    print("=" * 50)
    print("Observation Loaded Successfully")
    print("=" * 50)


if __name__ == "__main__":
    observation = load_observation()
    confidence = calculate_confidence(observation)
    print_summary(observation,confidence)