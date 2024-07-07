#!/usr/bin/python3

"""Defines a function that finds a peak in a list
"""


def find_peak(lst):
    """Finds a peak in a list of unsorted integers

    Args:
        lst (:obj:list): A list of integers

    Returns:
        int: The peak in the list if found,
                None otherwise
    """
    peak = 0

    if not lst or type(lst) is not list or not len(lst):
        return None

    for itm in lst:
        if type(itm) is not int:
            return None

    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return max(lst)

    for i in range(1, len(lst) - 1, 2):
        peak = lst[i - 1]

        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            return lst[i]

        if i + 2 < len(lst):
            if lst[i + 1] > lst[i] and lst[i + 1] > lst[i + 2]:
                return lst[i + 1]

    return peak
