# Smart Study Planner

## 1. Project Overview

Smart Study Planner is a Python-based application designed to help students organize their academic activities.

The application allows students to manage subjects, create and track tasks, record study sessions, monitor progress, and generate study reports.

The project uses Python and SQLite and follows a modular structure with separate files for different functionalities.

## 2. Features

- Add, view, and delete subjects.
- Add, view, complete, and delete tasks.
- Set task deadlines and priorities.
- Record study sessions.
- View study sessions.
- Track total, completed, and pending tasks.
- Calculate task completion percentage.
- Track total study time.
- Generate and save study reports.
- Validate user inputs.
- Automated unit testing.

## 3. Technologies / Tools Used

- **Python** – Application development
- **SQLite** – Database management
- **Python unittest** – Automated testing
- **Git** – Version control
- **GitHub** – Source code repository
- **Visual Studio Code** – Development environment

No external Python packages are required.

## 4. Steps to Install & Run the Project

### Requirements

- Python 3.x
- Git
- Visual Studio Code

### Installation

Clone the GitHub repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Open the project folder in Visual Studio Code.

### Run the Project

Open the terminal in the project folder and run:

```bash
python main.py
```

The Smart Study Planner menu will appear.

### Testing

The project includes automated tests using Python's `unittest` framework.

Open the terminal in the project folder and run:

```bash
python -m unittest discover -s tests -v
```

A successful test run should end with:

```text
OK
```
