"""
utils/exceptions.py

Educational Concept: Custom Exception Hierarchy
- Custom exceptions inherit from Python's built-in `Exception` class.
- They allow domain-specific error handling across the application.
- `raise` keyword is used to trigger these exceptions when validation fails.
"""

class StudentManagementError(Exception):
    """Base exception class for all Student Management System errors."""
    pass

class StudentNotFoundError(StudentManagementError):
    """Raised when a requested student ID is not found in the database."""
    def __init__(self, student_id: str):
        self.student_id = student_id
        super().__init__(f"StudentNotFoundError: Student with ID '{student_id}' was not found.")

class DuplicateStudentError(StudentManagementError):
    """Raised when attempting to register a student with an existing ID."""
    def __init__(self, student_id: str):
        self.student_id = student_id
        super().__init__(f"DuplicateStudentError: A student with ID '{student_id}' already exists.")

class InvalidMarksError(StudentManagementError):
    """Raised when entered marks fall outside the valid 0-100 range."""
    def __init__(self, mark_value, message="Marks must be a numeric value between 0.0 and 100.0."):
        self.mark_value = mark_value
        super().__init__(f"InvalidMarksError: {message} Received: '{mark_value}'.")

class InvalidAttendanceError(StudentManagementError):
    """Raised when attendance inputs are logically invalid (e.g. attended > conducted)."""
    def __init__(self, message="Attended classes cannot exceed total conducted classes or be negative."):
        super().__init__(f"InvalidAttendanceError: {message}")

class InvalidStudentDataError(StudentManagementError):
    """Raised when student personal or academic attributes fail validation."""
    def __init__(self, message="Provided student data is invalid."):
        super().__init__(f"InvalidStudentDataError: {message}")
