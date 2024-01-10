#!/usr/bin/python3
""" function that returns True if the object is an instance of
or if the object is an instance of a class that inherited from
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """checks if an object is sort of a class
        -> through inheritance
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be 'type'")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
