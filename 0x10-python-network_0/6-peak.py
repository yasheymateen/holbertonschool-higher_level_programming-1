#!/usr/bin/python3
# Find a peak in a list of unsorted integers


def find_peak(list_of_ints):
    """Find a peak in a list of unsorted integers
    """
    if list_of_ints is None or len(list_of_ints) == 0:
        return None
    if len(set(list_of_ints)) == 1:
        return list_of_ints[0]
    length = len(list_of_ints)
    mid = length // 2
    if length > 2:
        if list_of_ints[mid-1] < list_of_ints[mid] > list_of_ints[mid+1]:
            return list_of_ints[mid]
        else:
            if list_of_ints[mid - 1] > list_of_ints[mid + 1]:
                return find_peak(list_of_ints[:mid+1])
            else:
                return find_peak(list_of_ints[mid:])
    else:
        if list_of_ints[mid-1] > list_of_ints[mid]:
            return list_of_ints[mid-1]
        else:
            return list_of_ints[mid]
