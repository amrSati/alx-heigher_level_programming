#!/usr/bin/python3

"""Defines a function that finds a peak in a list
"""


def find_peak(lst):
    """Finds a peak in a list of unsorted integers
            The algorithm uses a divide and conqure approach

    Args:
        lst (:obj:list): A list of integers

    Returns:
        int: The peak in the list if found,
                None otherwise
    """
    if not lst or type(lst) is not list or not len(lst):
        return None

    for itm in lst:
        if type(itm) is not int:
            return None

    n = len(lst)
    if n == 1:
        return lst[0]
    if n == 2:
        return max(lst)

    lo, hi = 0, n - 1
    while lo < hi:
        mid = lo + (hi - lo) / 2
        mid = int(mid)

        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return lst[mid]

        if lst[mid - 1] > lst[mid + 1]:
            hi = mid
        else:
            lo = mid + 1

    return lst[lo]
