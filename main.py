import database
import subjects
import tasks
import schedule
import progress
import reports


def show_menu():
    print("\n")
    print("================================")
    print("       SMART STUDY PLANNER")
    print("================================")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Delete Subject")
    print("4. Add Task")
    print("5. View Tasks")
    print("6. Complete Task")
    print("7. Delete Task")
    print("8. Add Study Session")
    print("9. View Study Sessions")
    print("10. View Progress")
    print("11. Generate Report")
    print("12. Save Report")
    print("13. Exit")


def main():
    database.create_tables()

    while True:
        show_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            subjects.add_subject()

        elif choice == "2":
            subjects.view_subjects()

        elif choice == "3":
            subjects.delete_subject()

        elif choice == "4":
            tasks.add_task()

        elif choice == "5":
            tasks.view_tasks()

        elif choice == "6":
            tasks.complete_task()

        elif choice == "7":
            tasks.delete_task()

        elif choice == "8":
            schedule.add_study_session()

        elif choice == "9":
            schedule.view_study_sessions()

        elif choice == "10":
            progress.view_progress()

        elif choice == "11":
            reports.generate_report()

        elif choice == "12":
            reports.save_report()

        elif choice == "13":
            print("\nThank you for using Smart Study Planner!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 13.")


if __name__ == "__main__":
    main()