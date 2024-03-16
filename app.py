from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index_page():
    with open("static/skills.json") as json_file:
        skills_data = json.load(json_file)
    return render_template("index.html", courses=skills_data)


@app.route("/skill")
def skill_page():
    with open("static/skills.json") as json_file:
        skills_data = json.load(json_file)
    course_type = request.args.get("course_type")
    return render_template("courseSkill.html", course_type=course_type, skills=skills_data)


if __name__ == '__main__':
    app.run(debug=True)
