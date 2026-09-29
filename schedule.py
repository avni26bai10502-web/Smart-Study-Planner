import database
import validation


def add_study_session():
    subject = input("Enter subject: ").strip()
    study_date = input("Enter study date (DD-MM-YYYY): ").strip()
    duration = input("Enter study duration in minutes: ").strip()

    if not validation.validate_text(subject):
        print("Subject cannot be empty.")
        return

    if not validation.validate_date(study_date):
        print("Invalid date. Use DD-MM-YYYY.")
        return

    if not validation.validate_duration(duration):
        print("Duration must be a positive number.")
        return

    duration = int(duration)

    database.add_study_session(
        subject,
        study_date,
        duration
    )

    print("Study session added successfully!")


def view_study_sessions():
    sessions = database.get_study_sessions()

    if not sessions:
        print("No study sessions added yet.")
        return

    print("\n========== STUDY SCHEDULE ==========")

    for session in sessions:

        session_id, subject, date, duration = session

        print("\n------------------------------")
        print(f"ID       : {session_id}")
        print(f"Subject  : {subject}")
        print(f"Date     : {date}")
        print(f"Duration : {duration} minutes")