#!/usr/bin/python3
"""Defines all common attributes of other classes"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    """The BaseModel of the project"""

    def __init__(self, *args, **kwargs):
        """Initialise BaseModel"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """updates updated_at with today's time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def __str__(self):
        """print class name, self id """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """returns all dict keys and values of
        __dict__ instance
        """
        retdict = self.__dict__.copy()
        retdict["created_at"] = self.created_at.isoformat()
        retdict["updated_at"] = self.updated_at.isoformat()
        retdict["__class__"] = self.__class__.__name__
        return retdict

