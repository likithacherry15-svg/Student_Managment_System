"""
services/report_service.py

Educational Concepts:
1. Polymorphism: Calling generate_report() on Student, GraduateStudent, or ScholarshipStudent
2. Dictionary Comprehensions & Set Operations
3. Higher-Order Functions & Aggregations (max, min, sum, reduce)
4. String formatting & multi-line reports
"""

from datetime import datetime
from functools import reduce
from services.student_service import get_student_by_id, get_all_students


def generate_student_report(student_id: str) -> str:
    """
    Generates a single student's academic report string.
    
    # CONCEPT: Polymorphism - Student subclass overrides generate_report()
    """
    student = get_student_by_id(student_id)
    return student.generate_report()


def generate_performance_report() -> str:
    """
    Generates an overall system performance & analytical report.
    Calculates:
      - Total student count
      - Highest percentage & Top performer student
      - Lowest percentage student
      - Class average percentage
      - Failed students count & list
      - Attendance shortage count & list
      - Department-wise breakdown
      
    # CONCEPT: Aggregations, List/Dict comprehensions, and max/min with lambda keys
    """
    students = get_all_students()
    
    if not students:
        return "==================================================\n" \
               "         ACADEMIC PERFORMANCE REPORT             \n" \
               "==================================================\n" \
               " No student records available in the system.\n" \
               "=================================================="

    total_count = len(students)
    
    # CONCEPT: Extract percentages list
    percentages = [s.calculate_percentage() for s in students]
    
    # CONCEPT: max() and min() with lambda key functions
    top_student = max(students, key=lambda s: s.calculate_percentage())
    lowest_student = min(students, key=lambda s: s.calculate_percentage())
    
    highest_pct = top_student.calculate_percentage()
    lowest_pct = lowest_student.calculate_percentage()
    
    # CONCEPT: reduce() to compute class average percentage
    sum_pct = reduce(lambda acc, p: acc + p, percentages, 0.0)
    avg_pct = round(sum_pct / total_count, 2)
    
    # CONCEPT: Filter passed and failed students
    failed_students = [s for s in students if s.calculate_result()["status"] == "FAILED"]
    passed_students = [s for s in students if s.calculate_result()["status"] == "PASSED"]
    
    # CONCEPT: Attendance shortage filter
    shortage_students = [s for s in students if s.attendance_percentage < 75.0]

    # CONCEPT: Set operation to get unique departments
    departments = sorted(list({s.department for s in students}))
    
    # CONCEPT: Dictionary Comprehension for department-wise student count
    dept_counts = {dept: len([s for s in students if s.department == dept]) for dept in departments}

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_lines = [
        "=" * 60,
        "              ACADEMIC PERFORMANCE REPORT               ",
        f" Generated On: {now_str}",
        "=" * 60,
        f" Total Registered Students : {total_count}",
        f" Overall Class Average     : {avg_pct}%",
        f" Passed Students Count     : {len(passed_students)} ({round(len(passed_students)/total_count*100, 1)}%)",
        f" Failed Students Count     : {len(failed_students)}",
        f" Attendance Shortage Count : {len(shortage_students)}",
        "-" * 60,
        " TOP PERFORMER:",
        f"   ID: {top_student.student_id} | Name: {top_student.name} | Dept: {top_student.department}",
        f"   Percentage: {highest_pct}% | GPA: {top_student.gpa} | Grade: {top_student.grade}",
        "-" * 60,
        " LOWEST PERFORMER:",
        f"   ID: {lowest_student.student_id} | Name: {lowest_student.name} | Dept: {lowest_student.department}",
        f"   Percentage: {lowest_pct}% | GPA: {lowest_student.gpa} | Grade: {lowest_student.grade}",
        "-" * 60,
        " DEPARTMENT BREAKDOWN:"
    ]

    for dept, count in dept_counts.items():
        report_lines.append(f"   - {dept:<10} : {count} Student(s)")

    if failed_students:
        report_lines.append("-" * 60)
        report_lines.append(" FAILED STUDENTS LIST:")
        for s in failed_students:
            report_lines.append(f"   * [{s.student_id}] {s.name:<20} ({s.department}) - Pct: {s.calculate_percentage()}%")

    if shortage_students:
        report_lines.append("-" * 60)
        report_lines.append(" ATTENDANCE SHORTAGE LIST (< 75%):")
        for s in shortage_students:
            report_lines.append(f"   * [{s.student_id}] {s.name:<20} ({s.department}) - Attendance: {s.attendance_percentage}%")

    report_lines.append("=" * 60)

    return "\n".join(report_lines)
