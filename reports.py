import database
import progress


def generate_report():

    subjects = database.get_subjects()
    sessions = database.get_study_sessions()
    data = progress.get_progress()

    print("\n")
    print("==========================================")
    print("          SMART STUDY PLANNER")
    print("             PROGRESS REPORT")
    print("==========================================")

    print("\nSUBJECTS")
    print("------------------------------------------")

    if subjects:

        for subject_id, name in subjects:
            print(f"{subject_id}. {name}")

    else:
        print("No subjects available.")

    print("\nTASK SUMMARY")
    print("------------------------------------------")

    print(f"Total Tasks      : {data['total_tasks']}")
    print(f"Completed Tasks  : {data['completed_tasks']}")
    print(f"Pending Tasks    : {data['pending_tasks']}")
    print(f"Completion       : {data['completion_percentage']:.2f}%")

    print("\nSTUDY TIME")
    print("------------------------------------------")

    print(f"Total Study Time : {data['total_study_time']} minutes")
    print(f"Study Sessions   : {len(sessions)}")

    print("\n==========================================")
    print("              END OF REPORT")
    print("==========================================")


def save_report():

    subjects = database.get_subjects()
    sessions = database.get_study_sessions()
    data = progress.get_progress()

    with open(
        "study_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("SMART STUDY PLANNER\n")
        file.write("====================\n\n")

        file.write("SUBJECTS\n")
        file.write("--------------------\n")

        if subjects:

            for subject_id, name in subjects:
                file.write(
                    f"{subject_id}. {name}\n"
                )

        else:
            file.write(
                "No subjects available.\n"
            )

        file.write("\nTASK SUMMARY\n")
        file.write("--------------------\n")

        file.write(
            f"Total Tasks: {data['total_tasks']}\n"
        )

        file.write(
            f"Completed Tasks: "
            f"{data['completed_tasks']}\n"
        )

        file.write(
            f"Pending Tasks: "
            f"{data['pending_tasks']}\n"
        )

        file.write(
            f"Completion: "
            f"{data['completion_percentage']:.2f}%\n"
        )

        file.write("\nSTUDY TIME\n")
        file.write("--------------------\n")

        file.write(
            f"Total Study Time: "
            f"{data['total_study_time']} minutes\n"
        )

        file.write(
            f"Study Sessions: "
            f"{len(sessions)}\n"
        )

    print(
        "Report saved as study_report.txt"
    )