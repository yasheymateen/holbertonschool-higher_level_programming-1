#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    def multiply_by(x):
        return x * number
    new_list = list(map(multiply_by, my_list))
    return new_list
