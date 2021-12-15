from utils import load_envs
import os
from flask import Flask, request, send_from_directory
from utils import proxy

app = Flask(__name__)

IS_DEV = os.environ["FLASK_ENV"] == "development"

if not IS_DEV:
    app = Flask(__name__, static_folder="dist")


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def index(path):
    if IS_DEV:
        result = proxy.proxy(os.environ["CLIENT_HOST"], request.path)
        return result
    return send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    app.run()
