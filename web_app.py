from flask import Flask

app = Flask(__name__)


@app.route("/")
def dashboard():
    return """
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
        Strategic Scorecard goes here
    </div>

    <hr>

    <h2>Weekly Execution Scorecard</h2>

    <div id="execution-scorecard">
        Weekly Execution goes here
    </div>

    <hr>

    <h2>Atlas Weekly Brief</h2>

    <div id="weekly-brief">
        Weekly Brief goes here
    </div>

    <hr>

    <h2>Pillar Status</h2>

    <div id="pillar-status">
        Pillar cards go here
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