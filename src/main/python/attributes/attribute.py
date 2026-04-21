"""Module: attribute. Contains the base Attribute class"""
from abc import ABC, abstractmethod


class Attribute(ABC):
    """Abstract base class for all business attributes with validation"""

    def __init__(self, value):
        """Initialize attribute with value and validate it"""
        self._value = value
        self.validate()

    @abstractmethod
    def validate(self):
        """Validate the attribute value. Must be implemented by subclasses"""

    @abstractmethod
    def to_json(self):
        """Convert attribute to JSON representation. Must be implemented by subclasses"""

    def __str__(self):
        """String representation of the attribute"""
        return str(self._value)

    @property
    def value(self):
        """Get the attribute value"""
        return self._value
