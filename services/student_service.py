"""
services/student_service.py

Educational Concepts:
1. Data Structure Management: Lists & Dictionaries of Student objects
2. Functions: Default arguments, *args, **kwargs, Scope (Local & Global)
3. List & Dictionary Comprehensions
4. Higher-Order Functions & Lambdas: sorted(), filter(), map()
5. Exception Handling & Custom Exceptions
"""

from models.student import Student, GraduateStudent, ScholarshipStudent
from utils.exceptions import StudentNotFoundError, DuplicateStudentError
from utils.file_handler import load_students_from_json, save_students_to_json

# CONCEPT: Global in-memory student repository list
_students_repository = []


def load_all_students(file_path: str = None) -> list:
    """
    Loads student data from JSON storage and instantiates OOP objects.
    
    # CONCEPT: Function return values & List comprehension with factory call
    """
    global _students_repository
    raw_records = load_students_from_json(file_path) if file_path else load_students_from_json()
    
    # CONCEPT: List Comprehension converting dictionaries to Student objects
    _students_repository = [Student.create_from_dictionary(data) for data in raw_records]
    return _students_repository


def save_all_students(file_path: str = None) -> bool:
    """
    Serializes in-memory Student objects into dictionary records and persists to JSON.
    
    # CONCEPT: List Comprehension calling instance methods (to_dict)
    """
    global _students_repository
    dict_records = [student.to_dict() for student in _students_repository]
    return save_students_to_json(dict_records, file_path) if file_path else save_students_to_json(dict_records)


def get_all_students() -> list:
    """Returns copy of all student objects."""
    global _students_repository
    return list(_students_repository)


def add_student(student_obj: Student) -> bool:
    """
    Registers a new student into the repository.
    
    # CONCEPT: Membership Operator 'in' with List Comprehension
    # CONCEPT: Raising Custom Exception
    """
    global _students_repository
    existing_ids = [s.student_id for s in _students_repository]
    
    if student_obj.student_id in existing_ids:
        raise DuplicateStudentError(student_obj.student_id)
    
    _students_repository.append(student_obj)
    save_all_students()
    return True


def get_student_by_id(student_id: str) -> Student:
    """
    Searches for a student by unique Student ID.
    
    # CONCEPT: Generator Expression & next() built-in function
    """
    global _students_repository
    target_id = student_id.strip().upper()
    
    # CONCEPT: Searching list with next() generator expression
    found_student = next((s for s in _students_repository if s.student_id == target_id), None)
    if not found_student:
        raise StudentNotFoundError(target_id)
    return found_student


def search_students(query: str, search_by: str = "id") -> list:
    """
    Flexible student search by ID, Name, or Department.
    
    # CONCEPT: String Methods (upper, lower) & List Comprehension
    """
    global _students_repository
    clean_query = query.strip().lower()
    search_by = search_by.lower()

    if search_by == "id":
        return [s for s in _students_repository if clean_query in s.student_id.lower()]
    elif search_by == "name":
        return [s for s in _students_repository if clean_query in s.name.lower()]
    elif search_by == "department" or search_by == "dept":
        return [s for s in _students_repository if clean_query in s.department.lower()]
    else:
        # CONCEPT: General search checking multiple attributes
        return [
            s for s in _students_repository
            if clean_query in s.student_id.lower() or clean_query in s.name.lower() or clean_query in s.department.lower()
        ]


def update_student(student_id: str, **kwargs) -> Student:
    """
    Updates student information using Keyword Arguments (**kwargs).
    
    # CONCEPT: **kwargs Variable-length keyword arguments
    """
    student = get_student_by_id(student_id)
    
    for key, value in kwargs.items():
        if hasattr(student, key) and value is not None:
            if key == "email":
                student.email = value  # Triggers property setter
            elif key == "department":
                student.department = value
            elif key == "age":
                student.age = value
            elif key == "phone":
                student.phone = value
            elif key == "year":
                student.year = int(value)
            elif key == "semester":
                student.semester = int(value)
            elif key == "name":
                student.name = value

    save_all_students()
    return student


def delete_student(student_id: str) -> bool:
    """
    Deletes a student record by ID.
    
    # CONCEPT: List method remove()
    """
    student = get_student_by_id(student_id)
    _students_repository.remove(student)
    save_all_students()
    return True


# CONCEPT: List Comprehensions for Filtering Data
def filter_students_by_department(department: str) -> list:
    """Filters students matching a target department."""
    global _students_repository
    dept_target = department.strip().upper()
    return [s for s in _students_repository if s.department == dept_target]


def filter_passing_students() -> list:
    """
    Filters students who have passed all subjects.
    
    # CONCEPT: Filter built-in function with Lambda
    """
    global _students_repository
    return list(filter(lambda s: s.calculate_result()["status"] == "PASSED", _students_repository))


def filter_failing_students() -> list:
    """Filters students who have failed one or more subjects."""
    global _students_repository
    return list(filter(lambda s: s.calculate_result()["status"] == "FAILED", _students_repository))


def filter_attendance_shortage(min_percentage: float = 75.0) -> list:
    """
    Filters students whose attendance falls below minimum requirement.
    
    # CONCEPT: List comprehension with float comparison
    """
    global _students_repository
    return [s for s in _students_repository if s.attendance_percentage < min_percentage]


# CONCEPT: Sorting with Lambda Functions
def sort_students(criteria: str = "name", reverse: bool = False) -> list:
    """
    Sorts in-memory student records dynamically using lambda key functions.
    
    Criteria options: 'name', 'id', 'percentage', 'gpa', 'attendance'
    """
    global _students_repository
    students_copy = list(_students_repository)
    
    criteria = criteria.lower()
    if criteria == "name":
        # CONCEPT: Lambda function key parameter
        return sorted(students_copy, key=lambda s: s.name, reverse=reverse)
    elif criteria == "id" or criteria == "student_id":
        return sorted(students_copy, key=lambda s: s.student_id, reverse=reverse)
    elif criteria == "percentage":
        return sorted(students_copy, key=lambda s: s.calculate_percentage(), reverse=reverse)
    elif criteria == "gpa":
        return sorted(students_copy, key=lambda s: s.calculate_gpa(), reverse=reverse)
    elif criteria == "attendance":
        return sorted(students_copy, key=lambda s: s.attendance_percentage, reverse=reverse)
    else:
        return sorted(students_copy, key=lambda s: s.name, reverse=reverse)
