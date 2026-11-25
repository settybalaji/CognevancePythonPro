def get_non_empty(prompt, current_value=None):
    while True:
        value = input(prompt).strip()
        if not value and current_value is not None:
            return current_value
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_age(prompt="Enter age: ", current_value=None):
    while True:
        value = input(prompt).strip()
        if not value and current_value is not None:
            return current_value
        try:
            age = int(value)
            if 3 <= age <= 100:
                return age
            print("Age must be between 3 and 100.")
        except ValueError:
            print("Please enter a valid whole number for age.")


def get_marks(prompt, current_value=None):
    while True:
        value = input(prompt).strip()
        if not value and current_value is not None:
            return current_value
        try:
            marks = float(value)
            if 0 <= marks <= 100:
                return round(marks, 2)
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number for marks.")


def get_email(prompt="Enter email: ", current_value=None):
    while True:
        value = input(prompt).strip()
        if not value and current_value is not None:
            return current_value
        if "@" in value and "." in value.split("@")[-1] and " " not in value:
            return value
        print("Please enter a valid email address.")


def get_student_details(existing=None):
    """Collect new details or update existing details by pressing Enter."""
    existing = existing or {}
    print("For updates, press Enter to keep the existing value.")
    name = get_non_empty(
        f"Enter name [{existing.get('name', '')}]: ",
        existing.get("name")
    )
    age = get_age(
        f"Enter age [{existing.get('age', '')}]: ",
        existing.get("age")
    )
    course = get_non_empty(
        f"Enter course [{existing.get('course', '')}]: ",
        existing.get("course")
    )
    email = get_email(
        f"Enter email [{existing.get('email', '')}]: ",
        existing.get("email")
    )

    print("Enter marks out of 100:")
    marks = {}
    for subject in ("Python", "Database", "Computer Networks"):
        old_mark = existing.get("marks", {}).get(subject)
        suffix = f" [{old_mark}]" if old_mark is not None else ""
        marks[subject] = get_marks(
            f"{subject}{suffix}: ",
            old_mark
        )

    return {
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "marks": marks
    }
