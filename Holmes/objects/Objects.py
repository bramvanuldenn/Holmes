from Holmes.objects.BaseObject import BaseObject
from dataclasses import dataclass


@dataclass
class Company(BaseObject):
    ...


@dataclass
class Domain(BaseObject):
    ...


@dataclass
class Person(BaseObject):
    ...


@dataclass
class Place(BaseObject):
    ...
