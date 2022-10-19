from objects.data_objects.DataObject import DataObject
from dataclasses import dataclass


@dataclass
class PersonData(DataObject):
    person_key: str = None
