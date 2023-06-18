import pytest
from find_single import find_single_element


def test_one():
    assert find_single_element([39]) == 39
