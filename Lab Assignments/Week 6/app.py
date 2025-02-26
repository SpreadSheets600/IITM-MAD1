from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource, reqparse, abort
from exceptions import CourseException, StudentException, EnrollmentException

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api_database.sqlite3"
db = SQLAlchemy(app)
api = Api(app)


class Course(db.Model):
    __tablename__ = "course"
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String, nullable=False)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_description = db.Column(db.String)


class Student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)


class Enrollment(db.Model):
    __tablename__ = "enrollment"
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(
        db.Integer, db.ForeignKey("student.student_id"), nullable=False
    )
    course_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)


class CourseResource(Resource):
    def get(self, course_id):
        course = Course.query.get(course_id)
        if course is None:
            return make_response("", 404)
        return jsonify(
            course_id=course.course_id,
            course_name=course.course_name,
            course_code=course.course_code,
            course_description=course.course_description,
        )

    def put(self, course_id):
        data = request.get_json()

        course = Course.query.get(course_id)
        if not course:
            return make_response("", 404)

        if "course_name" not in data:
            raise CourseException("COURSE001", 400)
        if "course_code" not in data:
            raise CourseException("COURSE002", 400)
        if Course.query.filter(
            Course.course_code == data["course_code"], Course.course_id != course_id
        ).first():
            return make_response("", 409)

        course.course_name = data.get("course_name", course.course_name)
        course.course_code = data.get("course_code", course.course_code)
        course.course_description = data.get(
            "course_description", course.course_description
        )
        db.session.commit()
        return jsonify(
            course_id=course.course_id,
            course_name=course.course_name,
            course_code=course.course_code,
            course_description=course.course_description,
        )

    def delete(self, course_id):
        course = Course.query.get(course_id)
        if not course:
            return make_response("", 404)
        db.session.delete(course)
        db.session.commit()
        return make_response("", 200)

    def post(self):
        data = request.get_json()

        if "course_name" not in data:
            raise CourseException("COURSE001", 400)
        if "course_code" not in data:
            raise CourseException("COURSE002", 400)

        if Course.query.filter_by(course_code=data["course_code"]).first():
            return make_response("", 409)

        new_course = Course(
            course_name=data["course_name"],
            course_code=data["course_code"],
            course_description=data.get("course_description"),
        )
        db.session.add(new_course)
        db.session.commit()

        added_course = (
            db.session.query(Course).filter_by(course_id=new_course.course_id).first()
        )

        response = jsonify(
            course_id=added_course.course_id,
            course_name=added_course.course_name,
            course_code=added_course.course_code,
            course_description=added_course.course_description,
        )
        response.status_code = 201
        return response


class StudentResource(Resource):
    def get(self, student_id):
        student = Student.query.get(student_id)
        if not student:
            return make_response("", 404)

        return jsonify(
            student_id=student.student_id,
            roll_number=student.roll_number,
            first_name=student.first_name,
            last_name=student.last_name,
        )

    def put(self, student_id):
        data = request.get_json()

        student = Student.query.get(student_id)
        if not student:
            return make_response("", 404)

        if "roll_number" not in data:
            raise StudentException("STUDENT001", 400)
        if "first_name" not in data:
            raise StudentException("STUDENT002", 400)
        if Student.query.filter(
            Student.roll_number == data["roll_number"], Student.student_id != student_id
        ).first():
            return make_response("", 409)

        student.first_name = data.get("first_name", student.first_name)
        student.last_name = data.get("last_name", student.last_name)
        student.roll_number = data.get("roll_number", student.roll_number)
        db.session.commit()
        return jsonify(
            student_id=student.student_id,
            roll_number=student.roll_number,
            first_name=student.first_name,
            last_name=student.last_name,
        )

    def delete(self, student_id):
        student = Student.query.get(student_id)
        if not student:
            return make_response("", 404)
        db.session.delete(student)
        db.session.commit()
        return make_response("", 200)

    def post(self):
        data = request.get_json()

        if "roll_number" not in data:
            raise StudentException("STUDENT001", 400)
        if "first_name" not in data:
            raise StudentException("STUDENT002", 400)

        if Student.query.filter_by(roll_number=data["roll_number"]).first():
            return make_response("", 409)

        new_student = Student(
            roll_number=data["roll_number"],
            first_name=data["first_name"],
            last_name=data.get("last_name"),
        )
        db.session.add(new_student)
        db.session.commit()

        added_student = (
            db.session.query(Student)
            .filter_by(student_id=new_student.student_id)
            .first()
        )

        response = jsonify(
            student_id=added_student.student_id,
            roll_number=added_student.roll_number,
            first_name=added_student.first_name,
            last_name=added_student.last_name,
        )
        response.status_code = 201
        return response


class EnrollmentResource(Resource):
    def get(self, student_id):
        student = Student.query.get(student_id)
        if not student:
            raise StudentException("ENROLLMENT002", 400)
        enrollments = Enrollment.query.filter_by(student_id=student_id).all()
        if not enrollments:
            return make_response("", 404)
        courses = [
            {
                "enrollment_id": enrollment.enrollment_id,
                "student_id": enrollment.student_id,
                "course_id": enrollment.course_id,
            }
            for enrollment in enrollments
        ]

        return jsonify(courses)

    def post(self, student_id):
        data = request.get_json()
        student = Student.query.get(student_id)
        if not student:
            return make_response("", 404)
        if "course_id" not in data:
            raise EnrollmentException("ENROLLMENT003", 400)
        course = Course.query.get(data["course_id"])
        if not course:
            raise EnrollmentException("ENROLLMENT001", 400)
        if Enrollment.query.filter_by(
            student_id=student_id, course_id=data["course_id"]
        ).first():
            return make_response("", 409)

        new_enrollment = Enrollment(student_id=student_id, course_id=data["course_id"])
        db.session.add(new_enrollment)
        db.session.commit()

        enrollments = Enrollment.query.filter_by(student_id=student_id).all()
        courses = [
            {
                "enrollment_id": enrollment.enrollment_id,
                "student_id": enrollment.student_id,
                "course_id": enrollment.course_id,
            }
            for enrollment in enrollments
        ]

        response = jsonify(courses)
        response.status_code = 201
        return response

    def delete(self, student_id, course_id):
        student = Student.query.get(student_id)
        if not student:
            raise EnrollmentException("ENROLLMENT002", 400)
        course = Course.query.get(course_id)
        if not course:
            raise EnrollmentException("ENROLLMENT001", 400)

        enrollment = Enrollment.query.filter_by(
            student_id=student_id, course_id=course_id
        ).first()
        if not enrollment:
            return make_response("", 404)

        db.session.delete(enrollment)
        db.session.commit()

        return make_response("", 200)


api.add_resource(CourseResource, "/api/course", "/api/course/<int:course_id>")
api.add_resource(StudentResource, "/api/student", "/api/student/<int:student_id>")
api.add_resource(
    EnrollmentResource,
    "/api/student/<int:student_id>/course",
    "/api/student/<int:student_id>/course/<int:course_id>",
)

if __name__ == "__main__":
    app.run(debug=True)
