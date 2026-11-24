#!/usr/bin/python3
"""Defines the Base class."""
import csv
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

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class>.json."""
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as f:
                data = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in data]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write list_objs to <Class>.csv, one object per row."""
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(cls.__name__ + ".csv", "w", newline="",
                  encoding="utf-8") as f:
            writer = csv.writer(f)
            if list_objs:
                for obj in list_objs:
                    d = obj.to_dictionary()
                    writer.writerow([d[k] for k in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from <Class>.csv."""
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        try:
            with open(cls.__name__ + ".csv", newline="",
                      encoding="utf-8") as f:
                rows = list(csv.reader(f))
        except FileNotFoundError:
            return []
        return [cls.create(**{k: int(v) for k, v in zip(fields, row)})
                for row in rows]
