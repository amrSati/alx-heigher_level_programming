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

    def to_json(self):
        """Dictionary representation of object"""
        return self.__dict__.copy()
