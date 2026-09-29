import database


def get_progress():

    total_tasks, completed_tasks = database.get_task_progress()

    pending_tasks = total_tasks - completed_tasks

    total_study_time = database.get_total_study_time()

    if total_tasks > 0:
        completion_percentage = (
            completed_tasks / total_tasks
        ) * 100
    else:
        completion_percentage = 0

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_percentage": completion_percentage,
        "total_study_time": total_study_time
    }


def view_progress():

    data = get_progress()

    print("\n================================")
    print("        STUDY PROGRESS")
    print("================================")

    print(f"Total Tasks       : {data['total_tasks']}")
    print(f"Completed Tasks   : {data['completed_tasks']}")
    print(f"Pending Tasks     : {data['pending_tasks']}")
    print(f"Task Completion   : {data['completion_percentage']:.2f}%")
    print(f"Total Study Time  : {data['total_study_time']} minutes")