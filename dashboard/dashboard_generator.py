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

def render_weekly_execution_scorecard(data):
    execution = data["weekly_execution_scorecard"]

    print("WEEKLY EXECUTION SCORECARD")
    print("-" * 70)
    print()

    # Body
    body = execution["body"]
    print("Body")
    print(f"    Weight          : {body['weight']['value']} {body['weight']['unit']}")
    print(f"    Weekly Change   : {body['weight']['weekly_change']} {body['weight']['unit']}")
    print(f"    Confidence      : {body['confidence']}")
    print()

    # Nutrition
    nutrition = execution["nutrition"]
    print("Nutrition")
    print(f"    Calories        : {nutrition['calories']['actual']} / {nutrition['calories']['target']} kcal")
    print(f"    Protein         : {nutrition['protein']['actual']} / {nutrition['protein']['target']} g")
    print(f"    Fat             : {nutrition['fat']['actual']} g")
    print(f"    Carbohydrates   : {nutrition['carbohydrates']['actual']} g")
    print(f"    Deficit         : {nutrition['deficit']['value']} kcal")
    print(f"    Adaptive TDEE   : {nutrition['adaptive_tdee']['value']} kcal")
    print(f"    Confidence      : {nutrition['confidence']}")
    print()

    # Training
    training = execution["training"]
    print("Training")
    print(f"    Strength Volume : {training['weekly_strength_volume']}")
    print(f"    Avg Volume      : {training['average_volume_per_session']}")
    print(f"    VO₂ Intervals   : {training['vo2_intervals']['completed']} / {training['vo2_intervals']['goal']}")
    print(f"    Strength        : {training['strength_sessions']['completed']} / {training['strength_sessions']['goal']}")
    print(f"    Zone 2          : {training['zone2_sessions']['completed']} / {training['zone2_sessions']['goal']}")
    print(f"    Zone 1-3 Time   : {training['zone1_3_time']}")
    print(f"    Zone 4-5 Time   : {training['zone4_5_time']}")
    print(f"    Confidence      : {training['confidence']}")
    print()

    # Recovery
    recovery = execution["recovery"]
    print("Recovery")
    print(f"    Sleep           : {recovery['sleep_performance']['value']}{recovery['sleep_performance']['unit']}")
    print(f"    HRV             : {recovery['hrv']['value']} {recovery['hrv']['unit']}")
    print(f"    Resting HR      : {recovery['resting_hr']['value']} {recovery['resting_hr']['unit']}")
    print(f"    Confidence      : {recovery['confidence']}")
    print()

    # Lifestyle
    lifestyle = execution["lifestyle_adherence"]
    print("Lifestyle")
    print(f"    Steps           : {lifestyle['steps']['actual']} / {lifestyle['steps']['goal']}")
    print(f"    Drinks          : {lifestyle['drinks']['actual']} / {lifestyle['drinks']['goal']}")
    print(f"    Work Stress     : {lifestyle['work_stress']['value']} / {lifestyle['work_stress']['scale']}")
    print(f"    Confidence      : {lifestyle['confidence']}")
    print()

def render_weekly_brief(data):
    brief = data["atlas_weekly_brief"]

    print("ATLAS WEEKLY BRIEF")
    print("-" * 70)
    print()

    print("Overall Status")
    print(f"    Status      : {brief['overall_status']}")
    print(f"    Confidence  : {brief['confidence']}")
    print()

    context = data["week_context"]
    print("Week Context")
    print(f"    Week Type   : {context['week_type']}")
    print(f"    Goal        : {context['goal']}")
    print(f"    Travel      : {context['travel']}")
    print(f"    Work Stress : {context['work_stress']}")
    print(f"    Alcohol     : {context['alcohol']}")
    print(f"    Events      : {context['special_events']}")
    print(f"    Sleep       : {context['sleep_location']}")
    print(f"    Injury      : {context['illness_injury']}")
    print(f"    Confidence  : {context['confidence']}")
    print()

    coach = data["coach_analysis_focus"]
    print("Coach Analysis")
    print(f"    Analysis    : {coach['analysis']}")
    print(f"    Next Week   : {coach['focus_for_next_week']}")
    print(f"    Confidence  : {coach['confidence']}")
    print()

    overall = data["overall_confidence"]
    print("Overall Confidence")
    print(f"    Level       : {overall['level']}")
    print(f"    Summary     : {overall['summary']}")
    print(f"    Confidence  : {overall['confidence']}")
    print()

def render_pillar_status(data):
    pillars = data["pillar_status"]

    print("PILLAR STATUS")
    print("-" * 70)
    print()

    for name, pillar in pillars.items():
        print(name.title())
        print(f"    Status      : {pillar['status']}")

        print("    Summary")
        for item in pillar["summary"]:
            print(f"      • {item}")

        print(f"    Confidence  : {pillar['confidence']}")
        print()

def display_dashboard():
    """Display the latest Atlas dashboard."""

    observation = load_observation()
    render_strategic_scorecard(observation)
    render_weekly_execution_scorecard(observation)
    render_weekly_brief(observation)
    render_pillar_status(observation)
    confidence = calculate_confidence(observation)


if __name__ == "__main__":
    display_dashboard()