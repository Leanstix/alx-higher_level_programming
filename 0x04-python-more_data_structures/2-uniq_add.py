#!/usr/bin/python3
"""
welcome
"""


def uniq_add(my_list=[]):
    """
    (c)leanstix
    """
    if my_list == []:
        return 0
    new = my_list[:]
    new.sort()
    a = new[0]
    for i in range(1, len(new)):
        if new[i] == new[i - 1]:
            continue
        else:
            a += new[i]
    return a
