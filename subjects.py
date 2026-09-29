import database
import validation


def add_subject():
    name = input("Enter subject name: ").strip()

    if not validation.validate_text(name):
        print("Subject name cannot be empty.")
        return

    success = database.add_subject(name)

    if success:
        print("Subject added successfully!")
    else:
        print("Subject already exists.")


def view_subjects():
    subjects = database.get_subjects()

    if not subjects:
        print("No subjects added yet.")
        return

    print("\n========== YOUR SUBJECTS ==========")

    for subject_id, name in subjects:
        print(f"{subject_id}. {name}")


def delete_subject():
    subjects = database.get_subjects()

    if not subjects:
        print("No subjects to delete.")
        return

    view_subjects()

    subject_id = input("\nEnter subject ID to delete: ")

    if not validation.validate_id(subject_id):
        print("Please enter a valid ID.")
        return

    deleted = database.delete_subject(int(subject_id))

    if deleted:
        print("Subject deleted successfully!")
    else:
        print("Subject ID not found.")