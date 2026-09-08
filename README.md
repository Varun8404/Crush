# 💌 A Little Something For You ❤️

A small romantic interactive quiz website made with **Python Flask, HTML, CSS and JavaScript**.

## ✨ Features

* 💌 Romantic welcome screen
* 👀 "Do you know me?"
* 🥰 "Do you like me?"
* 🌹 "Do you wanna go on a date?"
* 😈 The "No" button tries to escape
* ☕ Choose a date location
* 📅 Choose the date
* ❤️ Romantic final message
* 💾 Answers are saved using the Flask backend
* 📱 Mobile-friendly design
* 💕 Animated floating hearts

## 📁 Project Structure

```text
crush_website/
│
├── app.py
│
├── answers.json
│
├── requirements.txt
│
├── README.md
│
└── templates/
    └── index.html
```

## 🛠️ Requirements

You need:

* Python 3
* Flask
* A web browser

## 🚀 Run Locally

Open the project folder in VS Code.

Open the terminal and run:

```bash
pip install -r requirements.txt
```

Then start the Flask server:

```bash
python app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

Open this address in your browser:

```text
http://127.0.0.1:5000
```

## 💻 Run Without requirements.txt

If you don't have `requirements.txt`, install Flask directly:

```bash
pip install flask
```

Then:

```bash
python app.py
```

## 💾 Answers

After the quiz is completed, the submitted answers are stored in:

```text
answers.json
```

Example:

```json
[
    {
        "knowsMe": "Yes",
        "likesMe": "Yes",
        "wantsDate": "Yes",
        "datePlace": "☕ Cafe",
        "date": "2026-09-20",
        "time": "2026-09-09 23:30:00"
    }
]
```

## 🌐 Deploying Online

This project can be deployed to a Flask-compatible hosting service such as Render.

For deployment, make sure `requirements.txt` contains:

```text
Flask
gunicorn
```

Use:

```bash
pip install -r requirements.txt
```

as the build command and:

```bash
gunicorn app:app
```

as the start command.

## ❤️ Credits

Made with Python, HTML, CSS, JavaScript and a little bit of love.

> "Some questions are easy to answer.
> Some are meant to change everything. ❤️"
