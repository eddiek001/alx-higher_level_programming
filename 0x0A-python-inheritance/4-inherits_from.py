#!/usr/bin/python3
""" function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """checks if an object inherited from a class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be of type 'type'")

    return isinstance(obj, a_class) and type(obj) != a_class
