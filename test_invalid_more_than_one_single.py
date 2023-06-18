import pytest
from find_single import find_single_element


def test_invalid_more_than_one_single():
    with pytest.raises(ValueError):
        find_single_element([1, 4, 6, 7, 777, 39, 999, 39, 1, 4, 6, 7])
