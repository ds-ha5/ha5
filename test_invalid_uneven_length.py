import pytest
from find_single import find_single_element


def test_invalid_length():
    with pytest.raises(ValueError):
        find_single_element([1, 2, 3, 4])
