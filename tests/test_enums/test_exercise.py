"""Test range enum."""

import pytest

from enums.exercise import ExerciseRange


@pytest.mark.parametrize("exercise_range", [er for er in ExerciseRange])
def test_short_for_exercise_range(exercise_range: ExerciseRange):
    """Test that every ExerciseRange has a short string code."""
    assert exercise_range.short is not None and isinstance(exercise_range.short, str)
