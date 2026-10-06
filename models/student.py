"""
models/student.py

Educational Concepts:
1. Object-Oriented Programming (OOP):
   - Inheritance: Student inherits from Person & AcademicRecord (Multiple Inheritance)
   - Hierarchy: Person -> Student -> GraduateStudent / ScholarshipStudent
   - Encapsulation: Private attributes __marks and __attendance
   - Polymorphism: Method overriding display_info(), generate_report(), calculate_result()
   - Abstraction: Implements abstract methods from AcademicRecord
2. Class Methods & Static Methods: @classmethod and @staticmethod
3. Decorators: @property getters for percentage, gpa, attendance_percentage
4. Standard Library Modules: datetime, functools (reduce)
5. Data Structures: Lists, Dictionaries, Tuples, Sets
6. Functional Programming: zip, enumerate, map, filter, lambda
"""

from datetime import datetime
from functools import reduce
from models.person import Person
from models.academic_record import AcademicRecord
from models.attendance import AttendanceRecord
from utils.validators import (
    validate_student_id,
    validate_department,
    validate_semester,
    validate_marks
)
from utils.exceptions import InvalidMarksError


class Student(Person, AcademicRecord):
    """
    Represents an undergraduate student.
    Inherits biographical fields from Person and abstract requirements from AcademicRecord.
    """

    # CONCEPT: Class variable tracking total student instances created
    total_students_count = 0

    def __init__(
        self,
        student_id: str,
        name: str,
        age: int,
        email: str,
        phone: str,
        department: str,
        year: int = 1,
        semester: int = 1,
        subjects: list = None,
        enrollment_date: str = None
    ):
        # CONCEPT: super().__init__() invokes Parent class constructor
        super().__init__(name=name, age=age, email=email, phone=phone)

        self.student_id = validate_student_id(student_id)
        self.department = validate_department(department)
        self.year = int(year)
        self.semester = validate_semester(semester)
        
        # CONCEPT: Default mutable argument safety pattern (None check)
        self.subjects = list(subjects) if subjects else []

        # CONCEPT: Encapsulation - Private attributes (prefixed with double underscore)
        # Cannot be accessed directly from outside class instance
        self.__marks = {}  # Dict mapping subject_name -> float mark
        self.__attendance = AttendanceRecord(0, 0)

        # CONCEPT: Datetime module for enrollment timestamp
        self.enrollment_date = enrollment_date or datetime.now().strftime("%Y-%m-%d")

        # Increment class variable counter
        Student.total_students_count += 1

    # CONCEPT: Encapsulation - Getter method for private marks dictionary
    def get_marks(self) -> dict:
        """Returns a copy of the private marks dictionary to protect encapsulation."""
        return dict(self.__marks)

    # CONCEPT: Encapsulation - Setter method enforcing validation logic
    def set_marks(self, marks_dict: dict):
        """Replaces all marks with validation."""
        validated = {}
        for subject, score in marks_dict.items():
            validated[subject] = validate_marks(score)
        self.__marks = validated

    def add_marks(self, subject: str, score: float):
        """Adds or updates marks for a specific subject."""
        valid_score = validate_marks(score)
        clean_subj = subject.strip()
        if clean_subj not in self.subjects:
            self.subjects.append(clean_subj)
        self.__marks[clean_subj] = valid_score

    def remove_marks(self, subject: str):
        """Removes marks for a subject if exists."""
        self.__marks.pop(subject.strip(), None)

    # CONCEPT: Encapsulation - Getter & Setter for Attendance object
    def get_attendance(self) -> AttendanceRecord:
        """Getter for attendance record."""
        return self.__attendance

    def get_attendance_record(self) -> AttendanceRecord:
        """Getter for attendance record object."""
        return self.__attendance

    def update_attendance(self, attended: int, conducted: int):
        """Updates internal attendance record."""
        self.__attendance.update_attendance(attended, conducted)

    def add_subject(self, subject: str):
        """Adds a new subject to student's subject list."""
        clean_sub = subject.strip()
        if clean_sub not in self.subjects:
            self.subjects.append(clean_sub)

    def remove_subject(self, subject: str):
        """Removes a subject from subject list and associated marks."""
        clean_sub = subject.strip()
        if clean_sub in self.subjects:
            self.subjects.remove(clean_sub)
        self.remove_marks(clean_sub)

    # CONCEPT: Dynamic property calculation for Percentage
    @property
    def percentage(self) -> float:
        """Calculates percentage based on recorded marks."""
        return self.calculate_percentage()

    def calculate_percentage(self) -> float:
        """
        Calculates average marks percentage across all subjects.
        
        # CONCEPT: Map and Reduce demonstration
        """
        if not self.__marks:
            return 0.0
        
        # CONCEPT: Extracting values and using reduce to sum
        mark_values = list(self.__marks.values())
        total_sum = reduce(lambda acc, val: acc + val, mark_values, 0.0)
        return round(total_sum / len(mark_values), 2)

    # CONCEPT: Helper method to determine grade from numeric score
    @staticmethod
    def score_to_grade(score: float) -> tuple:
        """
        Maps score (0-100) to Letter Grade and Grade Point.
        Grade scale:
          90-100 -> A+ (10.0)
          80-89  -> A  (9.0)
          70-79  -> B  (8.0)
          60-69  -> C  (7.0)
          50-59  -> D  (6.0)
          Below 50 -> F (0.0)
        """
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

    @property
    def grade(self) -> str:
        """Calculates overall letter grade from average percentage."""
        avg_pct = self.calculate_percentage()
        letter_grade, _ = Student.score_to_grade(avg_pct)
        return letter_grade

    @property
    def gpa(self) -> float:
        """Calculates GPA (0.0 to 10.0 scale) based on average subject grade points."""
        return self.calculate_gpa()

    def calculate_gpa(self) -> float:
        """
        Calculates Grade Point Average across all subjects.
        
        # CONCEPT: List comprehension with helper function call
        """
        if not self.__marks:
            return 0.0
        
        grade_points = [Student.score_to_grade(score)[1] for score in self.__marks.values()]
        # CONCEPT: Map function for aggregate calculation
        avg_gp = sum(grade_points) / len(grade_points)
        return round(avg_gp, 2)

    @property
    def attendance_percentage(self) -> float:
        """Returns student attendance percentage."""
        return self.__attendance.percentage

    def calculate_attendance(self) -> float:
        """Calculates attendance percentage."""
        return self.__attendance.percentage

    # CONCEPT: Abstraction - Implementing Abstract Base Class Method
    def calculate_result(self) -> dict:
        """
        Computes comprehensive academic performance summary.
        """
        pct = self.calculate_percentage()
        gpa_val = self.calculate_gpa()
        grade_val = self.grade
        
        # CONCEPT: List comprehension to check if any subject failed (<50)
        failed_subjects = [sub for sub, mark in self.__marks.items() if mark < 50.0]
        status = "PASSED" if (pct >= 50.0 and len(failed_subjects) == 0) else "FAILED"
        
        return {
            "student_id": self.student_id,
            "name": self.name,
            "percentage": pct,
            "gpa": gpa_val,
            "grade": grade_val,
            "status": status,
            "failed_subjects": failed_subjects,
            "attendance_percentage": self.__attendance.percentage,
            "attendance_eligible": self.__attendance.is_eligible
        }

    # CONCEPT: Abstraction - Implementing Abstract Base Class Method
    def generate_report(self) -> str:
        """
        Generates formatted academic report string.
        
        # CONCEPT: String formatting and Zip / Enumerate demonstration
        """
        res = self.calculate_result()
        lines = [
            "=" * 50,
            f"       STUDENT ACADEMIC REPORT - {self.student_id}",
            "=" * 50,
            f"Name        : {self.name}",
            f"Department  : {self.department}",
            f"Year/Sem    : Year {self.year}, Semester {self.semester}",
            f"Email       : {self.email}",
            f"Phone       : {self.phone}",
            f"Enrollment  : {self.enrollment_date}",
            "-" * 50,
            "SUBJECT MARKS:"
        ]

        if self.__marks:
            # CONCEPT: Enumerate to display numbered list of subjects
            for idx, (subj, score) in enumerate(self.__marks.items(), start=1):
                let_grade, gp = Student.score_to_grade(score)
                lines.append(f"  {idx}. {subj:<20} : {score:>6.2f} | Grade: {let_grade:<2} (GP: {gp:.1f})")
        else:
            lines.append("  No marks recorded yet.")

        lines.extend([
            "-" * 50,
            f"Overall Percentage  : {res['percentage']}%",
            f"GPA                 : {res['gpa']} / 10.0",
            f"Overall Grade       : {res['grade']}",
            f"Academic Status     : {res['status']}",
            f"Attendance Status   : {self.__attendance.get_status_summary()}",
            "=" * 50
        ])
        return "\n".join(lines)

    # CONCEPT: Polymorphism - Overriding display_info() from Person
    def display_info(self) -> str:
        base_info = super().display_info()
        return (f"{base_info} | ID: {self.student_id} | Dept: {self.department} | "
                f"Year: {self.year} | Sem: {self.semester} | GPA: {self.gpa}")

    def display_student(self) -> str:
        """Alias method for display_info."""
        return self.display_info()

    # CONCEPT: Class Method Decorator (@classmethod)
    @classmethod
    def get_total_students(cls) -> int:
        """Class method returning the total count of student objects created."""
        return cls.total_students_count

    # CONCEPT: Class Method Factory for Deserialization from JSON Dictionary
    @classmethod
    def create_from_dictionary(cls, data: dict):
        """
        Factory method to construct a Student (or subclass) instance from a dictionary.
        """
        student_type = data.get("type", "Student")
        
        # Branch based on specialized subclass type
        if student_type == "GraduateStudent":
            return GraduateStudent.from_dict_record(data)
        elif student_type == "ScholarshipStudent":
            return ScholarshipStudent.from_dict_record(data)
        
        student = cls(
            student_id=data.get("student_id"),
            name=data.get("name"),
            age=data.get("age", 20),
            email=data.get("email"),
            phone=data.get("phone", "0000000000"),
            department=data.get("department"),
            year=data.get("year", 1),
            semester=data.get("semester", 1),
            subjects=data.get("subjects", []),
            enrollment_date=data.get("enrollment_date")
        )
        
        # Restore marks dictionary
        if "marks" in data and isinstance(data["marks"], dict):
            student.set_marks(data["marks"])
        
        # Restore attendance record
        if "attendance" in data and isinstance(data["attendance"], dict):
            att_data = data["attendance"]
            student.update_attendance(
                attended=att_data.get("attended", 0),
                conducted=att_data.get("conducted", 0)
            )
            
        return student

    # CONCEPT: Static Method Decorator (@staticmethod)
    @staticmethod
    def validate_student_id_format(student_id: str) -> bool:
        """Static utility method checking ID format without needing self instance."""
        try:
            validate_student_id(student_id)
            return True
        except Exception:
            return False

    def to_dict(self) -> dict:
        """Serializes Student object to JSON-compatible dictionary."""
        return {
            "type": "Student",
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "phone": self.phone,
            "department": self.department,
            "year": self.year,
            "semester": self.semester,
            "subjects": self.subjects,
            "marks": self.get_marks(),
            "attendance": self.__attendance.to_dict(),
            "enrollment_date": self.enrollment_date
        }

    # CONCEPT: Special Dunder methods __str__ and __repr__
    def __str__(self) -> str:
        return f"[{self.student_id}] {self.name} - Dept: {self.department} (GPA: {self.gpa})"

    def __repr__(self) -> str:
        return (f"Student(id='{self.student_id}', name='{self.name}', "
                f"dept='{self.department}', gpa={self.gpa})")


# CONCEPT: Inheritance Hierarchy Level 2 (Student -> GraduateStudent)
class GraduateStudent(Student):
    """
    Subclass representing a post-graduate / research student.
    Demonstrates Inheritance and Method Overriding.
    """

    def __init__(
        self,
        student_id: str,
        name: str,
        age: int,
        email: str,
        phone: str,
        department: str,
        research_topic: str,
        advisor_name: str,
        year: int = 1,
        semester: int = 1,
        subjects: list = None,
        enrollment_date: str = None
    ):
        # Invoke super Student constructor
        super().__init__(
            student_id=student_id,
            name=name,
            age=age,
            email=email,
            phone=phone,
            department=department,
            year=year,
            semester=semester,
            subjects=subjects,
            enrollment_date=enrollment_date
        )
        self.research_topic = research_topic.strip()
        self.advisor_name = advisor_name.strip()

    # CONCEPT: Polymorphism - Overriding display_info()
    def display_info(self) -> str:
        base_info = super().display_info()
        return f"{base_info} | Research: '{self.research_topic}' | Advisor: {self.advisor_name}"

    # CONCEPT: Polymorphism - Overriding generate_report()
    def generate_report(self) -> str:
        base_report = super().generate_report()
        lines = [
            base_report,
            "GRADUATE RESEARCH DETAILS:",
            f"Research Topic : {self.research_topic}",
            f"Thesis Advisor : {self.advisor_name}",
            "=" * 50
        ]
        return "\n".join(lines)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "GraduateStudent"
        data["research_topic"] = self.research_topic
        data["advisor_name"] = self.advisor_name
        return data

    @classmethod
    def from_dict_record(cls, data: dict):
        grad_student = cls(
            student_id=data.get("student_id"),
            name=data.get("name"),
            age=data.get("age", 22),
            email=data.get("email"),
            phone=data.get("phone", "0000000000"),
            department=data.get("department"),
            research_topic=data.get("research_topic", "General Research"),
            advisor_name=data.get("advisor_name", "Unassigned"),
            year=data.get("year", 1),
            semester=data.get("semester", 1),
            subjects=data.get("subjects", []),
            enrollment_date=data.get("enrollment_date")
        )
        if "marks" in data:
            grad_student.set_marks(data["marks"])
        if "attendance" in data:
            att = data["attendance"]
            grad_student.update_attendance(att.get("attended", 0), att.get("conducted", 0))
        return grad_student


# CONCEPT: Inheritance Hierarchy Level 2 (Student -> ScholarshipStudent)
class ScholarshipStudent(Student):
    """
    Subclass representing a student receiving merit/financial scholarship.
    Demonstrates Inheritance and Polymorphism.
    """

    def __init__(
        self,
        student_id: str,
        name: str,
        age: int,
        email: str,
        phone: str,
        department: str,
        scholarship_name: str,
        scholarship_percentage: float = 25.0,
        year: int = 1,
        semester: int = 1,
        subjects: list = None,
        enrollment_date: str = None
    ):
        super().__init__(
            student_id=student_id,
            name=name,
            age=age,
            email=email,
            phone=phone,
            department=department,
            year=year,
            semester=semester,
            subjects=subjects,
            enrollment_date=enrollment_date
        )
        self.scholarship_name = scholarship_name.strip()
        self.scholarship_percentage = max(0.0, min(100.0, float(scholarship_percentage)))

    def calculate_discounted_fee(self, base_fee: float = 50000.0) -> float:
        """Calculates final fee after applying scholarship percentage discount."""
        discount = (self.scholarship_percentage / 100.0) * base_fee
        return round(base_fee - discount, 2)

    def is_scholarship_eligible(self) -> bool:
        """Scholarship retention requires minimum 8.0 GPA and 75% attendance."""
        return self.gpa >= 8.0 and self.attendance_percentage >= 75.0

    # CONCEPT: Polymorphism - Overriding display_info()
    def display_info(self) -> str:
        base_info = super().display_info()
        return (f"{base_info} | Scholarship: {self.scholarship_name} "
                f"({self.scholarship_percentage}% Discount)")

    # CONCEPT: Polymorphism - Overriding generate_report()
    def generate_report(self) -> str:
        base_report = super().generate_report()
        retention = "MAINTAINED" if self.is_scholarship_eligible() else "AT RISK (Requires GPA >= 8.0 & Attendance >= 75%)"
        lines = [
            base_report,
            "SCHOLARSHIP STATUS:",
            f"Scholarship    : {self.scholarship_name}",
            f"Discount Rate  : {self.scholarship_percentage}%",
            f"Net Tuition Fee: ${self.calculate_discounted_fee(5000.0):,.2f}",
            f"Retention      : {retention}",
            "=" * 50
        ]
        return "\n".join(lines)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "ScholarshipStudent"
        data["scholarship_name"] = self.scholarship_name
        data["scholarship_percentage"] = self.scholarship_percentage
        return data

    @classmethod
    def from_dict_record(cls, data: dict):
        scholar_student = cls(
            student_id=data.get("student_id"),
            name=data.get("name"),
            age=data.get("age", 20),
            email=data.get("email"),
            phone=data.get("phone", "0000000000"),
            department=data.get("department"),
            scholarship_name=data.get("scholarship_name", "Merit Scholarship"),
            scholarship_percentage=data.get("scholarship_percentage", 25.0),
            year=data.get("year", 1),
            semester=data.get("semester", 1),
            subjects=data.get("subjects", []),
            enrollment_date=data.get("enrollment_date")
        )
        if "marks" in data:
            scholar_student.set_marks(data["marks"])
        if "attendance" in data:
            att = data["attendance"]
            scholar_student.update_attendance(att.get("attended", 0), att.get("conducted", 0))
        return scholar_student
