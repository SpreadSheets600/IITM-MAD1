from flask import render_template, redirect, request, Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

COURSE_MAP = {"course_1": 1, "course_2": 2, "course_3": 3, "course_4": 4}


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String(200), nullable=False, unique=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200))


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String(200), nullable=False, unique=True)
    course_name = db.Column(db.String(200), nullable=False)
    course_description = db.Column(db.String(200))


class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
def home():
    students = Student.query.all()
    return render_template("home.html", students=students)


@app.route("/student/create", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")

    roll_number = request.form["roll"]
    first_name = request.form["f_name"]
    last_name = request.form["l_name"]

    existing_student = Student.query.filter_by(roll_number=roll_number).first()
    if existing_student:
        return render_template("exists.html")

    new_student = Student(
        roll_number=roll_number, first_name=first_name, last_name=last_name
    )
    db.session.add(new_student)
    db.session.commit()

    student = Student.query.filter_by(roll_number=roll_number).first()

    courses = request.form.getlist("courses")
    for course in courses:
        course_id = COURSE_MAP.get(course)
        if course_id:
            enrollment = Enrollment(student_id=student.id, course_id=course_id)
            db.session.add(enrollment)
    db.session.commit()

    return redirect("/")


@app.route("/student/<int:student_id>/", methods=["GET"])
def view(student_id):
    student = Student.query.filter_by(id=student_id).first_or_404()
    enrollments = Enrollment.query.filter_by(student_id=student_id).all()
    courses = [
        Course.query.filter_by(id=enrollment.course_id).first()
        for enrollment in enrollments
    ]
    return render_template("about.html", courses=courses, student=student)


@app.route("/student/<int:student_id>/update", methods=["GET", "POST"])
def update(student_id):
    student = Student.query.filter_by(id=student_id).first_or_404()

    if request.method == "GET":
        enrollments = Enrollment.query.filter_by(student_id=student_id).all()
        enrolled_course_ids = [enrollment.course_id for enrollment in enrollments]
        return render_template("update.html", row=student, cid=enrolled_course_ids)

    student.first_name = request.form["f_name"]
    student.last_name = request.form["l_name"]

    Enrollment.query.filter_by(student_id=student_id).delete()
    for course in request.form.getlist("courses"):
        course_id = COURSE_MAP.get(course)
        if course_id:
            db.session.add(Enrollment(student_id=student_id, course_id=course_id))
    db.session.commit()

    return redirect("/")


@app.route("/student/<int:student_id>/delete", methods=["POST"])
def delete(student_id):
    Student.query.filter_by(id=student_id).delete()
    Enrollment.query.filter_by(student_id=student_id).delete()
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
