# Smart Study Planner

## 1. Project Overview

Smart Study Planner is a Python-based study management application designed to help students organize their subjects, assignments, study sessions, and academic progress.

The application uses Python, SQLite, and a modular software structure.

---

## 2. Problem Statement

Students often have multiple subjects, assignments, deadlines, and study sessions to manage.

Without a proper planning system, it can become difficult to keep track of pending work and study time.

The Smart Study Planner provides a simple system for managing academic activities in one place.

---

## 3. Objectives

The main objectives of the project are:

- Manage subjects.
- Manage assignments and tasks.
- Store task deadlines and priorities.
- Record study sessions.
- Track completed and pending tasks.
- Calculate study progress.
- Generate progress reports.
- Store information permanently using SQLite.
- Validate user input and handle errors.

---

## 4. Main Features

### Subject Management

Users can:

- Add subjects.
- View subjects.
- Delete subjects.

### Task Management

Users can:

- Add tasks.
- View tasks.
- Set deadlines.
- Set task priority.
- Mark tasks as completed.
- Delete tasks.

### Study Schedule

Users can:

- Add study sessions.
- Record study dates.
- Record study duration.
- View previous study sessions.

### Progress Tracking

The application calculates:

- Total tasks.
- Completed tasks.
- Pending tasks.
- Task completion percentage.
- Total study time.

### Reports

Users can:

- Generate a progress report.
- Save the report as a text file.

### Validation

The application validates:

- Empty text.
- Dates.
- Task priorities.
- Study duration.
- IDs.

---

## 5. Technologies Used

- Python
- SQLite
- Tkinter can be added for the GUI version
- unittest
- Git and GitHub

The current version uses a command-line interface.

---

## 6. Project Structure

```text
Study Planner project/
│
├── main.py
├── database.py
├── subjects.py
├── tasks.py
├── schedule.py
├── progress.py
├── reports.py
├── validation.py
├── README.md
│
└── tests/
    └── test_planner.py