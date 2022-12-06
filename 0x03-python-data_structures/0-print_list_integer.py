#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrates how to print all integers of a list
#
# (C) 2022 Hassan Mohamed, Nairobi, Kenya
# email younesabshir@gmail.com
# -----------------------------------------------------------


def print_list_integer(my_list=[]):
    """Prints all intergers of a list
    Args:
      my_list: the list argument whose items will be printed
    """

    # Iterate through list
    for integer in my_list:
        print("{:d}".format(integer))
