#!/usr/bin/python3
def roman_to_int(roman_string):
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

    sum = 0
    first_time = True
    for c in roman_string:
        if first_time:
            sum += get_value(c)
            first_time = False
        else:
            current_num = get_value(c)
            if current_num > sum:
                sum = current_num - sum
            else:
                sum += current_num
    return sum
