#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return None
    first_loop = True
    for person in a_dictionary:
        if first_loop:
            best_person = person
            score = a_dictionary[person]
            first_loop = False
        if a_dictionary[person] > score:
            score = a_dictionary[person]
            best_person = person
    return best_person
