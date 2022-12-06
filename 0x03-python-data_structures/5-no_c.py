#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print all integers of a list, in reverse order
#
# (C) 2022 Yunis Abshir, Nairobi, Kenya
# email younesabshir@gmail.com
# -----------------------------------------------------------


def no_c(my_string):
    """Removes all characters c and C from a string
    Args:
        my_list: a string
    Returns:
        the new string
    """

    # Create a mapping table(dictionary) that sets the characters
    # to their replacement values
    dict = {ord(char): None for char in "cC"}

    # Call the translate string method giving it the mapping table
    new_string = my_string.translate(dict)
    return new_string
