import pytest
from find_single import find_single_element


def test_invalid_not_integer():
    with pytest.raises(ValueError):
        find_single_element([3, 3, "asas", 1, 1])
