"""Exercise Enums"""

from enum import IntEnum, Enum


class ExerciseRange(IntEnum):
    """Enum for exercise range."""

    PERFECT_UNISON = 0
    MINOR_SECOND = 1
    MAJOR_SECOND = 2
    MINOR_THIRD = 3
    MAJOR_THIRD = 4
    PERFECT_FOURTH = 5
    TRITONE = 6
    PERFECT_FIFTH = 7
    MINOR_SIXTH = 8
    MAJOR_SIXTH = 9
    MINOR_SEVENTH = 10
    MAJOR_SEVENTH = 11
    PERFECT_OCTAVE = 12
    MINOR_NINTH = 13
    MAJOR_NINTH = 14
    MINOR_TENTH = 15
    MAJOR_TENTH = 16
    PERFECT_ELEVENTH = 17
    TRITONE_OCTAVE = 18
    PERFECT_TWELFTH = 19
    MINOR_THIRTEENTH = 20
    MAJOR_THIRTEENTH = 21
    MINOR_FOURTEENTH = 22
    MAJOR_FOURTEENTH = 23
    PERFECT_DOUBLE_OCTAVE = 24

    @property
    def short(self) -> str | None:
        """Return short name for exercise range."""
        return {
            ExerciseRange.PERFECT_UNISON: "P1",
            ExerciseRange.MINOR_SECOND: "m2",
            ExerciseRange.MAJOR_SECOND: "M2",
            ExerciseRange.MINOR_THIRD: "m3",
            ExerciseRange.MAJOR_THIRD: "M3",
            ExerciseRange.PERFECT_FOURTH: "P4",
            ExerciseRange.TRITONE: "TT",
            ExerciseRange.PERFECT_FIFTH: "P5",
            ExerciseRange.MINOR_SIXTH: "m6",
            ExerciseRange.MAJOR_SIXTH: "M6",
            ExerciseRange.MINOR_SEVENTH: "m7",
            ExerciseRange.MAJOR_SEVENTH: "M7",
            ExerciseRange.PERFECT_OCTAVE: "P8",
            ExerciseRange.MINOR_NINTH: "m9",
            ExerciseRange.MAJOR_NINTH: "M9",
            ExerciseRange.MINOR_TENTH: "m10",
            ExerciseRange.MAJOR_TENTH: "M10",
            ExerciseRange.PERFECT_ELEVENTH: "P11",
            ExerciseRange.TRITONE_OCTAVE: "TT8",
            ExerciseRange.PERFECT_TWELFTH: "P12",
            ExerciseRange.MINOR_THIRTEENTH: "m13",
            ExerciseRange.MAJOR_THIRTEENTH: "M13",
            ExerciseRange.MINOR_FOURTEENTH: "m14",
            ExerciseRange.MAJOR_FOURTEENTH: "M14",
            ExerciseRange.PERFECT_DOUBLE_OCTAVE: "P16",
        }.get(self)


class ExerciseDomain(Enum):
    """Enum for exercise domain."""

    BODY = "body"
    BREATHING = "breathing"
    VOICE = "voice"  # TODO: subcategories?
    LISTENING = "listening"
    EXPRESSION = "expression"
    BLENDING = "blending"
    IMPROVISATION = "improvisation"
    INTONATION = "intonation"
