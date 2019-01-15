#!/usr/bin/python3
# Find a peak in a list of unsorted integers
def find_peak(list_of_ints):
    """Find a peak in a list of unsorted integers
    """
    if list_of_ints is None or len(list_of_ints) == 0:
        return None
    if len(set(list_of_ints)) == 1:
        return list_of_ints[0]
    for i in range(len(list_of_ints)):
        if i == 0:
            if list_of_ints[i] > list_of_ints[i+1]:
                return list_of_ints[i]
        elif i == len(list_of_ints) - 1:
            if list_of_ints[i] > list_of_ints[i-1]:
                return list_of_ints[i]
        else:
            if list_of_ints[i-1] < list_of_ints[i] > list_of_ints[i+1]:
                return list_of_ints[i]

