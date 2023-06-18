import pytest
from find_single import find_single_element


def test_input_array_unchanged():
    input_list = [1, 4, 6, 7, 39, 999, 39, 1, 4, 6, 7]
    input_list_copy = input_list.copy()
    find_single_element(input_list)
    for index in range(len(input_list)):
        assert input_list[index] == input_list_copy[index]
