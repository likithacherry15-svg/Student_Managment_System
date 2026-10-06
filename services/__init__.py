"""
services package initializer
"""

from services.student_service import (
    load_all_students,
    save_all_students,
    get_all_students,
    add_student,
    get_student_by_id,
    search_students,
    update_student,
    delete_student,
    filter_students_by_department,
    filter_passing_students,
    filter_failing_students,
    filter_attendance_shortage,
    sort_students
)

from services.marks_service import (
    assign_subject_to_student,
    enter_student_marks,
    batch_enter_marks,
    view_student_marks,
    calculate_student_totals
)

from services.attendance_service import (
    record_student_attendance,
    view_student_attendance,
    get_all_attendance_shortage
)

from services.report_service import (
    generate_student_report,
    generate_performance_report
)

__all__ = [
    "load_all_students",
    "save_all_students",
    "get_all_students",
    "add_student",
    "get_student_by_id",
    "search_students",
    "update_student",
    "delete_student",
    "filter_students_by_department",
    "filter_passing_students",
    "filter_failing_students",
    "filter_attendance_shortage",
    "sort_students",
    "assign_subject_to_student",
    "enter_student_marks",
    "batch_enter_marks",
    "view_student_marks",
    "calculate_student_totals",
    "record_student_attendance",
    "view_student_attendance",
    "get_all_attendance_shortage",
    "generate_student_report",
    "generate_performance_report"
]
