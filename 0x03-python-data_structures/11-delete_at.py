#!/usr/bin/python3
"""
Welcome to data structures fellas
"""


def delete_at(my_list=[], idx=0):
    """
    a function that deletes the item at a specific position in a list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
