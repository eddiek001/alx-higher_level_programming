#!/usr/bin/python3
"""Write a class Student that defines a student """


class Student:
    """student class for use
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict rep of Student in json form
        """
        if attrs is None:
            return self.__dict__

        return {key: value for key, value in
                self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """reloads an object from a json dictionary
            -> assumes json to always be a dictionary
        """
        for key in ('first_name', 'last_name', 'age'):
            if key in json:
                setattr(self, key, json[key])
