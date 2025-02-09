from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

data_file = "data.csv"

def load_data():
    return pd.read_csv(data_file)

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        data = load_data()
        search_type = request.form.get("ID")
        search_value = request.form.get("id_value").strip()

        if search_type == "student_id":
            if not search_value.isdigit():
                error = "Invalid Student ID. Please enter a numeric Student ID."
            else:
                student_data = data[data["Student ID"] == int(search_value)]
                if student_data.empty:
                    error = "No records found for the given Student ID."
                else:
                    total_marks = student_data["Marks"].sum()
                    return render_template("student_details.html", records=student_data.to_dict(orient="records"), total=total_marks)
        
        elif search_type == "course_id":
            course_data = data[data["Course ID"] == search_value]
            if course_data.empty:
                error = "No records found for the given Course ID."
            else:
                avg_marks = round(course_data["Marks"].mean(), 2)
                max_marks = course_data["Marks"].max()
                plot_histogram(course_data["Marks"], search_value)
                return render_template("course_details.html", avg=avg_marks, max=max_marks, course_id=search_value)
        else:
            error = "Please select an option and enter a valid ID."

    return render_template("index.html", error=error)

def plot_histogram(marks, course_id):
    plt.figure()
    plt.hist(marks, bins=5, edgecolor='black')
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.title(f"Marks Distribution for {course_id}")
    plt.savefig("static/histogram.png")
    plt.close()

if __name__ == "__main__":
    app.run(debug=True)