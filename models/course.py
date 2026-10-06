"""
models/course.py

Educational Concepts:
1. Data Structures: Tuples & Sets for course categories and validation
2. Classes & Instances
3. Conversion to and from Dictionary representations
"""

# CONCEPT: Tuple constant for immutable category types
COURSE_TYPES = ("Theory", "Practical/Lab", "Project", "Elective")

# CONCEPT: Set for fast unique subject code storage
SYSTEM_SUBJECT_CODES = {"CS101", "CS102", "CS103", "AI101", "EC101", "EE101", "MA101", "PH101"}


class Course:
    """
    Represents an academic subject/course.
    """

    def __init__(self, code: str, title: str, credits: int = 3, course_type: str = "Theory"):
        self.code = code.strip().upper()
        self.title = title.strip().title()
        self.credits = max(1, min(6, int(credits)))
        self.course_type = course_type if course_type in COURSE_TYPES else "Theory"

    def display_course(self) -> str:
        return f"[{self.code}] {self.title} ({self.credits} Credits, {self.course_type})"

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "title": self.title,
            "credits": self.credits,
            "course_type": self.course_type
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            code=data.get("code", "SUB101"),
            title=data.get("title", "General Subject"),
            credits=data.get("credits", 3),
            course_type=data.get("course_type", "Theory")
        )

    def __str__(self) -> str:
        return f"{self.code}: {self.title}"

    def __repr__(self) -> str:
        return f"Course(code='{self.code}', title='{self.title}', credits={self.credits})"
