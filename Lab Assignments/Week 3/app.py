import csv
import sys

import matplotlib.pyplot as plt
from pyhtml import body, h1, head, html, img, p, table, td, th, title, tr


def read_csv(file_name):
    data = []
    try:
        with open(file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("Error : data.csv Not Found!")
        sys.exit(1)
    return data


def generate_student_html(student_id, data):
    student_records = [row for row in data if row["Student id"] == student_id]
    if not student_records:
        return generate_error_html("Invalid Student ID")

    total_marks = sum(int(row[" Marks"]) for row in student_records)

    doc = html(
        head(title("Student Details")),
        body(
            h1("Student Details"),
            table(
                tr(th("Student ID"), th("Course ID"), th("Marks")),
                *[
                    tr(td(row["Student id"]), td(row[" Course id"]), td(row[" Marks"]))
                    for row in student_records
                ],
                tr(td("Total Marks", {"colspan": "2"}), td(str(total_marks))),
            ),
        ),
    )
    return str(doc)


def generate_course_html(course_id, data):
    course_records = []

    print(course_id, data)

    for row in data:
        if row[" Course id"][1::] == course_id:
            course_records.append(int(row[" Marks"]))

    print(course_records)

    if not course_records:
        return generate_error_html("Invalid Course ID")

    avg_marks = sum(course_records) / len(course_records)
    max_marks = max(course_records)

    plt.hist(course_records, bins=10, edgecolor="black")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.title(f"Histogram For Course {course_id}")
    img_path = "Histogram.png"
    plt.savefig(img_path)
    plt.close()

    doc = html(
        head(title("Course Details")),
        body(
            h1("Course Details"),
            table(
                tr(th("Average Marks"), th("Maximum Marks")),
                tr(td(f"{avg_marks:.2f}"), td(str(max_marks))),
            ),
            img(src=img_path, alt="Histogram of Marks"),
        ),
    )
    return str(doc)


def generate_error_html(message):
    doc = html(head(title("Error")), body(h1("Error"), p(message)))
    return str(doc)


def main():
    if len(sys.argv) != 3:
        print("Usage : python app.py -s student_id OR python app.py -c course_id")
        sys.exit(1)

    option, identifier = sys.argv[1], sys.argv[2]
    data = read_csv("data.csv")

    if option == "-s":
        output = generate_student_html(identifier, data)
    elif option == "-c":
        output = generate_course_html(identifier, data)
    else:
        output = generate_error_html("Invalid Option Provided")

    with open("output.html", "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n" + output)

    print("HTML File Generated : output.html")

    if option == "-c":
        print("Histogram Generated : histogram.png")


if __name__ == "__main__":
    main()
