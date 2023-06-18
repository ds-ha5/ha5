import pytest
from find_single import find_single_element


def test_more_than_one():
    assert find_single_element([1, 4, 6, 7, 39, 999, 39, 1, 4, 6, 7]) == 999
    assert find_single_element([1, 1, 3, 5, 5]) == 3
