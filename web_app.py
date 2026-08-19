from flask import Flask, render_template_string
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

    return render_template_string(
        DASHBOARD_TEMPLATE,
        observation=observation,
        strategic=strategic,
        performance=performance,
        execution=execution,
        training=training,
        weekly_brief=weekly_brief,
    )


DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ATLAS — Weekly Dashboard</title>

    <style>
        :root {
            --bg: #06111b;
            --panel: #081723;
            --card: #0b1d2a;
            --border: #263846;
            --text: #e8eef2;
            --muted: #9fb0ba;
            --label: #cbd8df;
            --accent: #cbd8df;
            --accent-soft: rgba(203, 216, 223, 0.14);
            --good: #8fc7a0;
            --warn: #d6bd79;
            --bad: #d98d8d;
            --radius: 10px;
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
            line-height: 1.45;
        }

        .dashboard {
            max-width: 1500px;
            margin: 0 auto;
        }

        .header {
            margin-bottom: 22px;
        }

        .eyebrow {
            margin: 0 0 4px;
            color: var(--muted);
            font-size: 12px;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        h1 {
            margin: 0;
            font-size: 30px;
            letter-spacing: 3px;
        }

        h2 {
            margin: 0 0 12px;
            color: #dce5eb;
            font-size: 18px;
        }

        h3 {
            margin: 0 0 10px;
            color: #f0f4f7;
            font-size: 15px;
        }

        p {
            margin: 6px 0;
        }

        strong {
            color: var(--label);
        }

        .section {
            margin-top: 22px;
        }

        .section-title {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
        }

        .section-title::after {
            content: "";
            flex: 1;
            height: 1px;
            background: var(--border);
        }

        .panel {
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 16px;
            background: rgba(8, 23, 35, 0.92);
        }

        .scorecard-grid {
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 12px;
        }

        .scorecard-card {
            min-width: 0;
            border: 1px solid var(--border);
            border-radius: 9px;
            padding: 16px;
            background: var(--card);
        }

        .performance-card {
            display: flex;
            flex-direction: column;
        }

        .performance-top {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 12px;
        }

        .performance-circle {
            --score: 0;
            flex: 0 0 auto;
            width: 88px;
            height: 88px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: conic-gradient(
                var(--accent) calc(var(--score) * 1%),
                var(--border) 0
            );
        }

        .performance-circle-inner {
            width: 68px;
            height: 68px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--card);
        }

        .performance-score {
            font-size: 24px;
            font-weight: 700;
        }

        .performance-meta {
            flex: 1;
        }

        .performance-rating {
            margin: 0 0 3px;
            font-size: 16px;
            font-weight: 700;
        }

        .confidence {
            color: var(--muted);
            font-size: 12px;
            letter-spacing: 0.5px;
        }

        .breakdown {
            display: grid;
            grid-template-columns: 1fr;
            gap: 5px;
            margin-top: 4px;
        }

        .breakdown-row {
            display: grid;
            grid-template-columns: 1fr auto auto;
            gap: 8px;
            align-items: center;
            font-size: 12px;
        }

        .breakdown-weight {
            color: var(--muted);
        }

        .breakdown-score {
            min-width: 24px;
            text-align: right;
            font-weight: 700;
        }

        .metric-value {
            margin: 2px 0 8px;
            font-size: 22px;
            font-weight: 700;
        }

        .metric-change {
            color: var(--muted);
            font-size: 12px;
        }

        .metric-goal {
            margin-top: 8px;
            color: var(--label);
            font-size: 12px;
        }

        .execution-grid {
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(0, 2fr);
            gap: 16px;
        }

        .execution-summary {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 10px;
        }

        .execution-stat {
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 12px;
            background: var(--card);
        }

        .execution-stat-label {
            color: var(--muted);
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }

        .execution-stat-value {
            margin-top: 3px;
            font-size: 17px;
            font-weight: 700;
        }

        .brief-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
        }

        .brief-card {
            border: 1px solid var(--border);
            border-radius: 9px;
            padding: 14px;
            background: var(--card);
        }

        .brief-card.wide {
            grid-column: 1 / -1;
        }

        .status {
            display: inline-block;
            padding: 4px 9px;
            border: 1px solid var(--border);
            border-radius: 999px;
            background: var(--accent-soft);
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        .pillar-grid {
            display: grid;
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 12px;
        }

        .pillar-card {
            border: 1px solid var(--border);
            border-radius: 9px;
            padding: 14px;
            background: var(--card);
        }

        .pillar-status {
            margin-bottom: 8px;
        }

        .pillar-summary {
            color: #d7e0e5;
            font-size: 12px;
        }

        .events-list {
            display: grid;
            gap: 10px;
        }

        .event {
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 14px;
            background: var(--card);
        }

        .event-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            color: var(--muted);
            font-size: 12px;
        }

        .footer {
            margin-top: 28px;
            padding-top: 14px;
            border-top: 1px solid var(--border);
            color: var(--muted);
            font-size: 11px;
        }

        @media (max-width: 1100px) {
            .scorecard-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .scorecard-card:first-child {
                grid-column: 1 / -1;
            }

            .pillar-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        @media (max-width: 700px) {
            body {
                padding: 16px;
            }

            .scorecard-grid,
            .execution-grid,
            .brief-grid,
            .pillar-grid {
                grid-template-columns: 1fr;
            }

            .scorecard-card:first-child,
            .brief-card.wide {
                grid-column: auto;
            }
        }
    </style>
</head>

<body>
<div class="dashboard">

    <header class="header">
        <p class="eyebrow">Personal operating system</p>
        <h1>ATLAS</h1>
        <h2>Weekly Dashboard</h2>
    </header>


    <!-- STRATEGIC SCORECARD -->
    <section class="section">
        <div class="section-title">
            <h2>Strategic Scorecard</h2>
        </div>

        <div class="scorecard-grid">

            <!-- Performance -->
            <div class="scorecard-card performance-card">
                <h3>Performance</h3>

                <div class="performance-top">
                    <div
                        class="performance-circle"
                        style="--score: {{ performance['score'] }};"
                    >
                        <div class="performance-circle-inner">
                            <span class="performance-score">
                                {{ performance['score'] }}
                            </span>
                        </div>
                    </div>

                    <div class="performance-meta">
                        <p class="performance-rating">
                            {{ performance['rating'] }}
                        </p>
                        <p class="confidence">
                            Confidence: {{ performance['confidence'] }}
                        </p>
                    </div>
                </div>

                <div class="breakdown">
                    {% for name, item in performance["breakdown"].items() %}
                    <div class="breakdown-row">
                        <span>{{ name.replace("_", " ").title() }}</span>
                        <span class="breakdown-weight">{{ item["weight"] }}%</span>
                        <span class="breakdown-score">{{ item["score"] }}</span>
                    </div>
                    {% endfor %}
                </div>
            </div>


            <!-- Goal Progress -->
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
                    <strong>Goal:</strong>
                    {{ strategic["goal_progress"]["primary_goal"] }}
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


            <!-- Body Fat -->
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
                    <strong>Goal:</strong>
                    {{ strategic["body_fat"]["goal"] }}%
                </p>
            </div>


            <!-- VO2 Max -->
            <div class="scorecard-card">
                <h3>VO₂ Max</h3>
                <div class="metric-value">
                    {{ strategic["vo2_max"]["value"] }}
                </div>
                <p class="metric-change">
                    Change:
                    {% if strategic["vo2_max"]["monthly_change"] >= 0 %}+{% endif %}
                    {{ strategic["vo2_max"]["monthly_change"] }}
                </p>
                <p class="metric-goal">
                    <strong>Goal:</strong>
                    {{ strategic["vo2_max"]["goal"] }}
                </p>
            </div>


            <!-- Lean Mass -->
            <div class="scorecard-card">
                <h3>Lean Mass</h3>
                <div class="metric-value">
                    {{ strategic["lean_mass"]["value"] }} lbs
                </div>
                <p class="metric-change">
                    Change:
                    {% if strategic["lean_mass"]["monthly_change"] >= 0 %}+{% endif %}
                    {{ strategic["lean_mass"]["monthly_change"] }} lbs
                </p>
                <p class="metric-goal">
                    <strong>Goal:</strong>
                    {{ strategic["lean_mass"]["goal"] }}
                </p>
            </div>

        </div>
    </section>


    <!-- WEEKLY EXECUTION -->
    <section class="section">
        <div class="section-title">
            <h2>Weekly Execution Scorecard</h2>
        </div>

        <div class="panel execution-grid">

            <div>
                <h3>Training</h3>

                <div class="execution-summary">
                    <div class="execution-stat">
                        <div class="execution-stat-label">Strength Volume</div>
                        <div class="execution-stat-value">
                            {{ training["weekly_strength_volume"] }}
                        </div>
                    </div>

                    <div class="execution-stat">
                        <div class="execution-stat-label">Avg Volume</div>
                        <div class="execution-stat-value">
                            {{ training["average_volume_per_session"] }}
                        </div>
                    </div>

                    <div class="execution-stat">
                        <div class="execution-stat-label">VO₂ Intervals</div>
                        <div class="execution-stat-value">
                            {{ training["vo2_intervals"]["completed"] }}
                            / {{ training["vo2_intervals"]["goal"] }}
                        </div>
                    </div>

                    <div class="execution-stat">
                        <div class="execution-stat-label">Strength</div>
                        <div class="execution-stat-value">
                            {{ training["strength_sessions"]["completed"] }}
                            / {{ training["strength_sessions"]["goal"] }}
                        </div>
                    </div>

                    <div class="execution-stat">
                        <div class="execution-stat-label">Zone 2</div>
                        <div class="execution-stat-value">
                            {{ training["zone2_sessions"]["completed"] }}
                            / {{ training["zone2_sessions"]["goal"] }}
                        </div>
                    </div>

                    <div class="execution-stat">
                        <div class="execution-stat-label">Zone 1–3</div>
                        <div class="execution-stat-value">
                            {{ training["zone1_3_time"] }}
                        </div>
                    </div>

                    <div class="execution-stat">
                        <div class="execution-stat-label">Zone 4–5</div>
                        <div class="execution-stat-value">
                            {{ training["zone4_5_time"] }}
                        </div>
                    </div>
                </div>
            </div>

            <div>
                <h3>Execution Context</h3>
                <p>
                    <strong>Week:</strong>
                    {{ observation["week_context"]["week_type"] }}
                </p>
                <p>
                    <strong>Goal:</strong>
                    {{ observation["week_context"]["goal"] }}
                </p>
                <p>
                    <strong>Travel:</strong>
                    {{ observation["week_context"]["travel"] }}
                </p>
                <p>
                    <strong>Work Stress:</strong>
                    {{ observation["week_context"]["work_stress"] }}
                </p>
                <p>
                    <strong>Alcohol:</strong>
                    {{ observation["week_context"]["alcohol"] }}
                </p>
            </div>

        </div>
    </section>


    <!-- WEEKLY BRIEF -->
    <section class="section">
        <div class="section-title">
            <h2>Atlas Weekly Brief</h2>
        </div>

        <div class="brief-grid">

            <div class="brief-card">
                <h3>Status</h3>
                <p class="status">{{ weekly_brief["overall_status"] }}</p>
                <p class="confidence">
                    Confidence: {{ weekly_brief["confidence"] }}
                </p>
            </div>

            <div class="brief-card">
                <h3>Week Context</h3>
                <p>
                    <strong>Type:</strong>
                    {{ observation["week_context"]["week_type"] }}
                </p>
                <p>
                    <strong>Travel:</strong>
                    {{ observation["week_context"]["travel"] }}
                </p>
                <p>
                    <strong>Work Stress:</strong>
                    {{ observation["week_context"]["work_stress"] }}
                </p>
            </div>

            <div class="brief-card wide">
                <h3>Coach Analysis</h3>
                <p>
                    {{ observation["coach_analysis_focus"]["analysis"] }}
                </p>
            </div>

            <div class="brief-card wide">
                <h3>Focus for Next Week</h3>
                <p>
                    {{ observation["coach_analysis_focus"]["focus_for_next_week"] }}
                </p>
            </div>

        </div>
    </section>


    <!-- PILLAR STATUS -->
    <section class="section">
        <div class="section-title">
            <h2>Pillar Status</h2>
        </div>

        <div class="pillar-grid">
            {% for name, pillar in observation["pillar_status"].items() %}
            <div class="pillar-card">
                <h3>{{ name.title() }}</h3>

                <p class="pillar-status">
                    <span class="status">{{ pillar["status"] }}</span>
                </p>

                <p class="pillar-summary">
                    {{ pillar["summary"] | join(", ") }}
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

        <div class="panel events-list">
            {% for event in observation["upcoming_events"] %}
            <div class="event">
                <h3>{{ event["title"] }}</h3>

                <div class="event-meta">
                    <span>Date: {{ event["date"] }}</span>
                    <span>Days Remaining: {{ event["days_remaining"] }}</span>
                    <span>Confidence: {{ event["confidence"] }}</span>
                </div>

                <p>{{ event["description"] }}</p>
            </div>
            {% endfor %}
        </div>
    </section>


    <div class="footer">
        ATLAS Weekly Dashboard
    </div>

</div>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)