#!/usr/bin/python3
def get_value(c):
        if c == 'I':
            return 1
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        elif c == 'M':
            return 1000


def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0

    sum = 0
    for i in range(len(roman_string)):
        if i is (len(roman_string) - 1):
            sum += get_value(roman_string[i])
        else:
            if get_value(roman_string[i]) >= get_value(roman_string[i+1]):
                    sum += get_value(roman_string[i])
            else:
                    sum -= get_value(roman_string[i])
    return sum
