#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return None
    truth_table = []
    for i in my_list:
        if i % 2:
            truth_table.append(False)
        else:
            truth_table.append(True)
    return truth_table
