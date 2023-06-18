# imports at beginning of file
import matplotlib.pyplot as plt


# function names should be snake case
def merge_sort(list_to_sort_by_merge):
    """
    Sort list by mergesort
    """
    # this was redundant and complicated
    if len(list_to_sort_by_merge) < 2:
        return
    # use descriptive nouns
    middle = len(list_to_sort_by_merge) // 2
    left_list = list_to_sort_by_merge[:middle]
    right_list = list_to_sort_by_merge[middle:]

    merge_sort(left_list)
    merge_sort(right_list)

    # use descriptive nouns for variables
    left_index = 0
    right_index = 0
    new_index = 0

    # function names should be snake case verbs
    # encapsulate helper function in function namespace
    # remove parameters included in every function call
    def assign_new_list(source_list, source_index):
        nonlocal new_index
        list_to_sort_by_merge[new_index] = source_list[source_index]
        new_index += 1

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            assign_new_list(source_list=left_list, source_index=left_index)
            left_index += 1
        else:
            assign_new_list(source_list=right_list, source_index=right_index)
            right_index += 1

    while left_index < len(left_list):
        assign_new_list(source_list=left_list, source_index=left_index)
        left_index += 1

    while right_index < len(right_list):
        assign_new_list(source_list=right_list, source_index=right_index)
        right_index += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# Use descriptive noun and DRY
my_list_indexes = range(len(my_list))
plt.bar(my_list_indexes, my_list)
plt.title("Before mergesort")
plt.xlabel("List index")
plt.ylabel("List value at index (a.u.)")
plt.xticks(range(len(my_list)))
plt.show()
merge_sort(my_list)
x = range(len(my_list))
plt.bar(my_list_indexes, my_list)
plt.title("After mergesort")
plt.xlabel("List index")
plt.ylabel("List value at index (a.u.)")
plt.xticks(range(len(my_list)))
plt.show()
