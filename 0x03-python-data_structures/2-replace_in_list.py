#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list index
    """
    list_len = len(mylist)
    if list_len <= idx or idx < 0:
        return (my_list)

    my_list[idx] = element
    return (my_list)
