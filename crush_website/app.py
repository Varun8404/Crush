from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

ANSWERS_FILE = "answers.json"


def save_answer(data):
    answers = []

    if os.path.exists(ANSWERS_FILE):
        try:
            with open(ANSWERS_FILE, "r", encoding="utf-8") as file:
                answers = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            answers = []

    data["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    answers.append(data)

    with open(ANSWERS_FILE, "w", encoding="utf-8") as file:
        json.dump(
            answers,
            file,
            indent=4,
            ensure_ascii=False
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received."
        }), 400

    save_answer(data)

    return jsonify({
        "success": True,
        "message": "Answers saved ❤️"
    })


if __name__ == "__main__":
    app.run(debug=True)