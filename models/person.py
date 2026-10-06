"""
models/person.py

Educational Concepts:
1. Object-Oriented Programming: Base Class / Parent Class
2. Constructors: __init__()
3. Properties & Encapsulation: @property getter & setter for email
4. Special Methods: __str__(), __repr__()
"""

from utils.validators import validate_name, validate_age, validate_email, validate_phone


class Person:
    """
    Base class representing a general Person.
    Serves as the parent class for Student and other role hierarchies.
    """

    def __init__(self, name: str, age: int, email: str, phone: str):
        # CONCEPT: Constructor Initialization & Call to Validators
        self.name = validate_name(name)
        self.age = validate_age(age)
        
        # Protected attribute used internally for encapsulation property
        self._email = None
        self.email = email  # Triggers property setter validation
        
        self.phone = validate_phone(phone)

    # CONCEPT: Python @property Decorator for Encapsulation (Getter & Setter)
    @property
    def email(self) -> str:
        """Getter for email attribute."""
        return self._email

    @email.setter
    def email(self, value: str):
        """Setter for email attribute with validation."""
        self._email = validate_email(value)

    # CONCEPT: Polymorphism - Base implementation of display_info
    def display_info(self) -> str:
        """Displays basic biographical details of the person."""
        return f"Name: {self.name} | Age: {self.age} | Email: {self.email} | Phone: {self.phone}"

    # CONCEPT: Dunder / Magic Methods __str__ and __repr__
    def __str__(self) -> str:
        return f"{self.name} ({self.email})"

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}', phone='{self.phone}')"
