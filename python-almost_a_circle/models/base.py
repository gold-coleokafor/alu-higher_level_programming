#!/usr/bin/python3
"""Defines the Base class."""
import json


class Base:
    """Manages the id attribute for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize with a given id or an auto-incremented one."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of a list of dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of list_objs to <Class name>.json."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
