from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify

error_messages = {
    "COURSE001": "Course Name is required",
    "COURSE002": "Course Code is required",
    "STUDENT001": "Roll Number required",
    "STUDENT002": "First Name is required",
    "ENROLLMENT001": "Course does not exist",
    "ENROLLMENT002": "Student does not exist",
}


class CourseException(HTTPException):
    def __init__(self, error_code, status_code):
        message = {
            "error_code": error_code,
            "error_message": error_messages[error_code],
        }
        self.response = make_response(jsonify(message), status_code)


class StudentException(HTTPException):
    def __init__(self, error_code, status_code):
        message = {
            "error_code": error_code,
            "error_message": error_messages[error_code],
        }
        self.response = make_response(jsonify(message), status_code)


class EnrollmentException(HTTPException):
    def __init__(self, error_code, status_code):
        message = {
            "error_code": error_code,
            "error_message": error_messages[error_code],
        }
        self.response = make_response(jsonify(message), status_code)
