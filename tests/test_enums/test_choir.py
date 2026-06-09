"""Tests for choir voicing enum."""

import pytest

from enums.choir import ChoirVoicingCategory, ChoirSizeCategory, ChoirAgeCategory


@pytest.mark.parametrize("choir_size_category", [csz for csz in ChoirSizeCategory])
def test_choir_size_category_values(choir_size_category: ChoirVoicingCategory) -> None:
    """Test values of choir size category."""
    assert isinstance(choir_size_category.value, str)
    if choir_size_category is ChoirSizeCategory.ALL:
        assert choir_size_category.value == "variable_size"


@pytest.mark.parametrize("choir_age_category", [csz for csz in ChoirAgeCategory])
def test_choir_age_category_values(choir_age_category: ChoirAgeCategory) -> None:
    """Test values of choir age category."""
    assert isinstance(choir_age_category.value, str)
    if choir_age_category is ChoirAgeCategory.ALL:
        assert choir_age_category.value == "mixed_age"


def test_choir_voicing_self_contains_self_and_all_contains_all_voicings() -> None:
    """Test all voicings contain themselves and "all" voicing contains every other."""
    for cv in ChoirVoicingCategory:
        assert cv in cv
        assert cv in ChoirVoicingCategory.ALL


@pytest.mark.parametrize(
    "choir_voicing, possible_super_voicing, expected_outcome",
    [
        (ChoirVoicingCategory.SATB, ChoirVoicingCategory.SATB_div, False),
        (ChoirVoicingCategory.SATB_div, ChoirVoicingCategory.SATB, True),
    ],
)
def test_choir_voicing_contains_satb_to_satb(
    choir_voicing: ChoirVoicingCategory,
    possible_super_voicing: ChoirVoicingCategory,
    expected_outcome: bool,
) -> None:
    """Test what SATB voicing includes other SATB voicing."""
    assert (choir_voicing in possible_super_voicing) == expected_outcome


@pytest.mark.parametrize(
    "satb_voicing", [ChoirVoicingCategory.SATB, ChoirVoicingCategory.SATB_div]
)
@pytest.mark.parametrize(
    "non_satb_voicing", [ChoirVoicingCategory.SA, ChoirVoicingCategory.TB]
)
def test_choir_voicing_contains_satb_to_non_to_satb(
    satb_voicing: ChoirVoicingCategory, non_satb_voicing: ChoirVoicingCategory
) -> None:
    """Test that SATB voicing include no non-SATB voicing and vice versa."""
    assert satb_voicing not in non_satb_voicing
    assert non_satb_voicing not in satb_voicing
