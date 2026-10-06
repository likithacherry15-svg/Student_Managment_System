# Student Management & Academic Tracker

A comprehensive, educational, console-based Python application designed to guide learners from basic Python syntax through advanced Object-Oriented Programming (OOP) concepts.

---

## 📌 Project Overview

**Student Management & Academic Tracker** is a modular menu-driven application built using **pure Python 3 (Standard Library only)**. It allows administrators to manage student records, subject enrollments, grades, attendance, search and filter records, and generate analytical academic performance reports.

---

## ✨ Features

- **Student Record Management**: Add, view, search, update, and delete regular students, graduate students, and scholarship students.
- **Subject & Marks Management**: Assign subjects, enter/update subject marks, compute aggregate totals, subject averages, letter grades (A+, A, B, C, D, F), and GPA (0.0 – 10.0 scale).
- **Attendance Tracking**: Record classes conducted vs. attended, calculate attendance percentages, and flag eligibility shortages (< 75%).
- **Academic Reporting**: Generate detailed individual reports (with polymorphic customization per student subclass) and class-wide analytical reports.
- **Search, Filter & Sort**: Flexible search (by ID, Name, Department), filter (Passed/Failed, Shortage, Department), and dynamic sorting using lambda functions.
- **Data Persistence**: Auto-saves and loads student data to and from JSON format (`data/students.json`).

---

## 🛠️ Technologies Used

- **Language**: Python 3 (Standard Library ONLY)
- **Built-in Modules**:
  - `json` (Data persistence)
  - `os` & `sys` (File path navigation and CLI control)
  - `re` (Regular expression data validation)
  - `datetime` (Timestamping attendance and report generation)
  - `abc` (Abstract Base Classes for Abstraction)
  - `functools` (`reduce` function for higher-order aggregation)

---

## 🎓 Concepts Covered

| Category | Concepts Demonstrated |
|---|---|
| **Python Basics** | Variables, Constants, Data types (`int`, `float`, `str`, `bool`), Type conversion, Input/Output, Operators (Arithmetic, Comparison, Logical, Assignment, Membership `in`, Identity `is`), String formatting & f-strings |
| **Control Flow** | Conditional statements (`if`, `elif`, `else`), Nested conditions, Ternary conditional expressions |
| **Loops** | `while` loops (Interactive menu loops), `for` loops, Nested loops, `break`, `continue`, `pass` |
| **Data Structures** | **Lists** (`append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse`, `len`), **Tuples** (Semester tuples & constants), **Sets** (Unique department sets & operations `union`, `intersection`, `difference`), **Dictionaries** (Nested student records, marks mapping) |
| **Functions** | Scope (local/global), Parameters, Return values, Default arguments, Keyword arguments (`**kwargs`), Positional args (`*args`) |
| **Comprehensions** | List comprehensions, Set comprehensions, Dictionary comprehensions |
| **Functional Tools** | `map()`, `filter()`, `functools.reduce()`, `zip()`, `enumerate()`, `lambda` functions |
| **String Handling** | `upper()`, `lower()`, `title()`, `strip()`, `split()`, `join()`, `replace()`, `startswith()`, `endswith()`, `find()`, Slicing |
| **Exception Handling** | `try`, `except`, `else`, `finally`, `raise`, Custom exception hierarchy (`StudentNotFoundError`, `InvalidMarksError`, `InvalidAttendanceError`, `DuplicateStudentError`) |
| **File Handling & JSON** | `open()`, `read()`, `write()`, Context managers (`with open`), `json.load()`, `json.dump()` |
| **OOP Architecture** | Encapsulation (Private attributes `__marks`, `__attendance`), Inheritance (`Person` -> `Student` -> `GraduateStudent` / `ScholarshipStudent`), Polymorphism (Method overriding `display_info()`, `generate_report()`), Abstraction (`AcademicRecord` inheriting `ABC`), `@classmethod`, `@staticmethod`, `@property` getters/setters, `__str__`, `__repr__` |

---

## 📂 Project Structure

```
student_management_system/
├── main.py                     # Main application menu entry point
├── models/                     # Object-Oriented Domain Models
│   ├── __init__.py             # Package initializer
│   ├── academic_record.py      # Abstract Base Class (Abstraction demo)
│   ├── person.py               # Parent class for biographical data
│   ├── course.py               # Course / Subject entity model
│   ├── attendance.py           # Attendance record tracking model
│   └── student.py              # Student, GraduateStudent & ScholarshipStudent classes
├── services/                   # Business Logic & Service Layer
│   ├── __init__.py
│   ├── student_service.py      # Student CRUD, filter, and sort services
│   ├── marks_service.py        # Subject assignment and marks calculation
│   ├── attendance_service.py   # Attendance management services
│   └── report_service.py       # Individual & analytical report generation
├── utils/                      # Utilities & Helpers
│   ├── __init__.py
│   ├── validators.py           # Input validation and regex verification
│   ├── file_handler.py         # JSON file reading & writing utilities
│   └── exceptions.py           # Custom domain-specific exception classes
├── data/
│   └── students.json           # JSON database file
├── README.md                   # Project documentation
└── LEARNING_GUIDE.md           # 14-Stage step-by-step Python learning guide
```

---

## 🚀 Installation & Running the Application

### Prerequisites
- Python 3.8+ installed on your system.

### Running the App
Open a terminal/command prompt in the root directory and run:

```bash
python main.py
```
*(On Windows systems with Python launcher, you can also run `py main.py` or `python3 main.py`)*

---

## 💻 How to Use

When launched, the interactive menu displays:

```text
=======================================================
      STUDENT MANAGEMENT & ACADEMIC TRACKER      
=======================================================

------------------- MAIN MENU -------------------
1. Student Management
2. Subject Management
3. Marks Management
4. Attendance Management
5. Academic Reports
6. Search, Filter & Sort
7. Save Data to File
8. Exit Application
-------------------------------------------------
Enter your choice:
```

Navigate through options 1–8 to access dedicated submenus for student registration, subject evaluation, attendance entry, analytics, and report generation.

---

## 🏛️ Object-Oriented Programming (OOP) Highlights

### 1. Abstraction
- Defined in `models/academic_record.py` using `abc.ABC`.
- `AcademicRecord` mandates `@abstractmethod` implementations for `calculate_result()` and `generate_report()`.

### 2. Encapsulation
- Defined in `models/student.py`.
- Private attributes `self.__marks` and `self.__attendance` cannot be directly modified from outside the class. Safe getter and setter methods enforce validation rules (e.g. 0 ≤ marks ≤ 100).

### 3. Inheritance
- `Person` -> `Student` -> `GraduateStudent` (adds `research_topic`, `advisor_name`).
- `Person` -> `Student` -> `ScholarshipStudent` (adds `scholarship_percentage`, fee discount calculation logic).

### 4. Polymorphism
- The method `display_info()` is declared in `Person` and overridden in `Student`, `GraduateStudent`, and `ScholarshipStudent`.
- Calling `student.generate_report()` dynamically executes the specific report format for that object type.

---

## 🔮 Future Improvements

While this core project deliberately avoids external dependencies for learning purposes, future enhancements could include:
1. **Database Integration**: Replace JSON file storage with SQLite or PostgreSQL using Python's `sqlite3` module or SQLAlchemy ORM.
2. **Graphical User Interface (GUI)**: Build a desktop GUI using Tkinter or PyQt.
3. **REST API Backend**: Expose management functionality over HTTP using FastAPI or Flask.
4. **Web Frontend**: Build a modern web interface with React/Next.js consuming the API.
5. **Authentication**: Implement role-based access control (Admin, Teacher, Student roles).
