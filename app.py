
import os
from flask import Flask

app = Flask(__name__)

# Configuration par variable d'environnement
MESSAGE = os.getenv("APP_MESSAGE", "Bienvenue dans notre application Docker !")

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Mini Projet Docker</title>
        </head>
        <body>
            <h1>{MESSAGE}</h1>
            <p>Application Docker - Version avec cache optimise.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
