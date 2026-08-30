from flask import Flask, render_template_string, request, redirect, url_for
import json
from pathlib import Path
import tempfile


# ATLAS Dashboard V10

app = Flask(__name__)


# ATLAS Dashboard V10
# V10 allows the user to select any weekly ATLAS JSON from the browser/iPad
# Files picker. No weekly observation filename is hard-coded.

CURRENT_OBSERVATION_FILE = None


def load_observation():
    """Load the weekly observation selected by the user."""
    global CURRENT_OBSERVATION_FILE

    if not CURRENT_OBSERVATION_FILE:
        return None

    file_path = Path(CURRENT_OBSERVATION_FILE)

    if not file_path.exists():
        CURRENT_OBSERVATION_FILE = None
        return None

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/upload", methods=["POST"])
def upload_observation():
    """Accept a weekly JSON selected through the browser/iPad file picker."""
    global CURRENT_OBSERVATION_FILE

    uploaded = request.files.get("observation_file")

    if not uploaded or not uploaded.filename:
        return redirect(url_for("dashboard"))

    raw = uploaded.read()

    try:
        observation = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return (
            "Invalid JSON file. Please select an ATLAS weekly observation JSON.",
            400,
        )

    required_sections = (
        "strategic_scorecard",
        "weekly_execution_scorecard",
        "atlas_weekly_brief",
    )
    missing = [section for section in required_sections if section not in observation]

    if missing:
        return (
            "This JSON is not a compatible ATLAS observation file. "
            f"Missing: {', '.join(missing)}",
            400,
        )

    temp_file = tempfile.NamedTemporaryFile(
        mode="wb",
        suffix=".json",
        prefix="atlas_observation_",
        delete=False,
    )
    temp_file.write(raw)
    temp_file.close()

    CURRENT_OBSERVATION_FILE = temp_file.name
    return redirect(url_for("dashboard"))

@app.route("/choose")
def choose():
    return render_template_string(SELECT_FILE_TEMPLATE)

@app.route("/")
def dashboard():
    observation = load_observation()

    if observation is None:
        return render_template_string(SELECT_FILE_TEMPLATE)

    strategic = observation["strategic_scorecard"]
    performance = strategic["performance_score"]
    execution = observation["weekly_execution_scorecard"]
    weekly_brief = observation["atlas_weekly_brief"]

    return render_template_string(
        DASHBOARD_TEMPLATE,
        observation=observation,
        strategic=strategic,
        performance=performance,
        execution=execution,
        weekly_brief=weekly_brief,
    )


SELECT_FILE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ATLAS — Select Weekly Check-In</title>
<style>
:root {
    --bg:#050a12; --card:#08111b; --border:#1c2b38;
    --text:#e9eef3; --muted:#8f9da8; --purple:#b75cff;
}
* { box-sizing:border-box; }
body {
    margin:0; min-height:100vh; padding:28px;
    background:radial-gradient(circle at top left,rgba(38,56,70,.28),transparent 34%),var(--bg);
    color:var(--text); font-family:Arial,Helvetica,sans-serif;
    display:flex; align-items:center; justify-content:center;
}
.card {
    width:min(620px,100%); border:1px solid var(--border); border-radius:12px;
    background:linear-gradient(145deg,rgba(10,25,38,.96),rgba(5,13,21,.99));
    padding:28px;
}
.eyebrow { color:var(--muted); font-size:11px; letter-spacing:1.8px; text-transform:uppercase; }
h1 { margin:0; letter-spacing:3px; font-size:30px; }
h2 { margin:4px 0 22px; color:var(--muted); font-size:15px; font-weight:500; }
p { color:var(--muted); line-height:1.5; }
input[type=file] {
    width:100%; margin:18px 0; padding:14px;
    border:1px dashed #385064; border-radius:8px;
    background:rgba(4,11,18,.58); color:var(--text);
}
button {
    width:100%; padding:13px 18px; border:0; border-radius:8px;
    background:var(--purple); color:white; font-size:14px; font-weight:700;
}
.note { margin-top:16px; font-size:11px; }
</style>
</head>
<body>
<div class="card">
    <div class="eyebrow">Personal Operating System</div>
    <h1>ATLAS</h1>
    <h2>Weekly Dashboard</h2>
    <p>Select any ATLAS weekly observation JSON from Files. You can open
       the current week or any past week without changing the code.</p>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="observation_file"
               accept=".json,application/json" required>
        <button type="submit">Open Weekly Check-In</button>
    </form>
    <p class="note">Atlas starts with file selection; no weekly observation filename is hard-coded.</p>
</div>
</body>
</html>
"""


DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ATLAS — Weekly Dashboard V10</title>

    <style>
        :root {
            --bg: #050a12;
            --panel: #07101a;
            --card: #08111b;
            --border: #1c2b38;
            --text: #e9eef3;
            --muted: #8f9da8;
            --label: #c7d1d9;
            --good: #9bd62d;
            --warn: #f0a53a;
            --bad: #ef5b5b;
            --purple: #b75cff;
            --blue: #4d9fff;
            --teal: #25c7c0;
            --orange: #ff8b2d;
            --radius: 9px;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 28px;
            background:
                radial-gradient(circle at top left, rgba(38, 56, 70, 0.28), transparent 34%),
                var(--bg);
            color: var(--text);
            font-family: Arial, Helvetica, sans-serif;
            font-size: 14px;
            line-height: 1.4;
        }

        .dashboard {
            max-width: 1500px;
            margin: 0 auto;
        }

        .header {
            margin-bottom: 20px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 14px;
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 24px;
        }

        .brand {
            min-width: 0;
        }

        .week-stamp {
            text-align: right;
            white-space: nowrap;
            line-height: 1.15;
            padding-bottom: 1px;
        }

        .week-number {
            color: var(--text);
            font-size: 16px;
            font-weight: 700;
            letter-spacing: 0.8px;
            text-transform: uppercase;
        }

        .week-dates {
            margin-top: 4px;
            color: var(--muted);
            font-size: 12px;
        }

        .change-week {
            display: inline-block;
            margin-top: 7px;
            color: #71b7ff;
            font-size: 10px;
            text-decoration: none;
        }

        .change-week:hover {
            text-decoration: underline;
        }

        .eyebrow {
            margin: 0 0 2px;
            color: var(--muted);
            font-size: 11px;
            letter-spacing: 1.8px;
            text-transform: uppercase;
        }

        h1 {
            margin: 0;
            font-size: 29px;
            letter-spacing: 3px;
        }

        .header h2 {
            margin: 0;
            color: var(--muted);
            font-size: 15px;
            font-weight: 500;
        }

        h2 {
            margin: 0;
            color: #dce5eb;
            font-size: 17px;
        }

        h3 {
            margin: 0 0 9px;
            color: #f0f4f7;
            font-size: 13px;
        }

        p {
            margin: 5px 0;
        }

        strong {
            color: var(--label);
        }

        .section {
            margin-top: 20px;
        }

        .section-title {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 9px;
        }

        .section-title::after {
            content: "";
            flex: 1;
            height: 1px;
            background: var(--border);
        }

        .scorecard-grid,
        .execution-grid,
        .pillar-grid {
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 10px;
        }

        .scorecard-card,
        .execution-card,
        .pillar-card,
        .brief-card,
        .event {
            min-width: 0;
            border: 1px solid var(--border);
            border-radius: var(--radius);
            background: linear-gradient(145deg, rgba(10, 25, 38, 0.96), rgba(5, 13, 21, 0.99));
        }

        .scorecard-card {
            min-height: 142px;
            padding: 13px;
        }

        .performance-card {
            min-height: 142px;
        }

        .performance-top {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 8px;
        }

        .performance-circle {
            --score: 0;
            flex: 0 0 auto;
            width: 67px;
            height: 67px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: conic-gradient(
                #7fce28 calc(var(--score) * 1%),
                #263846 0
            );
        }

        .performance-circle-inner {
            width: 51px;
            height: 51px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--card);
        }

        .performance-score {
            font-size: 20px;
            font-weight: 700;
        }

        .performance-rating {
            margin: 0;
            font-size: 14px;
            font-weight: 700;
            color: #9ce83a;
        }

        .confidence {
            color: var(--muted);
            font-size: 10px;
            letter-spacing: .4px;
        }

        .breakdown {
            display: grid;
            gap: 2px;
            margin-top: 3px;
        }

        .breakdown-row {
            display: grid;
            grid-template-columns: 1fr auto auto;
            gap: 7px;
            align-items: center;
            font-size: 10px;
        }

        .breakdown-weight {
            color: var(--muted);
        }

        .breakdown-score {
            min-width: 20px;
            text-align: right;
            font-weight: 700;
        }

        .metric-value {
            margin: 2px 0 5px;
            font-size: 22px;
            font-weight: 700;
        }

        .metric-change {
            color: var(--muted);
            font-size: 10px;
        }

        .metric-goal {
            margin-top: 6px;
            color: var(--label);
            font-size: 10px;
        }

        .status {
            display: inline-block;
            padding: 3px 8px;
            border: 1px solid rgba(143, 199, 160, .45);
            border-radius: 999px;
            background: rgba(143, 199, 160, .08);
            color: #9ce83a;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: .4px;
            text-transform: uppercase;
        }

        .execution-card {
            padding: 12px;
            min-height: 158px;
        }

        .execution-stat-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 6px;
        }

        .execution-stat {
            border: 1px solid rgba(203, 216, 223, .18);
            border-radius: 6px;
            padding: 7px;
            background: rgba(4, 11, 18, .58);
        }

        .execution-stat-label {
            color: var(--muted);
            font-size: 9px;
            text-transform: uppercase;
            letter-spacing: .6px;
        }

        .execution-stat-value {
            margin-top: 2px;
            font-size: 13px;
            font-weight: 700;
        }

        .nutrition-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 6px;
        }

        .nutrition-item {
            border: 1px solid rgba(203, 216, 223, .18);
            border-radius: 6px;
            padding: 7px;
        }

        .nutrition-label {
            color: var(--muted);
            font-size: 9px;
            text-transform: uppercase;
        }

        .nutrition-value {
            font-size: 12px;
            font-weight: 700;
        }

        .brief-grid {
            display: grid;
            grid-template-columns: 1.15fr 1.05fr 2.1fr 1.1fr;
            gap: 10px;
        }

        .brief-card {
            min-height: 116px;
            padding: 12px;
        }

        .brief-card h3 {
            text-transform: uppercase;
            letter-spacing: .4px;
            font-size: 11px;
        }

        .brief-status {
            font-size: 17px;
            font-weight: 700;
            color: #9ce83a;
            margin: 8px 0 2px;
        }

        .brief-analysis {
            font-size: 11px;
            line-height: 1.45;
        }

        .brief-focus {
            margin-top: 9px;
            color: #71b7ff;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
        }

        .pillar-card {
            padding: 11px;
            min-height: 105px;
        }

        .pillar-status {
            margin-bottom: 6px;
        }

        .pillar-summary {
            color: #d7e0e5;
            font-size: 10px;
            line-height: 1.35;
        }

        .events-list {
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 10px;
            width: 100%;
        }

        /*
         * V4 FIX:
         * Upcoming Events are five horizontal cards on desktop,
         * matching the reference mockup. Each event is its own card.
         */
        .event {
            min-width: 0;
            min-height: 128px;
            padding: 12px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .event h3 {
            font-size: 11px;
            text-transform: uppercase;
            margin-bottom: 7px;
        }

        .event-meta {
            display: grid;
            gap: 2px;
            color: var(--muted);
            font-size: 9px;
        }

        .event-description {
            margin-top: 8px;
            font-size: 10px;
            line-height: 1.35;
        }

        .event-days {
            margin-top: 8px;
            color: #9ce83a;
            font-size: 10px;
            font-weight: 700;
        }

        .footer {
            margin-top: 18px;
            padding-top: 10px;
            border-top: 1px solid var(--border);
            color: var(--muted);
            font-size: 10px;
            text-align: center;
        }


        /* Mockup accent hierarchy */
        .scorecard-grid .scorecard-card:nth-child(1) h3,
        .execution-grid .execution-card:nth-child(1) h3 {
            color: var(--purple);
        }

        .execution-grid .execution-card:nth-child(2) h3 {
            color: #b6d94c;
        }

        .execution-grid .execution-card:nth-child(3) h3 {
            color: var(--blue);
        }

        .execution-grid .execution-card:nth-child(4) h3 {
            color: var(--teal);
        }

        .execution-grid .execution-card:nth-child(5) h3 {
            color: var(--orange);
        }

        .pillar-grid .pillar-card:nth-child(1) h3 {
            color: var(--purple);
        }

        .pillar-grid .pillar-card:nth-child(2) h3 {
            color: var(--blue);
        }

        .pillar-grid .pillar-card:nth-child(3) h3 {
            color: var(--teal);
        }

        .pillar-grid .pillar-card:nth-child(4) h3 {
            color: var(--orange);
        }

        .pillar-grid .pillar-card:nth-child(5) h3 {
            color: #54d6c8;
        }

        .section-title h2 {
            color: #e8eef2;
        }

        .events-list .event:nth-child(1) h3 {
            color: var(--purple);
        }

        .events-list .event:nth-child(2) h3 {
            color: #b6d94c;
        }

        .events-list .event:nth-child(3) h3 {
            color: var(--blue);
        }

        .events-list .event:nth-child(4) h3 {
            color: var(--orange);
        }

        .events-list .event:nth-child(5) h3 {
            color: var(--teal);
        }

        .event-days {
            color: var(--good);
        }

        .brief-focus {
            color: var(--blue);
        }

        .brief-status {
            color: var(--good);
        }

        .status {
            color: var(--good);
            border-color: rgba(155, 214, 45, .35);
            background: rgba(155, 214, 45, .06);
        }

        @media (max-width: 1150px) {
            .scorecard-grid,
            .execution-grid,
            .pillar-grid {
                grid-template-columns: repeat(3, minmax(0, 1fr));
            }

            .brief-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .events-list {
                grid-template-columns: repeat(3, minmax(0, 1fr));
            }
        }

        @media (max-width: 750px) {
            body {
                padding: 16px;
            }

            .header {
                align-items: flex-start;
            }

            .week-stamp {
                text-align: right;
            }

            .scorecard-grid,
            .execution-grid,
            .brief-grid,
            .pillar-grid,
            .events-list {
                grid-template-columns: 1fr;
            }

            .event {
                min-height: auto;
            }
        }
    </style>
</head>

<body>
<div class="dashboard">

    <header class="header">
        <div class="brand">
            <p class="eyebrow">Personal Operating System</p>
            <h1>ATLAS</h1>
            <h2>Weekly Dashboard</h2>
        </div>
        <div class="week-stamp">
            <div class="week-number">
                {{ observation.get("week", {}).get("reporting_week", "Week —") }}
            </div>
            <div class="week-dates">
                {{ observation.get("week", {}).get("date_range", "Check-in period unavailable") }}
            </div>
            <a class="change-week" href="/choose">Choose another week</a>
        </div>
    </header>


    <!-- STRATEGIC SCORECARD -->
    <section class="section">
        <div class="section-title">
            <h2>Strategic Scorecard</h2>
        </div>

        <div class="scorecard-grid">

            <div class="scorecard-card performance-card">
                <h3>Performance</h3>

                <div class="performance-top">
                    <div class="performance-circle"
                         style="--score: {{ performance['score'] }};">
                        <div class="performance-circle-inner">
                            <span class="performance-score">
                                {{ performance["score"] }}
                            </span>
                        </div>
                    </div>

                    <div>
                        <p class="performance-rating">
                            {{ performance["rating"] }}
                        </p>
                        <p class="confidence">
                            Confidence: {{ performance["confidence"] }}
                        </p>
                    </div>
                </div>

                <div class="breakdown">
                    {% for name, item in performance["breakdown"].items() %}
                    <div class="breakdown-row">
                        <span>{{ name.replace("_", " ").title() }}</span>
                        <span class="breakdown-weight">{{ item["weight"] }}%</span>
                        <span class="breakdown-score">{{ "N/A" if item["score"] is none else item["score"] }}</span>
                    </div>
                    {% endfor %}
                </div>
            </div>

            <div class="scorecard-card">
                <h3>Goal Progress</h3>
                <div class="metric-value">
                    {{ strategic["goal_progress"]["percent_complete"] }}%
                </div>
                <p>
                    <span class="status">
                        {{ strategic["goal_progress"]["status"] }}
                    </span>
                </p>
                <p class="metric-goal">
                    Goal: {{ strategic["goal_progress"]["primary_goal"] }}
                </p>
                <p class="metric-change">
                    Projected 20% BF:
                    {{ strategic["goal_progress"]["projected_20_percent_bf"] }}
                </p>
                <p class="metric-change">
                    Estimated completion:
                    {{ strategic["goal_progress"]["estimated_goal_date"] }}
                </p>
            </div>

            <div class="scorecard-card">
                <h3>Body Fat</h3>
                <div class="metric-value">
                    {{ strategic["body_fat"]["value"] }}%
                </div>
                <p class="metric-change">
                    Change:
                    {{ strategic["body_fat"]["monthly_change"] }}%
                </p>
                <p class="metric-goal">
                    Goal: {{ strategic["body_fat"]["goal"] }}%
                </p>
                <p class="confidence">
                    Confidence: {{ strategic["body_fat"]["confidence"] if strategic["body_fat"].get("confidence") else "MEDIUM" }}
                </p>
            </div>

            <div class="scorecard-card">
                <h3>VO₂ Max</h3>
                <div class="metric-value">
                    {{ strategic["vo2_max"]["value"] }}
                </div>
                <p class="metric-change">
                    Change:
                    {{ strategic["vo2_max"]["monthly_change"] }}
                </p>
                <p class="metric-goal">
                    Goal: {{ strategic["vo2_max"]["goal"] }}
                </p>
                <p class="confidence">
                    Confidence: HIGH
                </p>
            </div>

            <div class="scorecard-card">
                <h3>Lean Mass</h3>
                <div class="metric-value">
                    {{ strategic["lean_mass"]["value"] }} lbs
                </div>
                <p class="metric-change">
                    Change:
                    {{ strategic["lean_mass"]["monthly_change"] }} lbs
                </p>
                <p class="metric-goal">
                    Goal: {{ strategic["lean_mass"]["goal"] }}
                </p>
                <p class="confidence">
                    Confidence: HIGH
                </p>
            </div>

        </div>
    </section>


    <!-- WEEKLY EXECUTION SCORECARD -->
    <section class="section">
        <div class="section-title">
            <h2>Weekly Execution Scorecard</h2>
        </div>

        <div class="execution-grid">

            <!-- BODY -->
            <div class="execution-card">
                <h3>BODY</h3>
                <div class="execution-stat-grid">
                    <div class="execution-stat">
                        <div class="execution-stat-label">Weight</div>
                        <div class="execution-stat-value">
                            {{ execution["body"]["weight"]["value"] }}
                            {{ execution["body"]["weight"]["unit"] }}
                        </div>
                    </div>
                </div>
                <p class="confidence">
                    Weekly change:
                    {{ execution["body"]["weight"]["weekly_change"] }}
                </p>
                <p class="confidence">
                    Confidence: {{ execution["body"]["confidence"] }}
                </p>
            </div>

            <!-- NUTRITION -->
            <div class="execution-card">
                <h3>NUTRITION</h3>
                <div class="nutrition-grid">
                    <div class="nutrition-item">
                        <div class="nutrition-label">Calories</div>
                        <div class="nutrition-value">
                            {{ execution["nutrition"]["calories"]["actual"] }}
                            /
                            {{ execution["nutrition"]["calories"]["target"] }}
                        </div>
                    </div>
                    <div class="nutrition-item">
                        <div class="nutrition-label">Protein</div>
                        <div class="nutrition-value">
                            {{ execution["nutrition"]["protein"]["actual"] }}g /
                            {{ execution["nutrition"]["protein"]["target"] }}g
                        </div>
                    </div>
                    <div class="nutrition-item">
                        <div class="nutrition-label">Fat</div>
                        <div class="nutrition-value">
                            {{ execution["nutrition"]["fat"]["actual"] }}g
                        </div>
                    </div>
                    <div class="nutrition-item">
                        <div class="nutrition-label">Carbohydrates</div>
                        <div class="nutrition-value">
                            {{ execution["nutrition"]["carbohydrates"]["actual"] }}g
                        </div>
                    </div>
                    <div class="nutrition-item">
                        <div class="nutrition-label">Deficit</div>
                        <div class="nutrition-value">
                            {{ execution["nutrition"]["deficit"]["value"] }} kcal
                        </div>
                    </div>
                    <div class="nutrition-item">
                        <div class="nutrition-label">Adaptive TDEE</div>
                        <div class="nutrition-value">
                            {{ execution["nutrition"]["adaptive_tdee"]["value"] }} kcal
                        </div>
                    </div>
                </div>
                <p class="confidence">
                    Confidence: {{ execution["nutrition"]["confidence"] }}
                </p>
            </div>

            <!-- TRAINING -->
            <div class="execution-card">
                <h3>TRAINING</h3>
                <div class="execution-stat-grid">
                    <div class="execution-stat">
                        <div class="execution-stat-label">Strength Volume</div>
                        <div class="execution-stat-value">
                            {{ execution["training"]["weekly_strength_volume"] }}
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">Avg Volume</div>
                        <div class="execution-stat-value">
                            {{ execution["training"]["average_volume_per_session"] }}
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">VO₂ Intervals</div>
                        <div class="execution-stat-value">
                            {{ execution["training"]["vo2_intervals"]["completed"] }}
                            /
                            {{ execution["training"]["vo2_intervals"]["goal"] }}
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">Strength</div>
                        <div class="execution-stat-value">
                            {{ execution["training"]["strength_sessions"]["completed"] }}
                            /
                            {{ execution["training"]["strength_sessions"]["goal"] }}
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">Zone 2</div>
                        <div class="execution-stat-value">
                            {{ execution["training"]["zone2_sessions"]["completed"] }}
                            /
                            {{ execution["training"]["zone2_sessions"]["goal"] }}
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">Zone 1–3</div>
                        <div class="execution-stat-value">
                            {{ execution["training"]["zone1_3_time"] }}
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">Zone 4–5</div>
                        <div class="execution-stat-value">
                            {{ execution["training"]["zone4_5_time"] }}
                        </div>
                    </div>
                </div>
                <p class="confidence">
                    Confidence: {{ execution["training"]["confidence"] }}
                </p>
            </div>

            <!-- RECOVERY -->
            <div class="execution-card">
                <h3>RECOVERY</h3>
                <div class="execution-stat-grid">
                    <div class="execution-stat">
                        <div class="execution-stat-label">Sleep Performance</div>
                        <div class="execution-stat-value">
                            {{ execution["recovery"]["sleep_performance"]["value"] }}%
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">HRV</div>
                        <div class="execution-stat-value">
                            {{ execution["recovery"]["hrv"]["value"] }} ms
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">Resting HR</div>
                        <div class="execution-stat-value">
                            {{ execution["recovery"]["resting_hr"]["value"] }} bpm
                        </div>
                    </div>
                </div>
                <p class="confidence">
                    Sleep: {{ execution["recovery"]["sleep_performance"]["status"] }}
                </p>
                <p class="confidence">
                    HRV: {{ execution["recovery"]["hrv"]["status"] }}
                </p>
                <p class="confidence">
                    RHR: {{ execution["recovery"]["resting_hr"]["status"] }}
                </p>
                <p class="confidence">
                    Confidence: {{ execution["recovery"]["confidence"] }}
                </p>
            </div>

            <!-- LIFESTYLE & ADHERENCE -->
            <div class="execution-card">
                <h3>LIFESTYLE &amp; ADHERENCE</h3>
                <div class="execution-stat-grid">
                    <div class="execution-stat">
                        <div class="execution-stat-label">Steps</div>
                        <div class="execution-stat-value">
                            {{ execution["lifestyle_adherence"]["steps"]["actual"] }}
                            /
                            {{ execution["lifestyle_adherence"]["steps"]["goal"] }}
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">Drinks</div>
                        <div class="execution-stat-value">
                            {{ execution["lifestyle_adherence"]["drinks"]["actual"] }}
                            /
                            {{ execution["lifestyle_adherence"]["drinks"]["goal"] }}
                        </div>
                    </div>
                    <div class="execution-stat">
                        <div class="execution-stat-label">Work Stress</div>
                        <div class="execution-stat-value">
                            {{ observation["week_context"]["work_stress"] }}
                        </div>
                    </div>
                </div>
                <p class="confidence">
                    Confidence: {{ execution["lifestyle_adherence"]["confidence"] }}
                </p>
            </div>

        </div>
    </section>


    <!-- ATLAS WEEKLY BRIEF -->
    <section class="section">
        <div class="section-title">
            <h2>Atlas Weekly Brief</h2>
        </div>

        <div class="brief-grid">

            <div class="brief-card">
                <h3>Overall Status</h3>
                <div class="brief-status">
                    {{ weekly_brief["overall_status"] }}
                </div>
                <p class="confidence">
                    Confidence: {{ weekly_brief["confidence"] }}
                </p>
            </div>

            <div class="brief-card">
                <h3>Week Context</h3>
                <p><strong>Type:</strong> {{ observation["week_context"]["week_type"] }}</p>
                <p><strong>Goal:</strong> {{ observation["week_context"]["goal"] }}</p>
                <p><strong>Travel:</strong> {{ observation["week_context"]["travel"] }}</p>
                <p><strong>Work Stress:</strong> {{ observation["week_context"]["work_stress"] }}</p>
                <p><strong>Alcohol:</strong> {{ observation["week_context"]["alcohol"] }}</p>
            </div>

            <div class="brief-card">
                <h3>Coach's Analysis &amp; Focus</h3>
                <p class="brief-analysis">
                    {{ observation["coach_analysis_focus"]["analysis"] }}
                </p>
                <div class="brief-focus">Focus for Next Week</div>
                <p class="brief-analysis">
                    {{ observation["coach_analysis_focus"]["focus_for_next_week"] }}
                </p>
                <p class="confidence">
                    Confidence: {{ observation["coach_analysis_focus"]["confidence"] }}
                </p>
            </div>

            <div class="brief-card">
                <h3>Overall Confidence</h3>
                <div class="brief-status">
                    {{ observation["overall_confidence"]["level"] }}
                </div>
                <p class="brief-analysis">
                    {{ observation["overall_confidence"]["summary"] }}
                </p>
                <p class="confidence">
                    Confidence: {{ observation["overall_confidence"]["confidence"] }}
                </p>
            </div>

        </div>
    </section>


    <!-- PILLAR STATUS -->
    <section class="section">
        <div class="section-title">
            <h2>Pillar Status</h2>
            <span class="confidence">Click a pillar to drive deeper analysis</span>
        </div>

        <div class="pillar-grid">
            {% for name, pillar in observation["pillar_status"].items() %}
            <div class="pillar-card">
                <h3>{{ name.replace("_", " ").title() }}</h3>
                <p class="pillar-status">
                    <span class="status">{{ pillar["status"] }}</span>
                </p>
                <p class="pillar-summary">
                    {{ pillar["summary"] | join(" • ") }}
                </p>
                <p class="confidence">
                    Confidence: {{ pillar["confidence"] }}
                </p>
            </div>
            {% endfor %}
        </div>
    </section>


    <!-- UPCOMING EVENTS -->
    <section class="section">
        <div class="section-title">
            <h2>Upcoming Events</h2>
        </div>

        <div class="events-list">
            {% for event in observation["upcoming_events"] %}
            <div class="event">
                <div>
                    <h3>{{ event["title"] }}</h3>
                    <div class="event-meta">
                        <span>Date: {{ event["date"] }}</span>
                        <span>Confidence: {{ event["confidence"] }}</span>
                    </div>
                    <p class="event-description">
                        {{ event["description"] }}
                    </p>
                </div>

                <div class="event-days">
                    {{ event["days_remaining"] }} days
                </div>
            </div>
            {% endfor %}
        </div>
    </section>


    <div class="footer">
        {{ observation.get("footer", {}).get("motivation", "Small, consistent wins lead to big long-term results. Stay consistent.") }}
    </div>

</div>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50010, debug=False)
