"""
models package initializer
"""

from models.person import Person
from models.academic_record import AcademicRecord
from models.course import Course
from models.attendance import AttendanceRecord
from models.student import Student, GraduateStudent, ScholarshipStudent

__all__ = [
    "Person",
    "AcademicRecord",
    "Course",
    "AttendanceRecord",
    "Student",
    "GraduateStudent",
    "ScholarshipStudent"
]
