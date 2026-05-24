"""Enum class for choir voicing."""

from enum import Enum


class ChoirVoicing(Enum):
    """Enum class for choir voicing."""

    ALL = "all"
    SATB = "SATB"
    SATB_div = "SATB_div"  # SATB choir that can divide at least into SSAATTBB.
    SA = "SA"
    TB = "TB"

    def __contains__(self, possible_subvoicing: "ChoirVoicing") -> bool:
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
                (self is ChoirVoicing.ALL)
                or (possible_subvoicing is self)
                or (
                    (self is ChoirVoicing.SATB)
                    and (possible_subvoicing is ChoirVoicing.SATB_div)
                )
            )
            else False
        )
