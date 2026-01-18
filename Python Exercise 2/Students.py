# List to store student records
students = []


def add_student(name, math, information, english):
    """Add a new student with their scores."""
    students.append({
        "name": name,
        "math": math,
        "information": information,
        "english": english
    })


def average_score(student):
    """Calculate and print average score for a student."""
    average = (student["math"] + student["information"] + student["english"]) / 3
    print(f"Average score for student \"{student['name']}\" is: {average}")


# Add sample students
add_student("Cefer Nadirov", 4, 4, 3)
add_student("Salami Niyam", 5, 4, 2)
add_student("Qedir Qizilses", 2, 3, 5)
add_student("Isfendiyar Insaat", 2, 3, 2)

# Calculate and print average for each student
for student in students:
    average_score(student)
