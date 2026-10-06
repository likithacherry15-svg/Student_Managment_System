"""
models/academic_record.py

Educational Concept: Abstraction
- Uses Python's built-in `abc` (Abstract Base Class) module.
- An abstract class defines a blueprint/contract for subclasses.
- Subclasses MUST implement all `@abstractmethod` definitions.
- Cannot be instantiated directly.
"""

from abc import ABC, abstractmethod


class AcademicRecord(ABC):
    """
    Abstract Base Class representing an academic record interface.
    Demonstrates Abstraction in Object-Oriented Programming (OOP).
    """

    @abstractmethod
    def calculate_result(self) -> dict:
        """
        Abstract method to compute summary academic performance.
        Must return a dictionary containing results like percentage, grade, status.
        """
        pass

    @abstractmethod
    def generate_report(self) -> str:
        """
        Abstract method to format and return a text-based academic performance report.
        """
        pass
