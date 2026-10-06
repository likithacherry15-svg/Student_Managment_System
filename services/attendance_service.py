"""
services/attendance_service.py

Educational Concepts:
1. Object Encapsulation & Service Layer Isolation
2. List Comprehensions & Conditional Evaluation
3. Default parameter values
"""

from services.student_service import get_student_by_id, get_all_students, save_all_students


def record_student_attendance(student_id: str, attended: int, conducted: int) -> str:
    """
    Updates attendance counts for a specific student.
    Formula: Attendance % = (Attended / Conducted) * 100
    Default Requirement: 75%
    """
    student = get_student_by_id(student_id)
    student.update_attendance(attended, conducted)
    save_all_students()
    
    # Return formatted summary statement
    attendance_obj = student.get_attendance_record()
    return attendance_obj.get_status_summary()


def view_student_attendance(student_id: str) -> dict:
    """Retrieves attendance summary object for a student."""
    student = get_student_by_id(student_id)
    att_record = student.get_attendance_record()
    
    return {
        "student_id": student.student_id,
        "name": student.name,
        "attended": att_record.attended,
        "conducted": att_record.conducted,
        "percentage": att_record.percentage,
        "is_eligible": att_record.is_eligible,
        "status_summary": att_record.get_status_summary(),
        "last_updated": att_record.last_updated
    }


def get_all_attendance_shortage(min_percentage: float = 75.0) -> list:
    """
    Filters all students whose attendance percentage is less than required minimum.
    
    # CONCEPT: List Comprehension with object method calls
    """
    all_students = get_all_students()
    shortage_list = [
        {
            "student_id": s.student_id,
            "name": s.name,
            "department": s.department,
            "percentage": s.attendance_percentage,
            "shortage": round(min_percentage - s.attendance_percentage, 2)
        }
        for s in all_students
        if s.attendance_percentage < min_percentage
    ]
    return shortage_list
