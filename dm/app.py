
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Indian Stock Analysis</title>
    </head>
    <body>
        <h1>Indian Stock Market Analysis</h1>
        <p>Flask homepage is working successfully!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
