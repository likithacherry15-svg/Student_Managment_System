# Educational Learning Guide: Student Management System

This step-by-step guide breaks down the codebase into **14 Progressive Learning Stages**, allowing beginners and intermediate programmers to trace how basic Python syntax evolves into a full Object-Oriented Programming (OOP) application.

---

## 🎯 Stage 1 — Python Basics

### 📖 Concept
Variables, constants, data types (`int`, `float`, `str`, `bool`), type casting, arithmetic operators, string formatting, and f-strings.

### 📁 File Location
[`utils/validators.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/utils/validators.py)

### 💻 Code Example
```python
MIN_MARKS = 0.0
MAX_MARKS = 100.0

def validate_age(age_input) -> int:
    age = int(age_input)  # Type casting str to int
    if not (15 <= age <= 100):
        raise ValueError(f"Age must be between 15 and 100. Received: {age}")
    return age
```

### ✏️ Exercise for Learner
Create a variable `tuition_fee = 50000` and `discount_rate = 0.15`. Calculate the net fee using arithmetic operators and print it using an f-string formatted to two decimal places.

---

## 🎯 Stage 2 — Conditional Statements

### 📖 Concept
Using `if`, `elif`, `else`, nested conditions, and ternary conditional expressions (`A if condition else B`).

### 📁 File Location
[`models/attendance.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/models/attendance.py) and [`models/student.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/models/student.py)

### 💻 Code Example
```python
# Grade Calculation
if score >= 90:
    return "A+", 10.0
elif score >= 80:
    return "A", 9.0
elif score >= 70:
    return "B", 8.0
elif score >= 60:
    return "C", 7.0
elif score >= 50:
    return "D", 6.0
else:
    return "F", 0.0

# Ternary Expression
status = "ELIGIBLE" if self.is_eligible else "NOT ELIGIBLE (SHORTAGE)"
```

### ✏️ Exercise for Learner
Write a conditional statement that takes a student's percentage and attendance percentage, and prints `"Honors Eligible"` if percentage >= 85 and attendance >= 80, else prints `"Standard Passed"`.

---

## 🎯 Stage 3 — Loops & Control Flow

### 📖 Concept
`while` loops for persistent menus, `for` loops for iteration, `enumerate()` for numbered output, `break`, and `continue`.

### 📁 File Location
[`main.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/main.py)

### 💻 Code Example
```python
while True:
    print_main_menu()
    user_choice = input("Enter choice (1-8): ").strip()
    if user_choice == "8":
        print("Exiting application...")
        break  # Exit loop
```

### ✏️ Exercise for Learner
Write a `for` loop using `enumerate()` to iterate over a list of 5 subject names `["Python", "DBMS", "Networks", "AI", "Math"]` and print each with a 1-based index (e.g. `1. Python`).

---

## 🎯 Stage 4 — Python Data Structures

### 📖 Concept
Lists, Tuples (fixed/immutable information), Sets (unique elements & set math), and Dictionaries (key-value records).

### 📁 File Location
[`models/course.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/models/course.py) and [`services/student_service.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/services/student_service.py)

### 💻 Code Example
```python
# Tuple Constant
COURSE_TYPES = ("Theory", "Practical/Lab", "Project")

# Set for Unique Departments
VALID_DEPARTMENTS = {"CSE", "CSE-AI", "ECE", "EEE"}

# Dictionary representing Student
student_dict = {
    "student_id": "STU001",
    "name": "Rahul",
    "marks": {"Python": 88.5, "DBMS": 82.0}
}
```

### ✏️ Exercise for Learner
Create two sets of department codes: `offered_depts = {"CSE", "ECE", "MECH"}` and `enrolled_depts = {"CSE", "CIVIL"}`. Perform set `union`, `intersection`, and `difference` operations on them.

---

## 🎯 Stage 5 — Reusable Functions & Arguments

### 📖 Concept
Parameters, return values, default arguments, positional `*args`, variable keyword `**kwargs`, and variable scope.

### 📁 File Location
[`services/marks_service.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/services/marks_service.py)

### 💻 Code Example
```python
# Default argument and *args demonstration
def batch_enter_marks(student_id: str, *subject_mark_pairs):
    student = get_student_by_id(student_id)
    for subject, score in subject_mark_pairs:
        student.add_marks(subject, score)
    return student.get_marks()
```

### ✏️ Exercise for Learner
Write a function `calculate_weighted_score(*marks, weight=1.0)` that accepts variable numeric marks, multiplies the average by `weight`, and returns the result.

---

## 🎯 Stage 6 — File Handling & Data Persistence

### 📖 Concept
Reading and writing JSON files safely using `with open(...)` context managers, `json.load()`, and `json.dump()`.

### 📁 File Location
[`utils/file_handler.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/utils/file_handler.py)

### 💻 Code Example
```python
def save_students_to_json(student_dicts: list, file_path: str) -> bool:
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(student_dicts, file, indent=4)
    return True
```

### ✏️ Exercise for Learner
Write a small script that opens a file named `sample_test.json`, writes a python dictionary `{ "app": "SMS", "version": 1.0 }`, and then reads it back to display the version.

---

## 🎯 Stage 7 — Exception Handling

### 📖 Concept
`try`, `except`, `else`, `finally`, `raise`, and creating a custom exception hierarchy.

### 📁 File Location
[`utils/exceptions.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/utils/exceptions.py)

### 💻 Code Example
```python
class StudentNotFoundError(Exception):
    def __init__(self, student_id: str):
        self.student_id = student_id
        super().__init__(f"Student with ID '{student_id}' not found.")

# Triggering exception
if not student:
    raise StudentNotFoundError(student_id)
```

### ✏️ Exercise for Learner
Create a custom exception `InvalidMarksError`. Write a function `set_score(score)` that raises `InvalidMarksError` if score < 0 or score > 100, and catch it in a `try-except` block.

---

## 🎯 Stage 8 — Modules & Package Structure

### 📖 Concept
Organizing code into packages (`models`, `services`, `utils`), using `__init__.py`, and importing symbols across modules.

### 📁 File Location
[`models/__init__.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/models/__init__.py) and [`services/__init__.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/services/__init__.py)

### 💻 Code Example
```python
from models.person import Person
from models.student import Student, GraduateStudent
from utils.validators import validate_student_id
```

### ✏️ Exercise for Learner
Create a folder `helpers/` with `__init__.py` and `calculator.py`. Import a function from `helpers.calculator` inside `main.py`.

---

## 🎯 Stage 9 — Classes & Objects

### 📖 Concept
Creating classes, initializing objects with `__init__()`, instantiating attributes, and defining instance methods.

### 📁 File Location
[`models/person.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/models/person.py)

### 💻 Code Example
```python
class Person:
    def __init__(self, name: str, age: int, email: str, phone: str):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def display_info(self) -> str:
        return f"Name: {self.name} | Age: {self.age}"
```

### ✏️ Exercise for Learner
Instantiate a `Person` object `p1 = Person("Alice", 22, "alice@example.com", "1234567890")` and call `p1.display_info()`.

---

## 🎯 Stage 10 — Encapsulation

### 📖 Concept
Protecting object state with private attributes (`self.__marks`), getters, setters, and Python `@property` decorators.

### 📁 File Location
[`models/student.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/models/student.py)

### 💻 Code Example
```python
class Student(Person):
    def __init__(self, ...):
        self.__marks = {}  # Private attribute

    def get_marks(self) -> dict:
        return dict(self.__marks)  # Safe getter

    def set_marks(self, marks_dict: dict):
        # Enforce validation before assignment
        for k, v in marks_dict.items():
            validate_marks(v)
        self.__marks = marks_dict
```

### ✏️ Exercise for Learner
Add a private attribute `self.__fee_balance` to a class with a `@property` getter and a setter that rejects negative payments.

---

## 🎯 Stage 11 — Inheritance

### 📖 Concept
Building class hierarchies (`Person` -> `Student` -> `GraduateStudent` & `ScholarshipStudent`) and using `super().__init__()`.

### 📁 File Location
[`models/student.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/models/student.py)

### 💻 Code Example
```python
class GraduateStudent(Student):
    def __init__(self, student_id, name, research_topic, advisor_name, **kwargs):
        super().__init__(student_id=student_id, name=name, **kwargs)
        self.research_topic = research_topic
        self.advisor_name = advisor_name
```

### ✏️ Exercise for Learner
Create a `TeachingAssistant` class that inherits from `GraduateStudent` and adds a `course_assigned` attribute.

---

## 🎯 Stage 12 — Polymorphism

### 📖 Concept
Method overriding where derived classes provide specialized implementations for common interface methods.

### 📁 File Location
[`models/student.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/models/student.py)

### 💻 Code Example
```python
# Person implementation
def display_info(self) -> str:
    return f"Name: {self.name}"

# ScholarshipStudent overriding implementation
def display_info(self) -> str:
    base = super().display_info()
    return f"{base} | Scholarship: {self.scholarship_name} ({self.scholarship_percentage}%)"
```

### ✏️ Exercise for Learner
Create a list containing instances of `Student`, `GraduateStudent`, and `ScholarshipStudent`. Iterate over the list and call `.display_info()` on each object to observe polymorphic behavior.

---

## 🎯 Stage 13 — Abstraction

### 📖 Concept
Using Python's `abc` module to define abstract base classes (`ABC`) and enforce abstract methods (`@abstractmethod`).

### 📁 File Location
[`models/academic_record.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/models/academic_record.py)

### 💻 Code Example
```python
from abc import ABC, abstractmethod

class AcademicRecord(ABC):
    @abstractmethod
    def calculate_result(self) -> dict:
        pass

    @abstractmethod
    def generate_report(self) -> str:
        pass
```

### ✏️ Exercise for Learner
Try instantiating `AcademicRecord()` directly in Python and observe the `TypeError` raised due to unimplemented abstract methods.

---

## 🎯 Stage 14 — Complete Integrated Project

### 📖 Concept
Combining all components into a modular, production-grade console application with interactive menus, service layers, and file persistence.

### 📁 File Location
[`main.py`](file:///d:/Projects/Cherry/Student%20Managment%20System/main.py)

### 💻 Launching Application
```bash
python main.py
```
