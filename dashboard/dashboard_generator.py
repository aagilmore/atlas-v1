from services.observation_repository import get_latest_observation
from services.confidence_engine import calculate_confidence

import json


def load_observation():
    file_path = get_latest_observation()

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def render_strategic_scorecard(data):
    strategic = data["strategic_scorecard"]

    print("=" * 70)
    print("ATLAS WEEKLY SNAPSHOT")
    print("=" * 70)
    print()

    print("STRATEGIC SCORECARD")
    print("-" * 70)

    performance = strategic["performance_score"]

    print(f"Performance Score : {performance['score']} / 100")
    print(f"Rating            : {performance['rating']}")
    print(f"Confidence        : {performance['confidence']}")
    print()

    goal = strategic["goal_progress"]
    print("Goal Progress")
    print(f"  Progress        : {goal['percent_complete']}%")
    print(f"  Status          : {goal['status']}")
    print(f"  Goal            : {goal['primary_goal']}")
    print(f"  Est. Completion : {goal['estimated_goal_date']}")
    print(f"  Projected 20%BF : {goal['projected_20_percent_bf']}")
    print()

    bodyfat = strategic["body_fat"]
    print("Body Fat")
    print(f"  Current         : {bodyfat['value']}%")
    print(f"  Goal            : {bodyfat['goal']}%")
    print(f"  Monthly Change  : {bodyfat['monthly_change']}%")
    print()

    vo2 = strategic["vo2_max"]
    print("VO₂ Max")
    print(f"  Current         : {vo2['value']}")
    print(f"  Goal            : {vo2['goal']}")
    print(f"  Monthly Change  : {vo2['monthly_change']}")
    print()

    lean = strategic["lean_mass"]
    print("Lean Mass")
    print(f"  Current         : {lean['value']} {lean['unit']}")
    print(f"  Goal            : {lean['goal']}")
    print(f"  Monthly Change  : +{lean['monthly_change']} {lean['unit']}")
    print()


def display_dashboard():
    """Display the latest Atlas dashboard."""

    observation = load_observation()
    render_strategic_scorecard(observation)
    confidence = calculate_confidence(observation)


if __name__ == "__main__":
    display_dashboard()