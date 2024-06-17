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
        """Dictionary representation of object

        Args:
            attrs (:obj:list, None): List of attributes to retrieve

        Returns:
            dict: Serialization of the object
        """
        res = {}
        dic = self.__dict__.copy()

        if type(attrs) is list:
            for attr in attrs:
                if attr in dic:
                    res[attr] = dic[attr]

            return res

        return dic

    def reload_from_json(self, json):
        """Replaces all attributes of the instance

        Args:
            json (:obj:dict): Dictionary of new attributes values
        """
        ins = self.__dict__

        for attr in json:
            if attr in ins:
                setattr(self, attr, json[attr])
