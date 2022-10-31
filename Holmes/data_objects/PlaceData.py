from Holmes.data_objects.DataObject import DataObject
from dataclasses import dataclass


@dataclass
class PlaceData(DataObject):
    data_type = 'place'
