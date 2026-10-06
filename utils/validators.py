"""
utils/validators.py

Educational Concepts:
1. String Handling: strip(), upper(), lower(), title(), isalpha(), startswith()
2. Type Conversion & Exception Handling
3. Set Operations for department verification
4. Standard Library imports (re module for Regular Expressions)
"""

import re
from utils.exceptions import (
    InvalidStudentDataError,
    InvalidMarksError,
    InvalidAttendanceError
)

# CONCEPT: Constants (Immutable reference set & tuple)
VALID_DEPARTMENTS = {"CSE", "CSE-AI", "ECE", "EEE", "MECH", "CIVIL"}
VALID_SEMESTERS = (1, 2, 3, 4, 5, 6, 7, 8)
MIN_MARKS = 0.0
MAX_MARKS = 100.0


def validate_student_id(student_id: str) -> str:
    """
    Validates and standardizes student ID format (e.g., STU001, STU102).
    
    # CONCEPT: String Methods & Strip
    """
    if not isinstance(student_id, str):
        raise InvalidStudentDataError("Student ID must be a string.")
    
    cleaned_id = student_id.strip().upper()
    
    # CONCEPT: Regular Expressions for format verification
    if not re.match(r"^STU\d{3,}$", cleaned_id):
        raise InvalidStudentDataError(
            f"Invalid Student ID format: '{student_id}'. ID must start with 'STU' followed by at least 3 digits (e.g., STU001)."
        )
    return cleaned_id


def validate_name(name: str) -> str:
    """
    Validates and formats full name.
    
    # CONCEPT: String method title() and replace()
    """
    if not name or not isinstance(name, str):
        raise InvalidStudentDataError("Name cannot be empty.")
    
    cleaned_name = name.strip()
    # Replace spaces temporarily to check if all other characters are alphabetic
    if not cleaned_name.replace(" ", "").isalpha():
        raise InvalidStudentDataError(f"Name '{name}' can only contain alphabetic characters and spaces.")
    
    return cleaned_name.title()


def validate_email(email: str) -> str:
    """
    Validates email format using regular expressions.
    
    # CONCEPT: String method lower()
    """
    if not email or not isinstance(email, str):
        raise InvalidStudentDataError("Email address cannot be empty.")
    
    cleaned_email = email.strip().lower()
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, cleaned_email):
        raise InvalidStudentDataError(f"Invalid email address format: '{email}'.")
    
    return cleaned_email


def validate_phone(phone: str) -> str:
    """
    Validates 10-digit mobile phone number.
    """
    if not phone or not isinstance(phone, str):
        raise InvalidStudentDataError("Phone number must be a string.")
    
    cleaned_phone = phone.strip()
    if not (cleaned_phone.isdigit() and len(cleaned_phone) == 10):
        raise InvalidStudentDataError(f"Invalid phone number: '{phone}'. Must contain exactly 10 digits.")
    
    return cleaned_phone


def validate_age(age_input) -> int:
    """
    Validates student age (15 to 100).
    
    # CONCEPT: Type Conversion (str to int) & Exception Handling
    """
    try:
        age = int(age_input)
    except (ValueError, TypeError):
        raise InvalidStudentDataError(f"Age must be a valid integer number. Received: '{age_input}'.")
    
    if not (15 <= age <= 100):
        raise InvalidStudentDataError(f"Age must be between 15 and 100. Received: {age}.")
    
    return age


def validate_department(department: str) -> str:
    """
    Validates department against predefined set of allowed departments.
    
    # CONCEPT: Membership operator 'in' and Set usage
    """
    if not department or not isinstance(department, str):
        raise InvalidStudentDataError("Department cannot be empty.")
    
    cleaned_dept = department.strip().upper()
    if cleaned_dept not in VALID_DEPARTMENTS:
        allowed = ", ".join(sorted(list(VALID_DEPARTMENTS)))
        raise InvalidStudentDataError(
            f"Invalid department '{department}'. Must be one of: {allowed}."
        )
    
    return cleaned_dept


def validate_semester(semester_input) -> int:
    """
    Validates semester number (1 to 8).
    
    # CONCEPT: Tuple membership check
    """
    try:
        semester = int(semester_input)
    except (ValueError, TypeError):
        raise InvalidStudentDataError(f"Semester must be an integer between 1 and 8. Received: '{semester_input}'.")
    
    if semester not in VALID_SEMESTERS:
        raise InvalidStudentDataError(f"Semester must be between 1 and 8. Received: {semester}.")
    
    return semester


def validate_marks(marks_input) -> float:
    """
    Validates academic subject mark (0.0 to 100.0).
    
    # CONCEPT: Type Conversion (float)
    """
    try:
        mark = float(marks_input)
    except (ValueError, TypeError):
        raise InvalidMarksError(marks_input, "Marks must be a numeric integer or float.")
    
    if not (MIN_MARKS <= mark <= MAX_MARKS):
        raise InvalidMarksError(mark, f"Marks must be between {MIN_MARKS} and {MAX_MARKS}.")
    
    return round(mark, 2)


def validate_attendance(classes_attended, classes_conducted) -> tuple:
    """
    Validates attendance count values.
    
    # CONCEPT: Tuple Return Value
    """
    try:
        attended = int(classes_attended)
        conducted = int(classes_conducted)
    except (ValueError, TypeError):
        raise InvalidAttendanceError("Attendance values must be integer numbers.")
    
    if attended < 0 or conducted < 0:
        raise InvalidAttendanceError("Attendance numbers cannot be negative.")
    
    if attended > conducted:
        raise InvalidAttendanceError(
            f"Classes attended ({attended}) cannot exceed total classes conducted ({conducted})."
        )
    
    return attended, conducted
