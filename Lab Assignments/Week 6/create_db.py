from app import (
    app,
    db,
    Course,
    Student,
    Enrollment,
)

with app.app_context():
    db.create_all()

    course1 = Course(
        course_name="Introduction to Programming",
        course_code="CS101",
        course_description="Learn the basics of programming.",
    )
    course2 = Course(
        course_name="Data Structures",
        course_code="CS102",
        course_description="Learn about data structures.",
    )

    student1 = Student(roll_number="S001", first_name="John", last_name="Doe")
    student2 = Student(roll_number="S002", first_name="Jane", last_name="Smith")

    enrollment1 = Enrollment(student_id=1, course_id=1)
    enrollment2 = Enrollment(student_id=2, course_id=2)

    db.session.add(course1)
    db.session.add(course2)
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(enrollment1)
    db.session.add(enrollment2)

    db.session.commit()

    print("Database Created")
