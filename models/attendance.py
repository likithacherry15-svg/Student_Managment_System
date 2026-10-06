"""
models/attendance.py

Educational Concepts:
1. Datetime Module: Tracking timestamp of attendance records
2. Arithmetic calculations & Conditional expressions (Ternary Operator)
3. Encapsulation & Validation logic
"""

from datetime import datetime
from utils.validators import validate_attendance

DEFAULT_ATTENDANCE_REQUIREMENT = 75.0  # Constant percentage requirement


class AttendanceRecord:
    """
    Tracks classes conducted and attended for a student.
    """

    def __init__(self, conducted: int = 0, attended: int = 0, last_updated: str = None):
        # CONCEPT: Validation tuple unpacking
        self.attended, self.conducted = validate_attendance(attended, conducted)
        
        # CONCEPT: Datetime formatting
        if last_updated:
            self.last_updated = last_updated
        else:
            self.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_attendance(self, new_attended: int, new_conducted: int):
        """Updates attendance counts and updates timestamp."""
        att, cond = validate_attendance(new_attended, new_conducted)
        self.attended = att
        self.conducted = cond
        self.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # CONCEPT: Python @property for dynamic calculated value
    @property
    def percentage(self) -> float:
        """
        Calculates attendance percentage: (Attended / Conducted) * 100.
        Returns 0.0 if no classes conducted yet.
        """
        if self.conducted == 0:
            return 0.0
        # CONCEPT: Float division and rounding
        return round((self.attended / self.conducted) * 100.0, 2)

    # CONCEPT: Conditional Expression (Ternary Operator)
    @property
    def is_eligible(self) -> bool:
        """Returns True if attendance meets minimum requirement (75%)."""
        return self.percentage >= DEFAULT_ATTENDANCE_REQUIREMENT

    def get_status(self) -> str:
        """Returns eligibility string statement."""
        return "ELIGIBLE" if self.is_eligible else "NOT ELIGIBLE (SHORTAGE)"

    def get_status_summary(self) -> str:
        # CONCEPT: Ternary expression in string formatting
        status = "ELIGIBLE" if self.is_eligible else "NOT ELIGIBLE (SHORTAGE)"
        return f"Attended: {self.attended}/{self.conducted} ({self.percentage}%) - {status}"

    def to_dict(self) -> dict:
        return {
            "conducted": self.conducted,
            "attended": self.attended,
            "last_updated": self.last_updated
        }

    @classmethod
    def from_dict(cls, data: dict):
        if not data:
            return cls(0, 0)
        return cls(
            conducted=data.get("conducted", 0),
            attended=data.get("attended", 0),
            last_updated=data.get("last_updated")
        )

    def __str__(self) -> str:
        return f"{self.percentage}% ({self.attended}/{self.conducted})"
