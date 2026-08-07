from flask import Flask

app = Flask(__name__)


@app.route("/")
def dashboard():
    return """
    <h1>ATLAS</h1>
    <h2>Weekly Dashboard</h2>
    <p>If you can read this, Atlas is running in a browser.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)