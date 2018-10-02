#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except:
        print("Exception:", sys.exc_info()[1])
        return None
