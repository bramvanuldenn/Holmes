from objects.data_objects.DataObject import DataObject
from dataclasses import dataclass


@dataclass
class PlaceData(DataObject):
    place_key: str = None
