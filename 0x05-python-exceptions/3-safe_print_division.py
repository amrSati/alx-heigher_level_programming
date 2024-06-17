#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        div = a / b
        res = div
        return res
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(res))
