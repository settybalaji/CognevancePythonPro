# Project Report: Student Record Management System

## 1. Title
Student Record Management System

## 2. Introduction
The Student Record Management System is a Python-based application designed to store and manage student information. It provides a simple menu-driven interface to add, view, search, update and delete student records. The application uses JSON file handling to store data permanently.

## 3. Problem Statement
Maintaining student information manually can take time and may lead to mistakes or misplaced records. A simple computerized system is required to organize student details, make searching easier and calculate academic performance.

## 4. Objectives
1. Develop a menu-driven Python application.
2. Perform add, view, search, update and delete operations.
3. Store student information using file handling.
4. Validate user inputs and handle exceptions.
5. Calculate student totals, averages and grades.

## 5. Scope
The application manages basic student details, course information, email addresses and marks in three subjects. It is intended for local demonstration and beginner-level academic use. It does not connect to a live institutional database.

## 6. Software and Hardware Requirements
### Software
- Python 3.9 or newer
- Visual Studio Code
- VS Code Python extension
- JSON for local data storage

### Hardware
- Computer or laptop
- 4 GB RAM recommended
- Basic disk space for Python and project files

## 7. System Modules
1. Main menu module – accepts user choices.
2. Student management module – performs CRUD operations.
3. Storage module – reads and writes JSON records.
4. Validation module – checks user input.
5. Report module – calculates academic performance.

## 8. System Workflow
1. Start the application.
2. Load existing records from the JSON file.
3. Display the main menu.
4. Accept the user's menu choice.
5. Perform the selected student operation.
6. Save changes to the JSON file.
7. Display the result and return to the menu.
8. Exit when the user selects Exit.

## 9. Data Fields
Each student record contains:
- Student ID
- Name
- Age
- Course
- Email
- Python marks
- Database marks
- Computer Networks marks

## 10. Performance Calculation
Total marks are calculated by adding the three subject marks. Average is total marks divided by three. Grades are assigned as follows: A+ (90–100), A (80–89.99), B (70–79.99), C (60–69.99), D (50–59.99), and F (below 50).

## 11. Testing
| Test case | Expected result |
|---|---|
| Add valid student | Student is saved and an ID is generated |
| Enter invalid age | Validation message is displayed |
| Enter invalid marks | User is asked to enter marks from 0 to 100 |
| View students | Stored records are displayed |
| Search existing student | Matching record is displayed |
| Search unknown student | No matching student message is displayed |
| Update existing student | Changes are saved |
| Delete and confirm | Record is removed |
| Cancel deletion | Record remains unchanged |
| Generate report | Total, average and grade are displayed |
| Restart application | Previously saved records are loaded |

## 12. Advantages
- Simple and easy to use.
- Reduces manual record maintenance.
- Searches student records quickly.
- Calculates performance automatically.
- Stores information persistently in a local file.
- Uses modular programming for easier maintenance.

## 13. Limitations
- Console-based interface only.
- Local JSON storage is not intended for simultaneous multi-user access.
- No authentication or role management.
- Reports are displayed in the terminal.

## 14. Future Enhancements
A graphical user interface, database integration, user authentication, attendance tracking and PDF/Excel report export can be added in future versions.

## 15. Conclusion
The Student Record Management System demonstrates how Python programming concepts can be applied to a practical record-management problem. It uses functions, modules, file handling, CRUD operations, input validation and exception handling. The system makes basic student record management easier and provides automatic academic performance calculations.
