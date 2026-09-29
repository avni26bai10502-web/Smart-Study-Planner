import sqlite3

DATABASE_NAME = "study_planner.db"


def set_database(database_name):
    global DATABASE_NAME
    DATABASE_NAME = database_name


def connect_db():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            deadline TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            study_date TEXT NOT NULL,
            duration INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_subject(name):
    connection = connect_db()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO subjects (name) VALUES (?)",
            (name,)
        )
        connection.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        connection.close()


def get_subjects():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name FROM subjects ORDER BY id"
    )

    subjects = cursor.fetchall()

    connection.close()

    return subjects


def delete_subject(subject_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM subjects WHERE id = ?",
        (subject_id,)
    )

    deleted = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return deleted


def add_task(name, subject, deadline, priority):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (name, subject, deadline, priority, status)
        VALUES (?, ?, ?, ?, ?)
    """, (name, subject, deadline, priority, "Pending"))

    connection.commit()

    task_id = cursor.lastrowid

    connection.close()

    return task_id


def get_tasks():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, subject, deadline, priority, status
        FROM tasks
        ORDER BY id
    """)

    tasks = cursor.fetchall()

    connection.close()

    return tasks


def complete_task(task_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = 'Completed'
        WHERE id = ?
    """, (task_id,))

    updated = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return updated


def delete_task(task_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    deleted = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return deleted


def add_study_session(subject, study_date, duration):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO study_sessions
        (subject, study_date, duration)
        VALUES (?, ?, ?)
    """, (subject, study_date, duration))

    connection.commit()

    session_id = cursor.lastrowid

    connection.close()

    return session_id


def get_study_sessions():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, subject, study_date, duration
        FROM study_sessions
        ORDER BY id
    """)

    sessions = cursor.fetchall()

    connection.close()

    return sessions


def get_task_progress():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total_tasks = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'Completed'
    """)

    completed_tasks = cursor.fetchone()[0]

    connection.close()

    return total_tasks, completed_tasks


def get_total_study_time():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT SUM(duration) FROM study_sessions"
    )

    result = cursor.fetchone()[0]

    connection.close()

    if result is None:
        return 0

    return result


create_tables()