"""Characterization tests for the original fee calculation."""

import pytest

from fees import calculate_fee


@pytest.mark.parametrize(
    "scholarship, late_payment, expected",
    [
        (False, False, 1000),
        (True, False, 900),
        (False, True, 1100),
        (True, True, 1000),
    ],
)
def test_calculate_fee(scholarship, late_payment, expected):
    """Capture the existing fee calculation behavior."""
    assert calculate_fee(scholarship, late_payment) == expected
