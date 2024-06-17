#!/usr/bin/python3
"""
Defines ``matrix_divided()`` function.
"""


def matrix_divided(matrix, div):
    """Divides elements of ``matrix`` by ``div``

    ``matrix`` must be a list of lists of integers or floats,
    otherwise raise a ``TypeError`` exception.

    Each row of the ``matrix`` must be of the same size,
    otherwise raise a ``TypeError`` exception.

    ``div`` can't be equal to 0, otherwise raise a ``ZeroDivisionError``.

    All resulting elements should be rounded to 2 decimal places

    Args:
        matrix (:obj:list, None): list of lists of integers/floats
        div (int/float): divisior

    Returns:
        list: new matrix with the results

    Raises:
        TypeError: If the matrix type is not a list,
            its elements also not lists,
            and their elements are not int/float.
            If the size of rows in matrix aren't equal.
            If ``div`` is not int/float.

        ZeroDivisionError: If ``div`` is 0
    """
    if (type(matrix) is not list or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(el, int) or isinstance(el, float))
                for el in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
