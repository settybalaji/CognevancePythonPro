def calculate_performance(student):
    marks = student.get("marks", {})
    values = list(marks.values())

    if not values:
        return 0, 0, "N/A"

    total = sum(values)
    average = total / len(values)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, average, grade


def print_performance(student):
    total, average, grade = calculate_performance(student)
    print(f"Student ID : {student['student_id']}")
    print(f"Name       : {student['name']}")
    print(f"Total      : {total:.2f} / 300")
    print(f"Average    : {average:.2f}%")
    print(f"Grade      : {grade}")
    print("-" * 40)
