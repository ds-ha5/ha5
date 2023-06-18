from mergesort import merge_sort
import sys


def find_single_element(pairs_and_single_list):
    '''
    Find single in list of pairs

    Returns None if empty list is passed.

    Assumes only pairs of integers and a single singlet integer are in list.
    '''
    if len(pairs_and_single_list) == 0:
        return None
    if len(pairs_and_single_list) == 1:
        return pairs_and_single_list[0]
    if len(pairs_and_single_list) % 2 != 1:
        raise ValueError("List length not uneven.")
    if not all(isinstance(x, int) for x in pairs_and_single_list):
        raise ValueError("Not all elements are integers")
    list_copy = pairs_and_single_list.copy()
    merge_sort(list_copy)
    index = 0
    candidate_single = None
    while index < len(list_copy):
        if index + 2 < len(list_copy):
            if list_copy[index] == list_copy[index + 1] and \
                    list_copy[index] == list_copy[index + 2]:
                raise ValueError("Multiplets other than double.")
        if index + 1 >= len(list_copy):
            if not candidate_single:
                candidate_single = list_copy[index]
            break
        if list_copy[index] == list_copy[index + 1]:
            index += 2
        else:
            if candidate_single:
                raise ValueError("More than one single.")
            candidate_single = list_copy[index]
            index += 1
    return candidate_single


if __name__ == "__main__":
    print(find_single_element([int(x) for x in sys.argv[1:]]))
