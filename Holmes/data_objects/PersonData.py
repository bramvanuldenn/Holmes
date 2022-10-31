from Holmes.data_objects.DataObject import DataObject
from dataclasses import dataclass


@dataclass
class PersonData(DataObject):
    data_type = 'person'
