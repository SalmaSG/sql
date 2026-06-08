"""
Introduction to Matplotlib

Matplotlib is a Python library used to create charts and graphs.
It is commonly used for data visualization in science, engineering,
statistics, and general data analysis.
"""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


# Sample data: number of students in different subjects
subjects = ["Math", "Science", "English", "Computer"]
students = [35, 42, 30, 48]


# Create a bar chart
plt.bar(subjects, students, color="skyblue")


# Add title and labels
plt.title("Students by Subject")
plt.xlabel("Subjects")
plt.ylabel("Number of Students")


# Save the chart as an image file
plt.savefig("students_by_subject.png")
print("Chart saved as students_by_subject.png")
