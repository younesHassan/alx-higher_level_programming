#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print all integers of a list, in reverse order
#
# (C) 2022 Yunis Abshir, Nairobi, Kenya
# email younesabhsir@gmail.com
# -----------------------------------------------------------


def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific location
      without modifying the original
    Args:
        my_list: a list
        idx: the index of item to replace
        element: item to be substituted
    Returns:
        the edited list copy
    """

    temp_list = my_list.copy()
    if idx < 0:
        return temp_list
    if idx >= len(my_list):
        return temp_list
    temp_list[idx] = element
    return temp_list
