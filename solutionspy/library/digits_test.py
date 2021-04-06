import pytest

from . import perftesting
from .digits import digits_mod_div_reverse, digits_str_list

DIGITS = [digits_mod_div_reverse, digits_str_list]


@pytest.mark.parametrize("digits", DIGITS)
def test_digits_implementations(digits):
    assert digits(123) == [1, 2, 3]
    assert digits(1) == [1]


@pytest.mark.parametrize("digits", DIGITS)
def test_digits_performance(digits):
    print(perftesting.run(perftesting.on_range(10000000, digits)))
