from dotenv import load_dotenv
from flask import jsonify

from app import create_app

app = create_app()


@app.route("/healthcheck")
def healthcheck():
    return jsonify({"status": "on"}), 200


if __name__ == "__main__":
    load_dotenv(".env")
    app.run(host="0.0.0.0")
