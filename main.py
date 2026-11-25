from student_manager import StudentManager


def display_menu():
    print("\n" + "=" * 52)
    print("       STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 52)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Performance Report")
    print("7. Exit")
    print("=" * 52)


def main():
    manager = StudentManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        try:
            if choice == "1":
                manager.add_student()
            elif choice == "2":
                manager.view_students()
            elif choice == "3":
                manager.search_student()
            elif choice == "4":
                manager.update_student()
            elif choice == "5":
                manager.delete_student()
            elif choice == "6":
                manager.performance_report()
            elif choice == "7":
                print("\nThank you for using the Student Record Management System.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")
        except (EOFError, KeyboardInterrupt):
            print("\nApplication closed safely.")
            break
        except Exception as error:
            print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    main()
