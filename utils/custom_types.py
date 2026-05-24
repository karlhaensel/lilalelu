"""Custom types for lilalelu."""

from enum import IntEnum


class OrderedStrEnum(IntEnum):
    """
    Enum that returns string value but uses IntEnum ordering for simple comparison.
    """

    @property
    def value(self):
        """Overload value method to return string value while maintaining int order."""
        return self.all_value if self.name == "ALL" else self.name.lower()

    @property
    def all_value(self) -> str:
        raise NotImplementedError("Subclass must implement this property.")
