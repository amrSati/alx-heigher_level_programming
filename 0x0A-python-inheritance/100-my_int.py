#!/usr/bin/python3

"""Defines ``MyInt`` class
"""

class MyInt(int):
    """Inherets from ``int`` class
    """

    def __eq__(self, other):
        """Reverse of is equal method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Reverse of not equal method"""
        return super().__eq__(other)
