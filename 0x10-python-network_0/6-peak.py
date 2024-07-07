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

    return func_util(lst, 0, n - 1, n)


def func_util(lst, lo, hi, n):
    """Util to find the peak in a divide and conqure approach

    Args:
        lst (:obj:list): The list of integers
        lo (int): The lowest index
        hi (int): The highest index
        n (int): Full length of the list

    Returns:
        int: The peak in lst
    """
    mid = lo + (hi - lo) / 2
    mid = int(mid)

    if ((mid == 0 or lst[mid - 1] <= lst[mid]) and
            (mid == n - 1 or lst[mid + 1] <= lst[mid])):
        return lst[mid]

    if mid > 0 and lst[mid - 1] > lst[mid]:
        return func_util(lst, lo, mid - 1, n)
    else:
        return func_util(lst, mid + 1, hi, n)
