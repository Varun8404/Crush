from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "change-this-secret-key"
)

ADMIN_PASSWORD = os.environ.get(
    "ADMIN_PASSWORD",
    "change-this-password"
)


def get_connection():
    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        raise Exception("DATABASE_URL is not configured.")

    return psycopg2.connect(database_url)


def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS answers (
            id SERIAL PRIMARY KEY,
            knows_me TEXT,
            likes_me TEXT,
            wants_date TEXT,
            date_place TEXT,
            date_choice TEXT,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    cursor.close()
    connection.close()


# Create database table when the server starts
try:
    create_table()
    print("Database table checked successfully.")
except Exception as error:
    print("Database initialization error:", error)


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

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO answers
            (
                knows_me,
                likes_me,
                wants_date,
                date_place,
                date_choice
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (

            data.get("knowsMe"),

            data.get("likesMe"),

            data.get("wantsDate"),

            data.get("datePlace"),

            data.get("date")

        ))

        connection.commit()

        cursor.close()

        connection.close()

        return jsonify({
            "success": True,
            "message": "Answers saved ❤️"
        })

    except Exception as error:

        print("Database error:", error)

        return jsonify({
            "success": False,
            "message": "Could not save answers."
        }), 500


# =====================================
# LOGIN
# =====================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        password = request.form.get("password")

        if password == ADMIN_PASSWORD:

            session["admin"] = True

            return redirect(
                url_for("answers")
            )

        return render_template(
            "login.html",
            error="Wrong password 😭"
        )

    return render_template("login.html")


# =====================================
# ANSWERS DASHBOARD
# =====================================

@app.route("/answers")
def answers():

    if not session.get("admin"):

        return redirect(
            url_for("login")
        )

    try:

        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        cursor.execute("""
            SELECT *
            FROM answers
            ORDER BY submitted_at DESC
        """)

        all_answers = cursor.fetchall()

        cursor.close()

        connection.close()

        return render_template(
            "answers.html",
            answers=all_answers
        )

    except Exception as error:

        print("Dashboard error:", error)

        return "Database error. Check Render logs.", 500


# =====================================
# LOGOUT
# =====================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )


# =====================================
# LOCAL DEVELOPMENT
# =====================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "change-this-secret-key"
)

ADMIN_PASSWORD = os.environ.get(
    "ADMIN_PASSWORD",
    "change-this-password"
)


def get_connection():
    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        raise Exception("DATABASE_URL is not configured.")

    return psycopg2.connect(database_url)


def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS answers (
            id SERIAL PRIMARY KEY,
            knows_me TEXT,
            likes_me TEXT,
            wants_date TEXT,
            date_place TEXT,
            date_choice TEXT,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    cursor.close()
    connection.close()


# Create database table when the server starts
try:
    create_table()
    print("Database table checked successfully.")
except Exception as error:
    print("Database initialization error:", error)


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

    try:

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO answers
            (
                knows_me,
                likes_me,
                wants_date,
                date_place,
                date_choice
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (

            data.get("knowsMe"),

            data.get("likesMe"),

            data.get("wantsDate"),

            data.get("datePlace"),

            data.get("date")

        ))

        connection.commit()

        cursor.close()

        connection.close()

        return jsonify({
            "success": True,
            "message": "Answers saved ❤️"
        })

    except Exception as error:

        print("Database error:", error)

        return jsonify({
            "success": False,
            "message": "Could not save answers."
        }), 500


# =====================================
# LOGIN
# =====================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        password = request.form.get("password")

        if password == ADMIN_PASSWORD:

            session["admin"] = True

            return redirect(
                url_for("answers")
            )

        return render_template(
            "login.html",
            error="Wrong password 😭"
        )

    return render_template("login.html")


# =====================================
# ANSWERS DASHBOARD
# =====================================

@app.route("/answers")
def answers():

    if not session.get("admin"):

        return redirect(
            url_for("login")
        )

    try:

        connection = get_connection()

        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        cursor.execute("""
            SELECT *
            FROM answers
            ORDER BY submitted_at DESC
        """)

        all_answers = cursor.fetchall()

        cursor.close()

        connection.close()

        return render_template(
            "answers.html",
            answers=all_answers
        )

    except Exception as error:

        print("Dashboard error:", error)

        return "Database error. Check Render logs.", 500


# =====================================
# LOGOUT
# =====================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )


# =====================================
# LOCAL DEVELOPMENT
# =====================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
