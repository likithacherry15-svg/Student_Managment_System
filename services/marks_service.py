"""
services/marks_service.py

Educational Concepts:
1. Higher-Order Functions: zip(), map(), filter(), functools.reduce()
2. Dictionary Operations
3. Variable-length positional parameters (*args)
"""

from functools import reduce
from services.student_service import get_student_by_id, save_all_students
from utils.validators import validate_marks


def assign_subject_to_student(student_id: str, subject_name: str) -> list:
    """Adds a new subject to a student's list of enrolled subjects."""
    student = get_student_by_id(student_id)
    student.add_subject(subject_name)
    save_all_students()
    return student.subjects


def enter_student_marks(student_id: str, subject_name: str, score: float) -> dict:
    """Enters or updates marks for a specific subject for a student."""
    student = get_student_by_id(student_id)
    student.add_marks(subject_name, score)
    save_all_students()
    return student.get_marks()


def batch_enter_marks(student_id: str, *subject_mark_pairs):
    """
    Enters multiple subject-mark pairs using Variable-Length Positional Arguments (*args).
    
    # CONCEPT: *args iteration & Tuple Unpacking
    """
    student = get_student_by_id(student_id)
    for subject, score in subject_mark_pairs:
        student.add_marks(subject, score)
    save_all_students()
    return student.get_marks()


def view_student_marks(student_id: str) -> dict:
    """
    Retrieves student marks and pairs subjects with marks using zip().
    
    # CONCEPT: zip() built-in function combining two parallel sequences
    """
    student = get_student_by_id(student_id)
    marks_dict = student.get_marks()
    
    # CONCEPT: Demonstrating zip() with subject list and corresponding score list
    subjects = list(marks_dict.keys())
    scores = list(marks_dict.values())
    
    # Pairing with zip
    paired_list = list(zip(subjects, scores))
    return {
        "student_id": student.student_id,
        "student_name": student.name,
        "paired_marks": paired_list,
        "marks_dict": marks_dict
    }


def calculate_student_totals(student_id: str) -> dict:
    """
    Calculates total score, average, percentage, grade, and GPA using map and reduce.
    
    # CONCEPT: map() and functools.reduce() demonstration
    """
    student = get_student_by_id(student_id)
    marks_dict = student.get_marks()
    
    if not marks_dict:
        return {
            "total_marks": 0.0,
            "average": 0.0,
            "percentage": 0.0,
            "grade": "N/A",
            "gpa": 0.0
        }

    scores = list(marks_dict.values())
    
    # CONCEPT: map() to format scores to rounded floats
    formatted_scores = list(map(lambda x: round(float(x), 2), scores))
    
    # CONCEPT: reduce() to compute aggregate total marks
    total_marks = reduce(lambda a, b: a + b, formatted_scores, 0.0)
    
    average_score = round(total_marks / len(formatted_scores), 2)
    percentage = student.calculate_percentage()
    grade = student.grade
    gpa = student.calculate_gpa()

    return {
        "subject_count": len(scores),
        "total_marks": total_marks,
        "average": average_score,
        "percentage": percentage,
        "grade": grade,
        "gpa": gpa
    }
