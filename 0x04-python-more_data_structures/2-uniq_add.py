#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique_list = list(set(my_list))
    for num in unique_list:
        sum += num
    return sum
