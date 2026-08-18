from flask import Flask
import json
from services.observation_repository import get_latest_observation

app = Flask(__name__)

def load_observation():
    file_path = get_latest_observation()

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
@app.route("/")
def dashboard():
    observation = load_observation()
    strategic = observation["strategic_scorecard"]
    performance = strategic["performance_score"]
    execution = observation["weekly_execution_scorecard"]
    training = execution["training"]
    weekly_brief = obserweekly_brief = observation["atlas_weekly_brief"]

    upcoming_events_html = ""

    for event in observation["upcoming_events"]:
        upcoming_events_html += f"""
        <div>
            <h3>{event["title"]}</h3>
            <p><strong>Date:</strong> {event["date"]}</p>
            <p><strong>Days Remaining:</strong> {event["days_remaining"]}</p>
            <p>{event["description"]}</p>
            <p><strong>Confidence:</strong> {event["confidence"]}</p>
        </div>
        """

    return f"""

    <!DOCTYPE html>
    <html>
    <head>
        
        <title>Atlas Dashboard</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                padding: 24px;
                background: #06111b;
                color: #e8eef2;
                font-family: Arial, Helvetica, sans-serif;
                font-size: 14px;
            }}

            h1 {{
                margin: 0;
                font-size: 30px;
                letter-spacing: 2px;
            }}

            h2 {{
                margin: 8px 0 14px;
                font-size: 18px;
                color: #dce5eb;
            }}

            h3 {{
                margin: 0 0 10px;
                font-size: 15px;
                color: #f0f4f7;
            }}

            p {{
                margin: 6px 0;
            }}

            hr {{
                border: 0;
                border-top: 1px solid #263846;
                margin: 18px 0;
            }}

            #strategic-scorecard,
            #events {{
                border: 1px solid #263846;
                border-radius: 10px;
                padding: 16px;
                background: #081723;
            }}

            #strategic-scorecard > div {{
                 border: 1px solid #263846;
                border-radius: 8px;
                padding: 14px;
                margin-bottom: 12px;
                background: #0b1d2a;
            }}

            #strategic-scorecard > div:last-child {{
                margin-bottom: 0;
            }}

            strong {{
                color: #cbd8df;
            }}
            
            .scorecard-grid {{
                display: grid;
                grid-template-columns: repeat(5, minmax(0, 1fr));
                gap: 12px;
            }}

            .scorecard-card {{
                border: 1px solid #263846;
                border-radius: 8px;
                padding: 14px;
                background: #0b1d2a;
            }}

            .scorecard-card h3 {{ 
                margin-top: 0;
            }}
        
            .performance-score {{
                font-size: 28px;
                font-weight: 700;
            }} 
            "performance": {
    "score": 87,
    "rating": "Great",
    "confidence": "HIGH",
    "components": {
        "body_composition": {
            "weight": 30,
            "score": 78
        },
        "training": {
            "weight": 20,
            "score": 92
        },
        "recovery": {
            "weight": 20,
            "score": 84
        },
        "nutrition": {
            "weight": 15,
            "score": 90
        },
        "lifestyle": {
            "weight": 10,
            "score": 74
        },
        "health": {
            "weight": 5,

        </style>
</head>


    <body>

    <h1>ATLAS</h1>
    <h2>Weekly Dashboard</h2>

    <h2>Strategic Scorecard</h2>

    <div id="strategic-scorecard">

        <div class="scorecard-grid">

            <div class="scorecard-card">
                <h3>Performance</h3>
                <p class="performance-score"><strong>Score:</strong> {performance["score"]} / 100</p>
                <p><strong>Rating:</strong> {performance["rating"]}</p>
                <p><strong>Confidence:</strong> {performance["confidence"]}</p>

                <div class="performance-breakdown">
                    <p><strong>Body Composition:</strong> {performance["breakdown"]["body_composition"]["weight"]}% &nbsp; {performance["breakdown"]["body_composition"]["score"]}</p>
                    <p><strong>Training:</strong> {performance["breakdown"]["training"]["weight"]}% &nbsp; {performance["breakdown"]["training"]["score"]}</p>
                    <p><strong>Recovery:</strong> {performance["breakdown"]["recovery"]["weight"]}% &nbsp; {performance["breakdown"]["recovery"]["score"]}</p>
                    <p><strong>Nutrition:</strong> {performance["breakdown"]["nutrition"]["weight"]}% &nbsp; {performance["breakdown"]["nutrition"]["score"]}</p>
                    <p><strong>Lifestyle:</strong> {performance["breakdown"]["lifestyle"]["weight"]}% &nbsp; {performance["breakdown"]["lifestyle"]["score"]}</p>
                    <p><strong>Health:</strong> {performance["breakdown"]["health"]["weight"]}% &nbsp; {performance["breakdown"]["health"]["score"]}</p>
                </div>
            </div>

            <div class="scorecard-card">
                <h3>Goal Progress</h3>
                <p><strong>Progress:</strong> {strategic["goal_progress"]["percent_complete"]}%</p>
                <p><strong>Status:</strong> {strategic["goal_progress"]["status"]}</p>
                <p><strong>Goal:</strong> {strategic["goal_progress"]["primary_goal"]}</p>
                <p><strong>Projected 20% BF:</strong> {strategic["goal_progress"]["projected_20_percent_bf"]}</p>
                <p><strong>Estimated Completion:</strong> {strategic["goal_progress"]["estimated_goal_date"]}</p>
            </div>

            <div class="scorecard-card">
                <h3>Body Fat</h3>
                <p><strong>Current:</strong> {strategic["body_fat"]["value"]}%</p>
                <p><strong>Change:</strong> {strategic["body_fat"]["monthly_change"]}%</p>
                <p><strong>Goal:</strong> {strategic["body_fat"]["goal"]}%</p>
            </div>

            <div class="scorecard-card">
                <h3>VO₂ Max</h3>
                <p><strong>Current:</strong> {strategic["vo2_max"]["value"]}</p>
                <p><strong>Change:</strong> +{strategic["vo2_max"]["monthly_change"]}</p>
                <p><strong>Goal:</strong> {strategic["vo2_max"]["goal"]}</p>
            </div>

            <div class="scorecard-card">
                <h3>Lean Mass</h3>
                <p><strong>Current:</strong> {strategic["lean_mass"]["value"]} lbs</p>
                <p><strong>Change:</strong> +{strategic["lean_mass"]["monthly_change"]} lbs</p>
                <p><strong>Goal:</strong> {strategic["lean_mass"]["goal"]}</p>
            </div>

    </div>

    <hr>

    <h2>Weekly Execution Scorecard</h2>

    <div id="execution-scorecard">

        <h3>Training</h3>

        <p><strong>Strength Volume:</strong> {training["weekly_strength_volume"]}</p>

        <p><strong>Avg Volume:</strong> {training["average_volume_per_session"]}</p>

        <p><strong>VO2 Intervals:</strong>
            {training["vo2_intervals"]["completed"]}
            /
            {training["vo2_intervals"]["goal"]}
        </p>

        <p><strong>Strength:</strong>
            {training["strength_sessions"]["completed"]}
            /
            {training["strength_sessions"]["goal"]}
        </p>

        <p><strong>Zone 2:</strong>
            {training["zone2_sessions"]["completed"]}
            /
            {training["zone2_sessions"]["goal"]}
        </p>

        <p><strong>Zone 1–3 Time:</strong> {training["zone1_3_time"]}</p>

        <p><strong>Zone 4–5 Time:</strong> {training["zone4_5_time"]}</p>

</div>

</div>
    </div>

    <hr>

    <h2>Atlas Weekly Brief</h2>

    <div id="weekly-brief">
        <p><strong>Status:</strong> {weekly_brief["overall_status"]}</p>
        <p><strong>Confidence:</strong> {weekly_brief["confidence"]}</p>

        <p><strong>Week:</strong> {observation["week_context"]["week_type"]}</p>
        <p><strong>Goal:</strong> {observation["week_context"]["goal"]}</p>
        <p><strong>Travel:</strong> {observation["week_context"]["travel"]}</p>
        <p><strong>Work Stress:</strong> {observation["week_context"]["work_stress"]}</p>
        <p><strong>Alcohol:</strong> {observation["week_context"]["alcohol"]}</p>

        <p><strong>Coach Analysis:</strong><br>
        {observation["coach_analysis_focus"]["analysis"]}</p>

        <p><strong>Focus for Next Week:</strong><br>
        {observation["coach_analysis_focus"]["focus_for_next_week"]}</p>
    </div>

    <hr>

    <h2>Pillar Status</h2>

    <div id="pillar-status">
        <div id="pillar-cards">

        <h3>Body — {observation["pillar_status"]["body"]["status"]}</h3>
        <p>{", ".join(observation["pillar_status"]["body"]["summary"])}</p>
        <p><strong>Confidence:</strong> {observation["pillar_status"]["body"]["confidence"]}</p>

        <h3>Training — {observation["pillar_status"]["training"]["status"]}</h3>
        <p>{", ".join(observation["pillar_status"]["training"]["summary"])}</p>
        <p><strong>Confidence:</strong> {observation["pillar_status"]["training"]["confidence"]}</p>

        <h3>Recovery — {observation["pillar_status"]["recovery"]["status"]}</h3>
        <p>{", ".join(observation["pillar_status"]["recovery"]["summary"])}</p>
        <p><strong>Confidence:</strong> {observation["pillar_status"]["recovery"]["confidence"]}</p>

        <h3>Lifestyle — {observation["pillar_status"]["lifestyle"]["status"]}</h3>
        <p>{", ".join(observation["pillar_status"]["lifestyle"]["summary"])}</p>
        <p><strong>Confidence:</strong> {observation["pillar_status"]["lifestyle"]["confidence"]}</p>

        <h3>Health — {observation["pillar_status"]["health"]["status"]}</h3>
        <p>{", ".join(observation["pillar_status"]["health"]["summary"])}</p>
        <p><strong>Confidence:</strong> {observation["pillar_status"]["health"]["confidence"]}</p>

</div>
    </div>

    <hr>

    <h2>Upcoming Events</h2>

    <div id="events">
    <hr>

    <div id="upcoming-events">
        {upcoming_events_html}
    </div>
</div>

    </body>
    </html> 
     """


if __name__ == "__main__":
    app.run(debug=True)