"""
main.py

Main Console Application Entry Point for Student Management & Academic Tracker.

Educational Concepts Demonstrated:
1. Control Flow Loops: while loops for persistent menus, break/continue
2. Functions & Modular Architecture
3. Exception Handling (try-except-else-finally) preventing application crashes
4. Object-Oriented Programming (Polymorphism, Encapsulation, Inheritance)
5. User Input Validation & Formatting
"""

import sys
import os

# Ensure package paths resolution when executed directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.student import Student, GraduateStudent, ScholarshipStudent
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
from utils.exceptions import (
    StudentManagementError,
    StudentNotFoundError,
    DuplicateStudentError,
    InvalidMarksError,
    InvalidAttendanceError,
    InvalidStudentDataError
)
from utils.validators import (
    validate_student_id,
    validate_name,
    validate_email,
    validate_phone,
    validate_age,
    validate_department,
    validate_semester,
    validate_marks,
    validate_attendance
)


def print_banner():
    """Prints application header banner."""
    print("\n" + "=" * 55)
    print("      STUDENT MANAGEMENT & ACADEMIC TRACKER      ")
    print("=" * 55)


def print_main_menu():
    """Displays the main menu options."""
    print("\n------------------- MAIN MENU -------------------")
    print("1. Student Management")
    print("2. Subject Management")
    print("3. Marks Management")
    print("4. Attendance Management")
    print("5. Academic Reports")
    print("6. Search, Filter & Sort")
    print("7. Save Data to File")
    print("8. Exit Application")
    print("-------------------------------------------------")


# =====================================================================
# 1. STUDENT MANAGEMENT SUBMENU
# =====================================================================
def menu_student_management():
    """Submenu loop for student registration, viewing, updating, deleting."""
    while True:
        print("\n--- [1] STUDENT MANAGEMENT ---")
        print("1. Add New Student (Regular / Graduate / Scholarship)")
        print("2. View All Students")
        print("3. Search Student Details")
        print("4. Update Student Information")
        print("5. Delete Student Record")
        print("6. Return to Main Menu")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == "1":
            print("\n-- Add New Student --")
            st_type = input("Student Type (1: Regular, 2: Graduate, 3: Scholarship) [Default 1]: ").strip()
            student_id = input("Enter Student ID (e.g. STU006): ").strip()
            name = input("Enter Full Name: ").strip()
            age = input("Enter Age: ").strip()
            email = input("Enter Email Address: ").strip()
            phone = input("Enter 10-digit Phone: ").strip()
            dept = input("Enter Department (CSE, CSE-AI, ECE, EEE): ").strip()
            year = input("Enter Academic Year (1-4) [Default 1]: ").strip() or "1"
            sem = input("Enter Semester (1-8) [Default 1]: ").strip() or "1"

            try:
                if st_type == "2":
                    topic = input("Enter Research Topic: ").strip()
                    advisor = input("Enter Advisor Name: ").strip()
                    student = GraduateStudent(
                        student_id=student_id, name=name, age=age, email=email,
                        phone=phone, department=dept, research_topic=topic, advisor_name=advisor,
                        year=year, semester=sem
                    )
                elif st_type == "3":
                    sch_name = input("Enter Scholarship Name: ").strip()
                    sch_pct = input("Enter Scholarship Discount % [Default 25]: ").strip() or "25"
                    student = ScholarshipStudent(
                        student_id=student_id, name=name, age=age, email=email,
                        phone=phone, department=dept, scholarship_name=sch_name, scholarship_percentage=sch_pct,
                        year=year, semester=sem
                    )
                else:
                    student = Student(
                        student_id=student_id, name=name, age=age, email=email,
                        phone=phone, department=dept, year=year, semester=sem
                    )

                add_student(student)
                print(f"[SUCCESS] Student '{name}' registered successfully with ID: {student.student_id}")
            except StudentManagementError as err:
                print(f"[ERROR] Registration Failed: {err}")
            except Exception as exc:
                print(f"[ERROR] Unexpected Error: {exc}")

        elif choice == "2":
            print("\n-- View All Students --")
            students = get_all_students()
            if not students:
                print("No students currently registered.")
            else:
                # CONCEPT: Enumerate for list formatting
                for idx, st in enumerate(students, start=1):
                    # CONCEPT: Polymorphism - display_info()
                    print(f"{idx:<2}. {st.display_info()}")

        elif choice == "3":
            query = input("\nEnter Student ID or Name to search: ").strip()
            try:
                results = search_students(query, search_by="general")
                if not results:
                    print("No matching student records found.")
                else:
                    print(f"Found {len(results)} matching record(s):")
                    for st in results:
                        print(f" - {st.display_info()}")
            except Exception as exc:
                print(f"[ERROR] Search failed: {exc}")

        elif choice == "4":
            st_id = input("\nEnter Student ID to update: ").strip()
            try:
                st = get_student_by_id(st_id)
                print(f"Updating details for: {st.name} [{st.student_id}]")
                print("Leave blank to keep existing value.")
                
                new_name = input(f"New Name [{st.name}]: ").strip() or None
                new_email = input(f"New Email [{st.email}]: ").strip() or None
                new_phone = input(f"New Phone [{st.phone}]: ").strip() or None
                new_dept = input(f"New Department [{st.department}]: ").strip() or None

                updated = update_student(
                    st_id,
                    name=new_name,
                    email=new_email,
                    phone=new_phone,
                    department=new_dept
                )
                print(f"[SUCCESS] Student details updated: {updated.display_info()}")
            except StudentManagementError as err:
                print(f"[ERROR] Update Failed: {err}")

        elif choice == "5":
            st_id = input("\nEnter Student ID to delete: ").strip()
            try:
                confirm = input(f"Are you sure you want to delete {st_id}? (y/n): ").strip().lower()
                if confirm == 'y':
                    delete_student(st_id)
                    print(f"[SUCCESS] Student '{st_id}' deleted successfully.")
            except StudentManagementError as err:
                print(f"[ERROR] Deletion Failed: {err}")

        elif choice == "6":
            break
        else:
            print("[INVALID] Invalid menu selection. Please enter 1-6.")


# =====================================================================
# 2. SUBJECT MANAGEMENT SUBMENU
# =====================================================================
def menu_subject_management():
    """Submenu for assigning and viewing subjects."""
    while True:
        print("\n--- [2] SUBJECT MANAGEMENT ---")
        print("1. Assign Subject to Student")
        print("2. View Student Subjects")
        print("3. Remove Subject from Student")
        print("4. Return to Main Menu")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            st_id = input("Enter Student ID: ").strip()
            subj_name = input("Enter Subject Name to Assign (e.g. Python, DBMS): ").strip()
            try:
                subjects = assign_subject_to_student(st_id, subj_name)
                print(f"[SUCCESS] Subject '{subj_name}' assigned to {st_id}. Total subjects: {subjects}")
            except StudentManagementError as err:
                print(f"[ERROR] {err}")

        elif choice == "2":
            st_id = input("Enter Student ID: ").strip()
            try:
                st = get_student_by_id(st_id)
                print(f"\nSubjects for {st.name} [{st.student_id}]:")
                if not st.subjects:
                    print(" No subjects currently assigned.")
                else:
                    for idx, subj in enumerate(st.subjects, start=1):
                        print(f" {idx}. {subj}")
            except StudentManagementError as err:
                print(f"[ERROR] {err}")

        elif choice == "3":
            st_id = input("Enter Student ID: ").strip()
            subj_name = input("Enter Subject Name to Remove: ").strip()
            try:
                st = get_student_by_id(st_id)
                st.remove_subject(subj_name)
                save_all_students()
                print(f"[SUCCESS] Subject '{subj_name}' removed from {st_id}.")
            except StudentManagementError as err:
                print(f"[ERROR] {err}")

        elif choice == "4":
            break
        else:
            print("[INVALID] Choice must be between 1 and 4.")


# =====================================================================
# 3. MARKS MANAGEMENT SUBMENU
# =====================================================================
def menu_marks_management():
    """Submenu for entering, updating, viewing marks and calculations."""
    while True:
        print("\n--- [3] MARKS MANAGEMENT ---")
        print("1. Enter / Update Subject Marks")
        print("2. View Student Marks (Zip demonstration)")
        print("3. Calculate Totals, Percentage, Grade & GPA")
        print("4. Return to Main Menu")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            st_id = input("Enter Student ID: ").strip()
            subj_name = input("Enter Subject Name: ").strip()
            mark_val = input("Enter Marks (0.0 - 100.0): ").strip()
            try:
                marks_dict = enter_student_marks(st_id, subj_name, mark_val)
                print(f"[SUCCESS] Marks updated for {subj_name}: {marks_dict[subj_name]}")
            except StudentManagementError as err:
                print(f"[ERROR] {err}")

        elif choice == "2":
            st_id = input("Enter Student ID: ").strip()
            try:
                result = view_student_marks(st_id)
                print(f"\nMarks summary for {result['student_name']} [{result['student_id']}]:")
                paired = result['paired_marks']
                if not paired:
                    print(" No marks recorded yet.")
                else:
                    # CONCEPT: Iterating zipped list pairs
                    for subject, score in paired:
                        let_grade, gp = Student.score_to_grade(score)
                        print(f" - {subject:<20} : {score:>6.2f} | Grade: {let_grade} (GP: {gp})")
            except StudentManagementError as err:
                print(f"[ERROR] {err}")

        elif choice == "3":
            st_id = input("Enter Student ID: ").strip()
            try:
                calc = calculate_student_totals(st_id)
                print(f"\n--- ACADEMIC SUMMARY FOR {st_id} ---")
                print(f" Total Subjects Evaluated : {calc['subject_count']}")
                print(f" Cumulative Marks Total  : {calc['total_marks']}")
                print(f" Subject Average          : {calc['average']}")
                print(f" Percentage               : {calc['percentage']}%")
                print(f" Grade                    : {calc['grade']}")
                print(f" GPA                      : {calc['gpa']} / 10.0")
            except StudentManagementError as err:
                print(f"[ERROR] {err}")

        elif choice == "4":
            break
        else:
            print("[INVALID] Enter a number from 1 to 4.")


# =====================================================================
# 4. ATTENDANCE MANAGEMENT SUBMENU
# =====================================================================
def menu_attendance_management():
    """Submenu for recording and auditing student attendance."""
    while True:
        print("\n--- [4] ATTENDANCE MANAGEMENT ---")
        print("1. Enter / Update Student Attendance")
        print("2. View Student Attendance Status")
        print("3. View Attendance Shortage List (< 75%)")
        print("4. Return to Main Menu")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            st_id = input("Enter Student ID: ").strip()
            attended = input("Enter Classes Attended: ").strip()
            conducted = input("Enter Total Classes Conducted: ").strip()
            try:
                status_summary = record_student_attendance(st_id, attended, conducted)
                print(f"[SUCCESS] Attendance Updated: {status_summary}")
            except StudentManagementError as err:
                print(f"[ERROR] {err}")

        elif choice == "2":
            st_id = input("Enter Student ID: ").strip()
            try:
                att_info = view_student_attendance(st_id)
                print(f"\nAttendance Record for {att_info['name']} [{att_info['student_id']}]:")
                print(f" Status       : {att_info['status_summary']}")
                print(f" Last Updated : {att_info['last_updated']}")
            except StudentManagementError as err:
                print(f"[ERROR] {err}")

        elif choice == "3":
            print("\n--- STUDENTS WITH ATTENDANCE SHORTAGE (< 75%) ---")
            shortage_list = get_all_attendance_shortage(min_percentage=75.0)
            if not shortage_list:
                print(" No students have attendance shortage.")
            else:
                for idx, item in enumerate(shortage_list, start=1):
                    print(f" {idx}. [{item['student_id']}] {item['name']:<20} ({item['department']}) "
                          f"| Attendance: {item['percentage']}% (Shortage: {item['shortage']}%)")

        elif choice == "4":
            break
        else:
            print("[INVALID] Invalid choice.")


# =====================================================================
# 5. REPORTS SUBMENU
# =====================================================================
def menu_reports():
    """Submenu for individual student reports and aggregate performance analytics."""
    while True:
        print("\n--- [5] ACADEMIC REPORTS ---")
        print("1. Generate Individual Student Report (Polymorphism)")
        print("2. Generate Class Performance & Analytical Report")
        print("3. Return to Main Menu")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            st_id = input("Enter Student ID: ").strip()
            try:
                report = generate_student_report(st_id)
                print("\n" + report)
            except StudentManagementError as err:
                print(f"[ERROR] {err}")

        elif choice == "2":
            report = generate_performance_report()
            print("\n" + report)

        elif choice == "3":
            break
        else:
            print("[INVALID] Choice must be 1, 2, or 3.")


# =====================================================================
# 6. SEARCH, FILTER & SORT SUBMENU
# =====================================================================
def menu_search_filter_sort():
    """Submenu demonstrating list comprehensions, lambda sorting, set filtering."""
    while True:
        print("\n--- [6] SEARCH, FILTER & SORT ---")
        print("1. Filter Students by Department")
        print("2. Filter Passed Students")
        print("3. Filter Failed Students")
        print("4. Filter Attendance Shortage (< 75%)")
        print("5. Sort Students by Name")
        print("6. Sort Students by GPA (Highest First)")
        print("7. Sort Students by Percentage")
        print("8. Sort Students by Attendance")
        print("9. Return to Main Menu")
        
        choice = input("Enter choice (1-9): ").strip()
        
        if choice == "1":
            dept = input("Enter Department Code (e.g. CSE, CSE-AI, ECE, EEE): ").strip()
            results = filter_students_by_department(dept)
            print(f"\nStudents in {dept.upper()} ({len(results)} found):")
            for st in results:
                print(f" - {st.display_info()}")

        elif choice == "2":
            passed = filter_passing_students()
            print(f"\nPassed Students ({len(passed)} found):")
            for st in passed:
                print(f" - [{st.student_id}] {st.name:<20} | Pct: {st.calculate_percentage()}% | GPA: {st.gpa}")

        elif choice == "3":
            failed = filter_failing_students()
            print(f"\nFailed Students ({len(failed)} found):")
            for st in failed:
                print(f" - [{st.student_id}] {st.name:<20} | Pct: {st.calculate_percentage()}% | Status: FAILED")

        elif choice == "4":
            shortage = filter_attendance_shortage(75.0)
            print(f"\nAttendance Shortage List ({len(shortage)} found):")
            for st in shortage:
                print(f" - [{st.student_id}] {st.name:<20} | Attendance: {st.attendance_percentage}%")

        elif choice == "5":
            # CONCEPT: Lambda sorting
            sorted_st = sort_students(criteria="name", reverse=False)
            print("\nStudents Sorted Alphabetically by Name:")
            for st in sorted_st:
                print(f" - {st.name:<25} | ID: {st.student_id}")

        elif choice == "6":
            sorted_st = sort_students(criteria="gpa", reverse=True)
            print("\nStudents Sorted by GPA (Highest First):")
            for st in sorted_st:
                print(f" - GPA: {st.gpa:<4} | [{st.student_id}] {st.name:<25} ({st.department})")

        elif choice == "7":
            sorted_st = sort_students(criteria="percentage", reverse=True)
            print("\nStudents Sorted by Percentage (Highest First):")
            for st in sorted_st:
                print(f" - Pct: {st.calculate_percentage():<6}% | [{st.student_id}] {st.name:<25}")

        elif choice == "8":
            sorted_st = sort_students(criteria="attendance", reverse=True)
            print("\nStudents Sorted by Attendance (Highest First):")
            for st in sorted_st:
                print(f" - Att: {st.attendance_percentage:<6}% | [{st.student_id}] {st.name:<25}")

        elif choice == "9":
            break
        else:
            print("[INVALID] Enter a choice between 1 and 9.")


# =====================================================================
# MAIN ENTRY POINT LOOP
# =====================================================================
def main():
    """
    Main Application Entry Point.
    Uses persistent while loop for navigation menu.
    """
    print_banner()
    print("[INFO] Loading student database records from JSON file...")
    loaded_list = load_all_students()
    print(f"[INFO] Successfully loaded {len(loaded_list)} student record(s).")

    # CONCEPT: Persistent Menu using while True loop
    while True:
        try:
            print_main_menu()
            user_choice = input("Enter your choice (1-8): ").strip()

            if user_choice == "1":
                menu_student_management()
            elif user_choice == "2":
                menu_subject_management()
            elif user_choice == "3":
                menu_marks_management()
            elif user_choice == "4":
                menu_attendance_management()
            elif user_choice == "5":
                menu_reports()
            elif user_choice == "6":
                menu_search_filter_sort()
            elif user_choice == "7":
                saved = save_all_students()
                if saved:
                    print("[SUCCESS] All student data saved successfully to JSON storage.")
                else:
                    print("[ERROR] Failed to save data.")
            elif user_choice == "8":
                print("\nSaving final changes before exit...")
                save_all_students()
                print("==================================================")
                print(" Thank you for using Student Management & Academic Tracker!")
                print("==================================================\n")
                sys.exit(0)
            else:
                print("[INVALID] Invalid selection. Please enter a number between 1 and 8.")
                
        except KeyboardInterrupt:
            print("\n\n[INFO] Keyboard interrupt detected. Saving progress and exiting...")
            save_all_students()
            sys.exit(0)
        except Exception as err:
            print(f"\n[UNHANDLED ERROR] An unexpected error occurred: {err}")
            print("Returning to main menu...\n")


if __name__ == "__main__":
    main()
