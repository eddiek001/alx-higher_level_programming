#!/usr/bin/python3
"""define a function def copy_list(l)"""


def copy_list(l):
    """generates a copy of a list
    """
    if not isinstance(l, list):
        return None
    return l[:]
