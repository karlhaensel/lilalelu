"""Choir Enums."""

from enum import Enum

from pydantic import Field
from pydantic.dataclasses import dataclass

from utils.custom_types import OrderedStrEnum


class ChoirSizeCategory(OrderedStrEnum):
    """Enum for choir size categories (sorted by size, all=0)."""

    ALL = 0
    SOLO_ENSEMBLE = 1
    VOCAL_ENSEMBLE = 2
    CHAMBER_CHOIR = 3
    CHOIR = 4
    BIG_CHOIR = 5

    @property
    def all_value(self) -> str:
        """Set str value for ALL."""
        return "variable_size"


class ChoirAgeCategory(OrderedStrEnum):
    """Enum for choir age categories (sorted by age, all=0)."""

    ALL = 0
    CHILDREN = 1
    YOUTH = 2
    ADULTS = 3
    SENIORS = 4

    @property
    def all_value(self) -> str:
        """Set str value for ALL."""
        return "mixed_age"


class ChoirVoicingCategory(Enum):
    """Enum class for choir voicing category."""

    ALL = "all"
    SATB = "SATB"
    SATB_div = "SATB_div"  # SATB choir that can divide at least into SSAATTBB.
    SA = "SA"
    TB = "TB"

    def __contains__(self, possible_subvoicing: "ChoirVoicingCategory") -> bool:
        """
        Return True if the given choir voicing is a subgroup of self.

        Usage as follows: `possible_subvoicing in some_choir_voicing`
        where `some_choir_voicing` is self.

        :param possible_subvoicing: The choir voicing to be checked.
        :return: True if it is indeed a subvoicing of self.
        """
        return (
            True
            if (
                (self is ChoirVoicingCategory.ALL)
                or (possible_subvoicing is self)
                or (
                    (self is ChoirVoicingCategory.SATB)
                    and (possible_subvoicing is ChoirVoicingCategory.SATB_div)
                )
            )
            else False
        )


@dataclass
class ChoirConfiguration:
    """Class for choir configuration."""

    choir_size_category: ChoirSizeCategory = Field(default=ChoirSizeCategory.ALL)
    choir_age_category: ChoirAgeCategory = Field(default=ChoirAgeCategory.ALL)
    choir_voicing_category: ChoirVoicingCategory = Field(
        default=ChoirVoicingCategory.ALL
    )

    @property
    def name(self) -> str:
        """Return the name of the choir configuration."""
        return (
            f"{self.choir_size_category.value} of {self.choir_age_category.value} "
            f"({self.choir_voicing_category.value})"
        )
