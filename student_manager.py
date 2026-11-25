from storage import load_students, save_students
from validators import get_student_details
from reports import calculate_performance, print_performance


class StudentManager:
    def __init__(self):
        self.students = load_students()

    def refresh(self):
        self.students = load_students()

    def next_student_id(self):
        highest = 0
        for student in self.students:
            student_id = student.get("student_id", "")
            if student_id.startswith("STU") and student_id[3:].isdigit():
                highest = max(highest, int(student_id[3:]))
        return f"STU{highest + 1:03d}"

    def add_student(self):
        print("\n--- Add New Student ---")
        details = get_student_details()
        student = {"student_id": self.next_student_id(), **details}
        self.students.append(student)
        save_students(self.students)
        print(f"Student added successfully. Student ID: {student['student_id']}")

    def view_students(self):
        self.refresh()
        print("\n--- All Student Records ---")
        if not self.students:
            print("No student records found.")
            return

        print(f"{'ID':<10} {'NAME':<22} {'COURSE':<20} {'AVERAGE':>9} {'GRADE':>7}")
        print("-" * 75)
        for student in self.students:
            _, average, grade = calculate_performance(student)
            print(
                f"{student['student_id']:<10} "
                f"{student['name'][:21]:<22} "
                f"{student['course'][:19]:<20} "
                f"{average:>8.2f}% {grade:>7}"
            )

    def search_student(self):
        self.refresh()
        term = input("\nEnter student ID or name to search: ").strip().lower()
        if not term:
            print("Search value cannot be empty.")
            return

        matches = [
            student for student in self.students
            if term in student.get("student_id", "").lower()
            or term in student.get("name", "").lower()
        ]

        if not matches:
            print("No matching student found.")
            return

        for student in matches:
            self.show_student_details(student)

    def show_student_details(self, student):
        print("\n" + "-" * 40)
        print(f"Student ID : {student['student_id']}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Course     : {student['course']}")
        print(f"Email      : {student['email']}")
        print("Marks:")
        for subject, mark in student.get("marks", {}).items():
            print(f"  {subject}: {mark:.2f}")
        print_performance(student)

    def find_by_id(self, student_id):
        return next(
            (student for student in self.students
             if student.get("student_id", "").lower() == student_id.lower()),
            None
        )

    def update_student(self):
        self.refresh()
        student_id = input("\nEnter the student ID to update: ").strip()
        student = self.find_by_id(student_id)

        if not student:
            print("Student ID not found.")
            return

        print(f"Updating record for {student['name']}.")
        updated_details = get_student_details(student)
        student.update(updated_details)
        save_students(self.students)
        print("Student record updated successfully.")

    def delete_student(self):
        self.refresh()
        student_id = input("\nEnter the student ID to delete: ").strip()
        student = self.find_by_id(student_id)

        if not student:
            print("Student ID not found.")
            return

        confirmation = input(
            f"Are you sure you want to delete {student['name']}? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            self.students.remove(student)
            save_students(self.students)
            print("Student record deleted successfully.")
        else:
            print("Delete operation cancelled.")

    def performance_report(self):
        self.refresh()
        print("\n--- Student Performance Report ---")
        if not self.students:
            print("No student records available for reporting.")
            return

        for student in self.students:
            print_performance(student)

        averages = [calculate_performance(s)[1] for s in self.students]
        class_average = sum(averages) / len(averages)
        top_student = max(self.students, key=lambda s: calculate_performance(s)[1])

        print(f"Number of students : {len(self.students)}")
        print(f"Class average      : {class_average:.2f}%")
        print(
            f"Top performer      : {top_student['name']} "
            f"({calculate_performance(top_student)[1]:.2f}%)"
        )
