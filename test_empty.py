import pytest
from find_single import find_single_element


def test_empty():
    assert find_single_element([]) is None
