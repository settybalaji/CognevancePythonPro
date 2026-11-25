import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "students.json"


def load_students():
    """Load student records from the JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("The student data file must contain a JSON list.")
        return data
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Could not read {DATA_FILE.name}. The JSON file may be damaged."
        ) from error


def save_students(students):
    """Save all student records to the JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_file = DATA_FILE.with_suffix(".tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)

    temporary_file.replace(DATA_FILE)
