from flask import Flask, render_template, request, send_file
import json
from utils import write_name, get_db
from werkzeug.local import LocalProxy

app = Flask(__name__)

app.template_folder = "templates"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/submitform", methods=["POST"])
def submitform():
    data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "branch": request.form["branch"],
        "q1rating": int(request.form["q1rating"]),
        "q2rating": int(request.form["q2rating"]),
        "q3rating": int(request.form["q3rating"]),
        "q4rating": int(request.form["q4rating"]),
        "q5rating": int(request.form["q5rating"]),
        "certificate": write_name(request.form["name"], request.form["branch"]),
    }
    db = LocalProxy(get_db)
    db.responses.insert_one(data)
    return render_template("submitform.html", certificate=data["certificate"])


@app.route("/certificates/<name>")
def certificates(name):
    cert_file = f"certificates/{name}"
    return send_file(cert_file, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
