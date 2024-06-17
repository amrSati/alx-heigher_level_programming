#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1 = 0
    num2 = 0

    if not tuple_a:
        if not tuple_b:
            pass
        else:
            num1 = tuple_b[0]
    else:
        if not tuple_b:
            num1 = tuple_a[0]
        else:
            num1 = tuple_a[0] + tuple_b[0]
    if len(tuple_a) < 2:
        if len(tuple_b) < 2:
            pass
        else:
            num2 = tuple_b[1]
    else:
        if len(tuple_b) < 2:
            num2 = tuple_a[1]
        else:
            num2 = tuple_a[1] + tuple_b[1]

    return (num1, num2)
