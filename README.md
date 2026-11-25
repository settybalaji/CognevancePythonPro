# Student Record Management System

A menu-driven Python application for managing student records using JSON file handling. This project is suitable for a beginner-level Python programming assignment.

## Features
- Add, view, search, update and delete student records (CRUD).
- Automatically generated student IDs (STU001, STU002, ...).
- Stores records in `data/students.json`.
- Validates names, age, email and marks.
- Calculates total marks, average and grade.
- Displays individual and class performance reports.
- Uses separate Python modules for clean organization.

## Requirements
- Python 3.9 or newer
- Visual Studio Code
- Python extension for VS Code (Microsoft)
- No third-party Python packages are required.

## Setup and execution
1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the VS Code terminal (`Terminal` > `New Terminal`).
4. Confirm Python is installed:
   ```bash
   python --version
   ```
   On some macOS/Linux systems, use `python3 --version`.
5. Run the application:
   ```bash
   python main.py
   ```
   On macOS/Linux, if needed:
   ```bash
   python3 main.py
   ```

## Project structure
```text
cognevance_student_record_management_system/
├── main.py
├── student_manager.py
├── storage.py
├── validators.py
├── reports.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── .gitignore
└── data/
    └── students.json
```

## Modules
- `main.py`: Displays the menu and routes the user's selection.
- `student_manager.py`: Implements student CRUD operations and reports.
- `storage.py`: Loads and saves JSON data.
- `validators.py`: Validates user input and collects student details.
- `reports.py`: Calculates totals, averages and grades.
- `data/students.json`: Persistent student data file.

## Grade calculation
| Average | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

The average is calculated from three subjects: Python, Database and Computer Networks.

## Data and privacy
The application stores student information locally in a JSON file. Use fictional data for demonstrations. Do not commit real student personal information to a public GitHub repository.

## Testing checklist
- Add a student with valid details.
- Try invalid age, email and marks.
- View all records.
- Search using a student ID and part of a name.
- Update a student's details.
- Delete a record and test cancellation.
- Generate a performance report.
- Close and reopen the program to confirm records persist.

## Limitations and future enhancements
This is a local, single-user console application. Future versions could add a graphical interface, login roles, CSV/PDF exports, database storage and attendance management.

## Author
Student project prepared for Cognevance Technologies – Python Programming, Level 1.
# CognevancePythonPro
