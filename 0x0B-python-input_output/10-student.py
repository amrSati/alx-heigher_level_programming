#!/usr/bin/python3

"""Defines ``Student`` class
"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Optional instantiation of instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of object"""
        res = {}
        dic = self.__dict__.copy()

        if type(attrs) is list:
            for attr in attrs:
                if attr in dic:
                    res[attr] = dic[attr]

            return res

        return dic
