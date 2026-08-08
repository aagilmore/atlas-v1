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
    weekly_brief = observation["atlas_weekly_brief"]

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Atlas Dashboard</title>
    </head>

    <body>

    <h1>ATLAS</h1>
    <h2>Weekly Dashboard</h2>

    <hr>

    <h2>Strategic Scorecard</h2>

    <div id="strategic-scorecard">
    
    <h3>Performance</h3>

    <p><strong>Score:</strong> {performance["score"]} / 100</p>
    <p><strong>Rating:</strong> {performance["rating"]}</p>
    <p><strong>Confidence:</strong> {performance["confidence"]}</p>

<hr>

    <h3>Goal Progress</h3>

    <p><strong>Progress:</strong> {strategic["goal_progress"]["percent_complete"]}%</p>
    <p><strong>Status:</strong> {strategic["goal_progress"]["status"]}</p>
    <p><strong>Goal:</strong> {strategic["goal_progress"]["primary_goal"]}</p>
    <p><strong>Projected 20% BF:</strong> {strategic["goal_progress"]["projected_20_percent_bf"]}</p>
    <p><strong>Estimated Completion:</strong> {strategic["goal_progress"]["estimated_goal_date"]}</p>
        
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
        Events go here
    </div>

    </body>
    </html> 
     """


if __name__ == "__main__":
    app.run(debug=True)