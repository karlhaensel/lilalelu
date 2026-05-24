"""Tests for choir voicing enum."""

import pytest

from enums.choir_voicing import ChoirVoicing


def test_choir_voicing_self_contains_self_and_all_contains_all_voicings() -> None:
    """Test all voicings contain themselves and "all" voicing contains every other."""
    for cv in ChoirVoicing:
        assert cv in cv
        assert cv in ChoirVoicing.ALL


@pytest.mark.parametrize(
    "choir_voicing, possible_super_voicing, expected_outcome",
    [
        (ChoirVoicing.SATB, ChoirVoicing.SATB_div, False),
        (ChoirVoicing.SATB_div, ChoirVoicing.SATB, True),
    ],
)
def test_choir_voicing_contains_satb_to_satb(
    choir_voicing: ChoirVoicing,
    possible_super_voicing: ChoirVoicing,
    expected_outcome: bool,
) -> None:
    """Test what SATB voicing includes other SATB voicing."""
    assert (choir_voicing in possible_super_voicing) == expected_outcome


@pytest.mark.parametrize("satb_voicing", [ChoirVoicing.SATB, ChoirVoicing.SATB_div])
@pytest.mark.parametrize("non_satb_voicing", [ChoirVoicing.SA, ChoirVoicing.TB])
def test_choir_voicing_contains_satb_to_non_to_satb(
    satb_voicing: ChoirVoicing, non_satb_voicing: ChoirVoicing
) -> None:
    """Test that SATB voicing include no non-SATB voicing and vice versa."""
    assert satb_voicing not in non_satb_voicing
    assert non_satb_voicing not in satb_voicing
